import json
from pathlib import Path
from typing import Any, Optional

BASE_DIR = Path.home() / ".ai_study_planner"
BASE_DIR.mkdir(exist_ok=True)

def save_to_file(data: Any, filename: str) -> None:
    filepath = BASE_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_file(filename: str) -> Optional[Any]:
    filepath = BASE_DIR / filename
    if not filepath.exists():
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
