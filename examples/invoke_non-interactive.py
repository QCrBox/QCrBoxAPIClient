"""Invoking an interactive olex2 session.

This is an example script of creating a dataset and passing the data file within
the dataset to the API to invoke an Olex2 session accessible at:

    http://127.0.0.1:12004/vnc.html?path=vnc&autoconnect=true&resize=remote&reconnect=true&show_dot=true

NB: you will need to remove the calls to `close_interactive_session` and
`delete_dataset_by_id` to actually interact with the interactive session.
"""

import io
import pathlib

from qcrboxapiclient.api.commands import invoke_command
from qcrboxapiclient.api.datasets import create_dataset, delete_dataset_by_id
from qcrboxapiclient.client import Client
from qcrboxapiclient.models import CreateDatasetBody, InvokeCommand, InvokeCommandArguments, QCrBoxErrorResponse
from qcrboxapiclient.types import File

# Create a synchronous client, which is passed to each `sync()` for an API endpoint
# via keyword
client = Client(base_url="http://127.0.0.1:11000")

# Example file in QCrBox repository, but could substitite with `work.cif` which
# 100% works w/ Olex2 and Crystal Explorer
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
if isinstance(response, QCrBoxErrorResponse):
    raise TypeError("Failed to upload file", response)
else:
    print("Created dataset:", response)

# The response returns the created object in payload.datasets[0]. Note that this
# doesn't contain any of the file's binary data and instead contains metadata
# about the dataset and data files in the data set.
dataset_id = response.payload.datasets[0].qcrbox_dataset_id
data_file_id = response.payload.datasets[0].data_files[test_file.name].qcrbox_file_id

# To create an interactive olex2 session we call the create_interactive_session_with_arguments
# endpoint with a payload of application we want to start and arguments for the olex2
# command. For olex2, we need an argument named "input_file" which contains a data_file_id.
# Note that the arguments is a dict and we use `CreateInteractiveSessionArguments` to
# marshal out input into Json for the API
arguments = InvokeCommandArguments.from_dict(
    {"input_cif": {"data_file_id": data_file_id}, "output_cif_path": "/opt/qcrbox/test_unified_cif.cif"}
)
create_session = InvokeCommand("qcrboxtools", "0.0.5", "to_unified_cif", arguments)
response = invoke_command.sync(client=client, body=create_session)
if isinstance(response, QCrBoxErrorResponse):
    raise TypeError("Failed to invoke command", response)
else:
    print("Invoked command session:", response)

# The response from this endpoint is slightly different as it returns a reference
# to the create object, rather than the object iself. The payload contains the
# interactive_session_id which is also the calcualtion id of the interactive session
calculation_id = response.payload.calculation_id
print("Calculation ID:", calculation_id)

# Delete the dataset afterward, because we are just using this for test purposes
response = delete_dataset_by_id.sync(id=dataset_id, client=client)
if isinstance(response, QCrBoxErrorResponse):
    raise TypeError("Failed to delete test dataset")
else:
    print("Deleted test dataset")
