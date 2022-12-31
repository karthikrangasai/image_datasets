from typing import Callable, Dict, Union

from datasets.features import Features

from image_datasets.core.schemas import classification

SCHEMA_NAME_TO_FEATURES: Dict[str, Union[Features, Callable[..., Features]]] = {
    classification.SCHEMA_NAME: classification.get_classification_features
}
