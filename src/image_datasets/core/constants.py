from collections import defaultdict
from enum import Enum
from types import SimpleNamespace

from image_datasets.core.license import License
from image_datasets.core.schemas import SCHEMA_NAME_TO_FEATURES

IMAGE_DATASET_VALUES = SimpleNamespace(NULL="<BB_NULL_STR>")

METADATA: dict = {
    "_LOCAL": bool,
    "_LICENSE": License,
    "_DISPLAYNAME": str,
}


# class Tasks(Enum):
#     CLASSIFICATION = "CLASS"
#     OBJECT_DETECTION = "OBJDET"
#     SEMANTIC_SEGMENTATION = "SEMSEG"
#     VISUAL_QUESTION_ANSWERING = "VQA"
#     STYLE_TRANSFER = "STYLE"


# TASK_TO_SCHEMA = {
#     Tasks.IMAGE_CLASSIFICATION: CLASSIFICATION_FEATURES,
#     # Tasks.OBJECT_DETECTION: "KB",
#     # Tasks.SEMANTIC_SEGMENTATION: "KB",
#     # Tasks.VISUAL_QUESTION_ANSWERING: "KB",
#     # Tasks.STYLE_TRANSFER: "KB",
# }

# SCHEMA_TO_TASKS = defaultdict(set)
# for task, schema in TASK_TO_SCHEMA.items():
#     SCHEMA_TO_TASKS[schema.schema_name].add(task)
# SCHEMA_TO_TASKS = dict(SCHEMA_TO_TASKS)

# VALID_TASKS = set(TASK_TO_SCHEMA.keys())
VALID_SCHEMA_NAMES = set(SCHEMA_NAME_TO_FEATURES.keys())
