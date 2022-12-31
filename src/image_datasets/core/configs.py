from dataclasses import dataclass
from typing import Optional

from datasets.builder import BuilderConfig
from datasets.utils import Version


@dataclass
class ImageDatasetConfig(BuilderConfig):
    """BuilderConfig for an Image Dataset."""

    name: str = "default"
    version: Optional[Version] = None
    description: Optional[str] = None
    schema: Optional[str] = None
