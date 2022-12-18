# Taken from https://github.com/bigscience-workshop/biomedical/blob/main/bigbio/utils/license.py
"""
License objects.
"""

import importlib.resources as pkg_resources
import json
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Dict, Optional

from image_datasets.core import resources


@dataclass
class License:
    """
    Base class from which all licenses inherit
    Args:
        name: License title
        text: Accompanying information of the license
        link: URL to License
        version: Current version of license
        provenance: Organization providing authorization, if possible
    """

    name: Optional[str] = None
    short_name: Optional[str] = None
    text: Optional[str] = None
    link: Optional[str] = None
    version: Optional[str] = None
    provenance: Optional[str] = None

    @property
    def is_share_alike(self):
        """
        Is Share-alike?
        """
        # NOTE: leave here has an example of license properties
        raise NotImplementedError()


@dataclass
class CustomLicense(License):
    """
    This class is for custom licenses.
    It must contain the text of the license.
    Optionally its version and a link to the license webpage.
    """

    def __post_init__(self):
        if self.name is None:
            self.name = "Custom license"

        if self.text is None and self.link is None:
            raise ValueError("A `CustomLicense` must provide either (a) the license text or (b) the license link!")


def _get_variable_name(k: str) -> str:
    return k.replace("-", "_").upper().replace(".", "p").replace("+", "plus")


def load_json_licenses() -> Dict[str, str]:
    """
    Load all licenses from JSON file.
    Amend names to be valid variable names
    """

    # shamelessly compied from:
    # https://github.com/huggingface/datasets/blob/master/src/datasets/utils/metadata.py
    licenses = {
        _get_variable_name(k): v
        for k, v in json.loads(pkg_resources.read_text(resources, "licenses.json"))["licenses"].items()
    }

    licenses["ZERO_BSD"] = licenses.pop("0BSD")

    return licenses


def load_licenses() -> Dict[str, License]:
    """
    Load `_LICENSES` dict:
        - key (str) : license name
        - value (License) : instance of license class
    """

    json_licenses = load_json_licenses()

    json_licenses.update({"DUA": "Data User Agreement"})

    licenses_kwargs = {k: {"name": v} for k, v in json_licenses.items()}

    licenses = {k: License(**kwargs) for k, kwargs in licenses_kwargs.items()}

    custom_licenses: Dict[str, CustomLicense] = dict()

    licenses.update(custom_licenses)
    for k, v in licenses.items():
        v.short_name = k

    return licenses


_LICENSES = load_licenses()
Licenses = SimpleNamespace(**_LICENSES)
