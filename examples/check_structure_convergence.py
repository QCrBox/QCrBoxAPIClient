"""Invoking an non-interactive qcrboxtools command."""

import io
import pathlib
import time

from qcrboxapiclient.api.calculations import get_calculation_by_id, stop_running_calculation
from qcrboxapiclient.api.commands import invoke_command
from qcrboxapiclient.api.datasets import create_dataset, delete_dataset_by_id
from qcrboxapiclient.client import Client
from qcrboxapiclient.models import (
    CreateDatasetBody,
    InvokeCommandParameters,
    InvokeCommandParametersCommandArguments,
    QCrBoxErrorResponse,
    QCrBoxResponseCalculationsResponse,
)
from qcrboxapiclient.types import File

# Create a synchronous client, which is passed to each `sync()` for an API endpoint
# via keyword
client = Client(base_url="http://127.0.0.1:11000")

# Example file in QCrBox repository, but could substitite with `work.cif`
cif1 = pathlib.Path(
    "/Users/saultyevil/srsg-projects/QCrBox/QCrBox/.build/QCrBoxTools/tests/analyse/cif_files/difference_test1.cif"
)
cif2 = pathlib.Path(
    "/Users/saultyevil/srsg-projects/QCrBox/QCrBox/.build/QCrBoxTools/tests/analyse/cif_files/difference_test2.cif"
)


def upload_dataset(file_to_upload):
    # To upload the file to the registry, we need to create a dataset and attach the
    # file to it. Files are sent via the API as binary in a CreateDatasetBody payload
    with file_to_upload.open("rb") as f:
        file = File(io.BytesIO(f.read()), file_to_upload.name)
    upload_payload = CreateDatasetBody(file)

    # Uploading the file with this endpoint creates a dataset containing this file.
    # Assuming everything went OK, thn we will get a QCrBoxResponse. If an error
    # occurred then the response is of type QCrBoxErrorResponse
    response = create_dataset.sync(client=client, body=upload_payload)
    if isinstance(response, QCrBoxErrorResponse) or response is None:
        raise TypeError("Failed to upload file", response)
    else:
        print("Created dataset:", response)

    # The response returns the created object in payload.datasets[0]. Note that this
    # doesn't contain any of the file's binary data and instead contains metadata
    # about the dataset and data files in the data set.
    dataset_id = response.payload.datasets[0].qcrbox_dataset_id
    data_file_id = response.payload.datasets[0].data_files[file_to_upload.name].qcrbox_file_id

    return dataset_id, data_file_id


dataset1, data_file1 = upload_dataset(cif1)
dataset2, data_file2 = upload_dataset(cif2)


# To invoke a non-interactive command, we need to create objects which represent
# the JSON data sent in the request to the API
arguments = InvokeCommandParametersCommandArguments.from_dict(
    {
        "cif1": {"data_file_id": data_file1},
        "cif2": {"data_file_id": data_file2},
        # "max_abs_position": None,
        # "max_position_su": None,
        # "max_abs_uij": None,
        # "max_uij_su": None,
        "output_json_path": "/opt/qcrbox/check_structure_convergence.json",
    }
)
create_session = InvokeCommandParameters("qcrboxtools", "0.0.5", "check_structure_convergence", arguments)

# Send the request to the API
try:
    response = invoke_command.sync(client=client, body=create_session)
    if isinstance(response, QCrBoxErrorResponse) or response is None:
        raise TypeError("Failed to invoke command", response)
    else:
        print("Invoked command session:", response)

    # The response from this endpoint is slightly different as it returns a reference
    # to the create object, rather than the object iself. The payload contains the
    # interactive_session_id which is also the calcualtion id of the interactive session
    calculation_id = response.payload.calculation_id
    print("Calculation ID:", calculation_id)

    # Check to see if a calculation is still running
    quit_after = 5
    calculation_status = "running"
    count = 0
    while calculation_status != "successful" and count < quit_after:
        response = get_calculation_by_id.sync(id=calculation_id, client=client)
        if isinstance(response, QCrBoxResponseCalculationsResponse):
            print(f"Calculation {calculation_id} status is {response.payload.calculations[0].status}")
            calculation_status = response.payload.calculations[0].status
        time.sleep(2)
        count += 1

    # If the command is still running, we can terminate it
    response = get_calculation_by_id.sync(id=calculation_id, client=client)
    if not isinstance(response, QCrBoxResponseCalculationsResponse):
        print("Failed to get calculation response")
    else:
        print("Calculation status:", response.payload.calculations[0])
        if response.payload.calculations[0].status == "running":
            print("Calculation is still running, so stopping it forcefully with stop_running_calculations")
            response = stop_running_calculation.sync(id=calculation_id, client=client)
            if isinstance(response, QCrBoxErrorResponse) or response is None:
                raise TypeError("Failed to stop running calculation:", response)
            else:
                print("Stopped running calculation:", response)
finally:
    # Delete the dataset afterward, because we are just using this for test purposes
    response = delete_dataset_by_id.sync(id=dataset1, client=client)
    response = delete_dataset_by_id.sync(id=dataset2, client=client)
