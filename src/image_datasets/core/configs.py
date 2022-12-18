# type: ignore
from dataclasses import dataclass
from typing import Optional, Type

from datasets.builder import BuilderConfig
from datasets.utils import Version


@dataclass
class ImageDatasetConfig(BuilderConfig):
    """BuilderConfig for an Image Dataset."""

    name: Optional[str] = None
    version: Optional[Version] = None
    description: Optional[str] = None
    schema: Optional[str] = None
