#!/usr/bin/env python3
"""Build reproducible public release packages for Codex and generic skill platforms."""

import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path
from zipfile import ZipInfo


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = "0.3.7"
GENERIC_NAME = "simaguang-perspective-public"
PLUGIN_NAME = "simaguang-perspective"
RELEASE_DATE = (2026, 8, 27, 0, 0, 0)

GENERIC_FILES = [
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "README.md",
    "SKILL.md",
    "manifest.json",
    "产品说明.md",
    "examples",
    "references",
    "scripts",
    "sources",
    "test-prompts.json",
    "knowledge/README.md",
    "knowledge/summaries",
]

SKILL_FILES = [
    "LICENSE",
    "SKILL.md",
    "examples",
    "references",
    "scripts",
    "sources",
    "test-prompts.json",
]


def ignored_files(directory: str, names: list[str]) -> set[str]:
    ignored = {".DS_Store", "__pycache__"}
    ignored.update(name for name in names if name.endswith(".pyc") or name == "build_release.py")
    return ignored


def copy_path(src: Path, dst: Path) -> None:
    if src.is_dir():
        shutil.copytree(src, dst, ignore=ignored_files, dirs_exist_ok=True)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def copy_public_files(dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for rel in GENERIC_FILES:
        copy_path(ROOT / rel, dest / rel)


def copy_skill_files(dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for rel in SKILL_FILES:
        copy_path(ROOT / rel, dest / rel)


def write_plugin_manifest(plugin_root: Path) -> None:
    manifest_path = ROOT / "platforms" / "codex-plugin" / "plugin.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    plugin_dir = plugin_root / ".codex-plugin"
    plugin_dir.mkdir(parents=True, exist_ok=True)
    (plugin_dir / "plugin.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def make_zip(source_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file() and path.name not in (".DS_Store",):
                rel = path.relative_to(source_dir)
                info = ZipInfo(f"{source_dir.name}/{rel}", date_time=RELEASE_DATE)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
                with path.open("rb") as handle:
                    archive.writestr(info, handle.read())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    DIST.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="simaguang-generic-") as tmp:
        tmp_root = Path(tmp)
        generic_root = tmp_root / GENERIC_NAME
        copy_public_files(generic_root)
        shutil.copy2(ROOT / "platforms" / "generic" / "README.md", generic_root / "README.md")
        generic_zip = DIST / f"{GENERIC_NAME}-{VERSION}.zip"
        make_zip(generic_root, generic_zip)

    with tempfile.TemporaryDirectory(prefix="simaguang-plugin-") as tmp:
        tmp_root = Path(tmp)
        plugin_root = tmp_root / PLUGIN_NAME
        plugin_root.mkdir(parents=True, exist_ok=True)
        copy_path(ROOT / "LICENSE", plugin_root / "LICENSE")
        write_plugin_manifest(plugin_root)
        skill_root = plugin_root / "skills" / PLUGIN_NAME
        copy_skill_files(skill_root)

        plugin_readme = ROOT / "platforms" / "codex-plugin" / "README.md"
        shutil.copy2(plugin_readme, plugin_root / "README.md")

        plugin_zip = DIST / f"{PLUGIN_NAME}-{VERSION}-codex-plugin.zip"
        make_zip(plugin_root, plugin_zip)

        marketplace_root = tmp_root / "simaguang-perspective-marketplace"
        marketplace_root.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            plugin_root,
            marketplace_root / "plugins" / PLUGIN_NAME,
            ignore=ignored_files,
        )
        shutil.copy2(
            ROOT / "platforms" / "codex-plugin" / "marketplace.json",
            marketplace_root / "marketplace.json",
        )
        marketplace_zip = DIST / f"{PLUGIN_NAME}-{VERSION}-codex-marketplace.zip"
        make_zip(marketplace_root, marketplace_zip)

    package_paths = [generic_zip, plugin_zip, marketplace_zip]
    optional = [
        DIST / f"{GENERIC_NAME}-{VERSION}-knowledge.zip",
        DIST / f"{PLUGIN_NAME}-{VERSION}-codex-knowledge.zip",
    ]
    package_paths.extend(path for path in optional if path.exists())

    checksums = []
    for path in package_paths:
        checksum = sha256(path)
        checksums.append(f"{checksum}  {path.name}")
        print(f"{path.name}: {path.stat().st_size} bytes, sha256 {checksum}")

    (DIST / "SHA256SUMS.txt").write_text("\n".join(checksums) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
