# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Taken from https://huggingface.co/datasets/mnist/blob/main/mnist.py

import struct
from typing import Any, Dict, Iterator, List, Tuple, cast

import datasets
import numpy as np
from datasets.builder import GeneratorBasedBuilder
from datasets.download import DownloadManager
from datasets.info import DatasetInfo
from datasets.splits import Split, SplitGenerator

from image_datasets.core import schemas, types
from image_datasets.core.configs import ImageDatasetConfig

_LOCAL = bool("False")

_CITATION = """\
@article{lecun2010mnist,
  title={MNIST handwritten digit database},
  author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
  journal={ATT Labs [Online]. Available: http://yann.lecun.com/exdb/mnist},
  volume={2},
  year={2010}
}
"""

_DATASETNAME = "mnist"

_ONE_LINE_DESCRIPTION = """\
The MNIST dataset consists of 70,000 28x28 images of digits and is used for training image classification models.
"""

_FULL_DESCRIPTION = """\
The MNIST dataset consists of 70,000 28x28 black-and-white images in 10 classes (one for each digits), with 7,000
images per class. There are 60,000 training images and 10,000 test images.
"""

_HOMEPAGE = "http://yann.lecun.com/exdb/mnist/"

_LICENSE = "MIT"

_URLS = {
    "train_images": "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
    "train_labels": "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
    "test_images": "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz",
    "test_labels": "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz",
}

_SCHEMA = "classification"

# _SUPPORTED_TASKS = []  # example: [Tasks.CLASSIFICATION, Tasks.OBJECT_DETECTION]

_VERSION = "1.0.0"


class MNIST(GeneratorBasedBuilder):
    f"""{_ONE_LINE_DESCRIPTION}"""

    DEFAULT_CONFIG_NAME = _DATASETNAME  # type: ignore
    BUILDER_CONFIG_CLASS = ImageDatasetConfig  # type: ignore
    BUILDER_CONFIGS = [
        ImageDatasetConfig(
            name=_DATASETNAME,
            version=datasets.Version(_VERSION),
            description=_ONE_LINE_DESCRIPTION,
            schema=_SCHEMA,
        )
    ]

    def _info(self) -> DatasetInfo:
        assert isinstance(self.config, ImageDatasetConfig)

        dataset_schema = self.config.schema
        features_getter = cast(types.CLASSIFICATION_FEATURE_GETTER_FUNC, schemas.SCHEMA_NAME_TO_FEATURES[dataset_schema])  # type: ignore

        features = features_getter(names=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        return DatasetInfo(
            description=_FULL_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: DownloadManager) -> List[SplitGenerator]:
        """Returns SplitGenerators."""
        data_dir = cast(Dict[str, str], dl_manager.download_and_extract(_URLS))

        return [
            SplitGenerator(
                name=Split.TRAIN, gen_kwargs={"filepath": (data_dir["train_images"], data_dir["train_labels"])}  # type: ignore
            ),
            SplitGenerator(
                name=Split.TEST, gen_kwargs={"filepath": (data_dir["test_images"], data_dir["test_labels"])}  # type: ignore
            ),
        ]

    def _generate_examples(self, filepath: Tuple[str, str]) -> Iterator[Tuple[int, Dict[str, Any]]]:  # type: ignore
        """Yields examples as (key, example) tuples."""
        images_file_path, labels_file_path = filepath

        # Images
        with open(images_file_path, "rb") as images_file:
            # First 16 bytes contain some metadata
            _ = images_file.read(4)
            size = struct.unpack(">I", images_file.read(4))[0]
            _ = images_file.read(8)
            images = np.frombuffer(images_file.read(), dtype=np.uint8).reshape(size, 28, 28)

        # Labels
        with open(labels_file_path, "rb") as labels_file:
            # First 8 bytes contain some metadata
            _ = labels_file.read(8)
            labels = np.frombuffer(labels_file.read(), dtype=np.uint8)

        for idx in range(size):
            yield idx, {"id": str(idx), "image": images[idx], "label": str(labels[idx])}
