"""
Classification Schema
"""
from datasets.features import Array2D, Features, Image, Value

SCHEMA_NAME = "classification"
SCHEMA_FEATURES = Features(
    {
        "id": Value("string"),
        "image": Image(decode=True),
        "label": Value(dtype="int32", id=None),
    }
)
