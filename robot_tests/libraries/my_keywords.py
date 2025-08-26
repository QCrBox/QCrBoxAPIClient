import io
import pathlib
import zipfile

from robot.api.deco import keyword

from qcrboxapiclient.models.append_to_dataset_body import AppendToDatasetBody
from qcrboxapiclient.models.create_data_file_body import CreateDataFileBody
from qcrboxapiclient.models.create_dataset_body import CreateDatasetBody
from qcrboxapiclient.models.create_interactive_session_parameters import CreateInteractiveSessionParameters
from qcrboxapiclient.models.create_interactive_session_parameters_command_arguments import (
    CreateInteractiveSessionParametersCommandArguments,
)
from qcrboxapiclient.models.invoke_command_parameters import InvokeCommandParameters
from qcrboxapiclient.models.invoke_command_parameters_command_arguments import InvokeCommandParametersCommandArguments
from qcrboxapiclient.types import File


@keyword
def should_be_none(value, name="Value"):
    if value is not None:
        raise AssertionError(f"{name} should not be None")


@keyword
def should_not_be_none(value, name="Value"):
    if value is None:
        raise AssertionError(f"{name} should not be None")


@keyword
def check_object_has_attributes(object, *attributes):
    missing = [attribute for attribute in attributes if not hasattr(object, attribute)]
    if missing:
        raise AssertionError(f"Object is missing attributes: {missing}")


@keyword
def construct_create_dataset_body(file_path):
    file_path = pathlib.Path(file_path)

    if not file_path.exists():
        raise AssertionError(f"No file exists at {file_path}")

    with file_path.open("rb") as file_in:
        file = File(io.BytesIO(file_in.read()), file_path.name)

    return CreateDatasetBody(file)

@keyword
def construct_create_data_file_body(file_path):
    file_path = pathlib.Path(file_path)

    if not file_path.exists():
        raise AssertionError(f"No file exists at {file_path}")

    with file_path.open("rb") as file_in:
        file = File(io.BytesIO(file_in.read()), file_path.name)

    return CreateDataFileBody(file)


@keyword
def construct_append_to_dataset_body(file_path):
    file_path = pathlib.Path(file_path)

    if not file_path.exists():
        raise AssertionError(f"No file exists at {file_path}")

    with file_path.open("rb") as file_in:
        file = File(io.BytesIO(file_in.read()), file_path.name)

    return AppendToDatasetBody(file)


@keyword
def create_interactive_session_create_body(application_slug, application_version, arguments):
    arguments = CreateInteractiveSessionParametersCommandArguments.from_dict(arguments)
    return CreateInteractiveSessionParameters(application_slug, application_version, arguments)


@keyword
def create_invoke_command_body(application_slug, application_version, command_name, arguments):
    arguments = InvokeCommandParametersCommandArguments.from_dict(arguments)
    return InvokeCommandParameters(application_slug, application_version, command_name, arguments)


@keyword
def get_command_parameter_names(parameters):
    return parameters.to_dict().keys()


@keyword
def validate_is_zip(file_path):
    zf = zipfile.ZipFile(file_path)
    bad_file = zf.testzip()
    assert bad_file is None
    zf.close()
