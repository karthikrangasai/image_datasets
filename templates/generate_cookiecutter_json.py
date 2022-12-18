from image_datasets.core.constants import VALID_SCHEMA_NAMES
from pathlib import Path
import json

TEMPLATE_DIR = Path(__file__).resolve().parent

COOKIECUTTER_JSON_FILE = TEMPLATE_DIR / "cookiecutter.json"

cookiecutter_options = {
    "dataset_name": "My New Dataset",
    "__module_dataset_name": "{{ cookiecutter.dataset_name|lower|replace(' ', '-')|replace('-', '_') }}",
    "one_line_description": "This dataset is designed for XXX Image task.",
    "schema_name": list(VALID_SCHEMA_NAMES),
    "is_dataset_local": [True, False],
}

with open(COOKIECUTTER_JSON_FILE, "w") as cookiecutter_json_file:
    json.dump(cookiecutter_options, cookiecutter_json_file)
    cookiecutter_json_file.write("\n")
