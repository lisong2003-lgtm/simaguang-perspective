#!/usr/bin/env python3
"""Build the optional knowledge extension package with full book skill packs."""

import hashlib
import zipfile
from pathlib import Path
from zipfile import ZipInfo


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = "0.3.1"
RELEASE_DATE = (2026, 8, 24, 0, 0, 0)


def make_zip(source_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file() and path.name != ".DS_Store":
                rel = path.relative_to(source_dir)
                info = ZipInfo(f"{source_dir.name}/{rel}", date_time=RELEASE_DATE)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
                with path.open("rb") as handle:
                    archive.writestr(info, handle.read())


def make_codex_knowledge_zip(source_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = Path("simaguang-perspective/skills/simaguang-perspective")
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file() and path.name != ".DS_Store":
                rel = prefix / "knowledge" / path.relative_to(source_dir)
                info = ZipInfo(str(rel), date_time=RELEASE_DATE)
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
    knowledge = ROOT / "knowledge"
    if not knowledge.exists():
        raise SystemExit("knowledge directory not found")
    output = DIST / f"simaguang-perspective-public-{VERSION}-knowledge.zip"
    make_zip(knowledge, output)
    codex_output = DIST / f"simaguang-perspective-{VERSION}-codex-knowledge.zip"
    make_codex_knowledge_zip(knowledge, codex_output)
    for path in (output, codex_output):
        print(f"{path.name}: {path.stat().st_size} bytes, sha256 {sha256(path)}")
    checksums = []
    for path in sorted(DIST.glob("*.zip")):
        checksum = sha256(path)
        checksums.append(f"{checksum}  {path.name}")
    (DIST / "SHA256SUMS.txt").write_text("\n".join(checksums) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
