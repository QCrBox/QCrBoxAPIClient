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
    InvokeCommandParametersArguments,
    QCrBoxErrorResponse,
    QCrBoxResponseCalculationsResponse,
    QCrBoxResponseStoppedCalculationResponse,
)
from qcrboxapiclient.types import File

# Create a synchronous client, which is passed to each `sync()` for an API endpoint
# via keyword
client = Client(base_url="http://127.0.0.1:11000")

# Example file in QCrBox repository, but could substitite with `work.cif`
test_file = pathlib.Path("../robot_tests/test_data/api_client_test_cif.cif").resolve()

# To upload the file to the registry, we need to create a dataset and attach the
# file to it. Files are sent via the API as binary in a CreateDatasetBody payload
with test_file.open("rb") as f:
    file = File(io.BytesIO(f.read()), test_file.name)
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
data_file_id = response.payload.datasets[0].data_files[test_file.name].qcrbox_file_id

# To invoke a non-interactive command, we need to create objects which represent
# the JSON data sent in the request to the API
arguments = InvokeCommandParametersArguments.from_dict(
    {"input_cif": {"data_file_id": data_file_id}, "output_cif_path": "/opt/qcrbox/test_unified_cif.cif"}
)
create_session = InvokeCommandParameters("qcrboxtools", "0.0.5", "to_unified_cif", arguments)

# Send the request to the API
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
    if response.payload.calculations[0].status == "running":
        print("Calculation is still running, so stopping it forcefully with stop_running_calculations")
        response = stop_running_calculation.sync(id=calculation_id, client=client)
        if isinstance(response, QCrBoxErrorResponse) or response is None:
            raise TypeError("Failed to stop running calculation:", response)
        else:
            print("Stopped running calculation:", response)

# Delete the dataset afterward, because we are just using this for test purposes
response = delete_dataset_by_id.sync(id=dataset_id, client=client)
if isinstance(response, QCrBoxErrorResponse):
    raise TypeError("Failed to delete test dataset")
else:
    print("Deleted test dataset")
