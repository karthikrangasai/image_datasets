from typing import Dict

from datasets.features import Features

from image_datasets.core.schemas import classification

SCHEMA_NAME_TO_FEATURES: Dict[str, Features] = {classification.SCHEMA_NAME: classification.SCHEMA_FEATURES}
