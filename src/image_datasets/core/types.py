from typing import Callable, Dict, Optional

from datasets.features import Features

CLASSIFICATION_FEATURE_GETTER_FUNC = Callable[..., Features]
