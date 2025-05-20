import pathlib

from robot.api.deco import keyword

from qcrboxapiclient.models.create_dataset_body import CreateDatasetBody
from qcrboxapiclient.types import File


@keyword
def should_not_be_none(value, name="Value"):
    if value is None:
        raise AssertionError(f"{name} should not be None.")


@keyword
def check_object_has_attributes(object, *attributes):
    missing = [attribute for attribute in attributes if not hasattr(object, attribute)]
    if missing:
        raise AssertionError(f"Object is missing attributes: {missing}")


@keyword
def create_file_upload_body(file_path):
    file_path = pathlib.Path(file_path)

    if not file_path.exists():
        raise AssertionError(f"No file exists at {file_path}")

    with file_path.open("rb") as file_in:
        file = File(file_in.read(), file_path.name)

    return CreateDatasetBody(file)
