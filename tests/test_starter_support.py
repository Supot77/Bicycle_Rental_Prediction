"""Protect the handoff contract; synthetic CSVs exist only in temporary tests."""

import tempfile
import unittest
from pathlib import Path

from starter_support import configuration_problems, inspect_dataset_header, resolve_dataset_path


class ContractTests(unittest.TestCase):
    def setUp(self):
        # Independent of the real settings students will legitimately change.
        self.config = {
            "task": "regression",
            "dataset": {"path": None, "encoding": "utf-8-sig", "delimiter": ","},
            "prediction": {"target": None, "unit": None, "context": None,
                           "time_column": None, "numeric_features": [],
                           "categorical_features": [], "excluded_columns": []},
        }

    def ready_config(self):
        self.config["dataset"]["path"] = "data/raw/test.csv"
        self.config["prediction"].update(
            target="rentals", unit="rentals/hour", context="test fixture only",
            numeric_features=["temperature"], categorical_features=["day_type"],
        )
        return self.config

    def test_waiting_for_dataset_is_valid_but_not_ready(self):
        self.assertEqual(configuration_problems(self.config), [])
        self.assertTrue(configuration_problems(self.config, require_ready=True))

    def test_target_cannot_be_an_input(self):
        config = self.ready_config()
        config["prediction"]["numeric_features"].append("rentals")
        self.assertTrue(any("target อยู่" in item for item in configuration_problems(config)))

    def test_features_cannot_overlap_or_include_excluded_columns(self):
        config = self.ready_config()
        config["prediction"]["categorical_features"].append("temperature")
        config["prediction"]["excluded_columns"] = ["temperature"]
        self.assertGreaterEqual(len(configuration_problems(config)), 2)

    def test_paths_must_stay_inside_data(self):
        for path in ("../outside.csv", "data/../../outside.csv", "/tmp/file.csv", "C:/data/file.csv"):
            with self.subTest(path=path):
                self.config["dataset"]["path"] = path
                with self.assertRaises(ValueError):
                    resolve_dataset_path(self.config)

    def test_malformed_settings_give_messages(self):
        self.config["prediction"]["numeric_features"] = "temperature"
        self.config["dataset"]["encoding"] = "not-an-encoding"
        self.config["dataset"]["delimiter"] = ""
        self.assertGreaterEqual(len(configuration_problems(self.config)), 3)

    def test_header_check_rejects_missing_or_duplicate_columns(self):
        config = self.ready_config()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "data/raw").mkdir(parents=True)
            file = root / "data/raw/test.csv"
            for header in ("rentals,temperature,day_type\n", "rentals,temperature\n", "rentals,temperature,day_type,day_type\n"):
                file.write_text(header, encoding="utf-8")
                result = inspect_dataset_header(config, root)
                if header == "rentals,temperature,day_type\n":
                    self.assertEqual(result, [])
                else:
                    self.assertTrue(result)

    def test_missing_dataset_is_reported_without_creating_it(self):
        with tempfile.TemporaryDirectory() as folder:
            problems = inspect_dataset_header(self.ready_config(), Path(folder))
            self.assertTrue(any("ไม่พบ dataset" in problem for problem in problems))


if __name__ == "__main__":
    unittest.main()
