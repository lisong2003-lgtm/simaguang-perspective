"""Path helpers for Git Bash and Windows Python interop."""

import os
import re
import tempfile
from pathlib import Path


def as_native_path(value):
    raw = os.fspath(value) if value is not None else ""
    raw = str(raw).strip()
    if not raw:
        return raw
    if os.name == "nt":
        match = re.match(r"^/([a-zA-Z])/(.*)$", raw)
        if match:
            return f"{match.group(1).upper()}:\\{match.group(2).replace('/', os.sep)}"
        if raw.startswith("/tmp/"):
            return str(Path(tempfile.gettempdir()) / raw[len("/tmp/"):].replace("/", os.sep))
    return raw
