"""Check starter integrity without requiring pandas or a dataset."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from starter_support import configuration_problems, inspect_dataset_header, load_config


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-data", action="store_true", help="Require completed config and CSV header")
    args = parser.parse_args()
    problems = []
    try:
        config = load_config()
        problems.extend(configuration_problems(config))
        if args.require_data and not problems:
            problems.extend(inspect_dataset_header(config))
    except (OSError, ValueError) as error:
        problems.append(f"Cannot read config: {error}")
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    expected = {
        "00_orientation.ipynb", "01_understand_dataset.ipynb",
        "02_explore_quality.ipynb", "03_split_and_preprocess.ipynb",
        "04_models_and_evaluation.ipynb", "05_app_testing_monitoring.ipynb",
    }
    missing = expected - {path.name for path in notebooks}
    if missing:
        problems.append("Missing starter notebooks: " + ", ".join(sorted(missing)))
    for path in notebooks:
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
                problems.append(f"Invalid notebook structure: {path.name}")
                continue
            for cell in notebook["cells"]:
                if cell["cell_type"] == "code":
                    source = cell["source"]
                    compile("".join(source) if isinstance(source, list) else source, path.name, "exec")
                    if cell.get("outputs") or cell.get("execution_count") is not None:
                        problems.append(f"Clear notebook outputs before sharing: {path.name}")
        except (OSError, ValueError, KeyError, SyntaxError) as error:
            problems.append(f"Notebook check failed ({path.name}): {error}")
    if problems:
        for problem in problems:
            print(f"[CHECK] {problem}")
        return 1
    print("[OK] Starter structure, notebook code syntax and configuration are valid.")
    print("[NOTE] This does not validate ML results, split design or deployment.")
    if args.require_data:
        print("[OK] The configured CSV header matches the declared columns.")
    else:
        print("[NOTE] Dataset readiness is optional. Later run with --require-data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
