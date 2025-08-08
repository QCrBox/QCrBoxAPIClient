#!/bin/bash

openapi-python-client generate \
	--url http://127.0.0.1:11000/api/schema \
	--config config.yaml \
	--output-path . \
	--custom-template-path=./templates \
	--overwrite
