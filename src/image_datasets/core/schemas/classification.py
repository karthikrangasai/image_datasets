"""
Classification Schema
"""
from typing import List, Optional

from datasets.features import ClassLabel, Features, Image, Value

SCHEMA_NAME = "classification"


def get_classification_features(
    num_classes: Optional[int] = None,
    names: Optional[List[str]] = None,
    names_file: Optional[str] = None,
    id: Optional[str] = None,
) -> Features:
    return Features(
        {
            "id": Value("string"),
            "image": Image(decode=True),
            "label": ClassLabel(
                num_classes=num_classes,
                names=names,  # type: ignore
                names_file=names_file,
                id=id,
            ),
        }
    )
