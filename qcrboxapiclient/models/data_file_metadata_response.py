from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataFileMetadataResponse")


@_attrs_define
class DataFileMetadataResponse:
    """
    Attributes:
        qcrbox_file_id (str):
        filename (str):
        filetype (str):
    """

    qcrbox_file_id: str
    filename: str
    filetype: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qcrbox_file_id = self.qcrbox_file_id

        filename = self.filename

        filetype = self.filetype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "qcrbox_file_id": qcrbox_file_id,
                "filename": filename,
                "filetype": filetype,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qcrbox_file_id = d.pop("qcrbox_file_id")

        filename = d.pop("filename")

        filetype = d.pop("filetype")

        data_file_metadata_response = cls(
            qcrbox_file_id=qcrbox_file_id,
            filename=filename,
            filetype=filetype,
        )

        data_file_metadata_response.additional_properties = d
        return data_file_metadata_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
