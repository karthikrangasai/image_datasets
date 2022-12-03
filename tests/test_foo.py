from importlib.util import find_spec


def test_foo() -> None:
    assert find_spec("image_datasets") is not None
