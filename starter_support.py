"""Small setup helpers; students implement the ML workflow in notebooks."""

import codecs
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_config(root: Path = ROOT) -> dict:
    """Read shared settings without guessing missing dataset details."""
    with (root / "config" / "project.json").open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def resolve_dataset_path(config: dict, root: Path = ROOT) -> Path | None:
    """Require a repository-relative path inside data/, including symlinks."""
    value = config["dataset"]["path"]
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError("dataset.path ต้องเป็นข้อความหรือ null")
    relative = Path(value)
    if relative.is_absolute() or "\\" in value or ":" in value:
        raise ValueError("dataset.path ใช้เส้นทางสัมพัทธ์ เช่น data/raw/ชื่อไฟล์.csv")
    path = (root / relative).resolve()
    if not path.is_relative_to((root / "data").resolve()):
        raise ValueError("dataset.path ต้องอยู่ภายใน data/ ของโครงงาน")
    if path.suffix.lower() != ".csv":
        raise ValueError("ตัวช่วยเริ่มต้นรองรับ CSV; หากได้รูปแบบอื่นให้ปรับตัวอ่านร่วมกัน")
    return path


def configuration_problems(config: dict, require_ready: bool = False) -> list[str]:
    """Validate syntax and obvious input-contract mistakes, not ML suitability."""
    problems = []
    if not isinstance(config, dict):
        return ["config ต้องเป็น JSON object"]
    if config.get("task") != "regression":
        problems.append("task ของโครงงานนี้ต้องเป็น regression")
    data, prediction = config.get("dataset"), config.get("prediction")
    if not isinstance(data, dict) or not isinstance(prediction, dict):
        return problems + ["config ต้องมี dataset และ prediction ที่เป็น object"]
    if "path" not in data:
        problems.append("dataset ต้องมี path (เริ่มต้นเป็น null ได้)")
    else:
        try:
            resolve_dataset_path(config)
        except ValueError as error:
            problems.append(str(error))
    encoding = data.get("encoding")
    try:
        codecs.lookup(encoding if isinstance(encoding, str) else "")
    except LookupError:
        problems.append("dataset.encoding ไม่ใช่ encoding ที่ Python รู้จัก")
    delimiter = data.get("delimiter")
    if not isinstance(delimiter, str) or len(delimiter) != 1 or delimiter in "\r\n":
        problems.append("dataset.delimiter ต้องเป็นอักขระคั่นหนึ่งตัว")
    for key in ("target", "unit", "context", "time_column"):
        value = prediction.get(key)
        if key not in prediction or (value is not None and
                                     (not isinstance(value, str) or not value.strip())):
            problems.append(f"prediction.{key} ต้องเป็นข้อความที่ไม่ว่างหรือ null")
    lists = {}
    for key in ("numeric_features", "categorical_features", "excluded_columns"):
        value = prediction.get(key)
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            problems.append(f"prediction.{key} ต้องเป็น list ของชื่อคอลัมน์")
            lists[key] = []
        else:
            lists[key] = value
            if len(value) != len(set(value)):
                problems.append(f"prediction.{key} มีชื่อซ้ำ")
    features = lists["numeric_features"] + lists["categorical_features"]
    if len(features) != len(set(features)):
        problems.append("feature ซ้ำระหว่าง numeric กับ categorical")
    target = prediction.get("target")
    if isinstance(target, str) and target in features:
        problems.append("target อยู่ใน features: ต้องตัดคำตอบออกจาก X")
    if set(features) & set(lists["excluded_columns"]):
        problems.append("คอลัมน์ที่ตัดออกยังอยู่ใน features")
    if require_ready:
        for label, value in (("dataset.path", data.get("path")),
                             ("prediction.target", target),
                             ("prediction.unit", prediction.get("unit")),
                             ("prediction.context", prediction.get("context"))):
            if not value:
                problems.append(f"ยังไม่ได้กำหนด {label} หลังตรวจข้อมูลกับอาจารย์")
        if not features:
            problems.append("ยังไม่ได้กำหนด features จากข้อมูลจริง")
    return problems


def inspect_dataset_header(config: dict, root: Path = ROOT) -> list[str]:
    """Read only the CSV header and check the declared contract."""
    problems = configuration_problems(config, require_ready=True)
    if problems:
        return problems
    try:
        path = resolve_dataset_path(config, root)
        if not path.is_file():
            return ["ไม่พบ dataset ตาม config; วางไฟล์ใน data/raw/ ก่อน"]
        with path.open(encoding=config["dataset"]["encoding"], newline="") as handle:
            header = next(csv.reader(handle, delimiter=config["dataset"]["delimiter"]), [])
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        return [f"อ่านหัวตารางไม่ได้: {error}"]
    if not header or any(not name.strip() for name in header):
        return ["CSV ไม่มีหัวตารางหรือมีชื่อคอลัมน์ว่าง"]
    if len(header) != len(set(header)):
        problems.append("CSV มีชื่อคอลัมน์ซ้ำ")
    prediction = config["prediction"]
    declared = [prediction["target"]] + prediction["numeric_features"] + prediction["categorical_features"]
    declared += prediction["excluded_columns"]
    if prediction["time_column"]:
        declared.append(prediction["time_column"])
    missing = sorted(set(declared) - set(header))
    if missing:
        problems.append("ไม่พบคอลัมน์ที่ประกาศ: " + ", ".join(missing))
    return problems
