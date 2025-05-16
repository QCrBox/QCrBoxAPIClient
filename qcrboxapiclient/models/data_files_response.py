from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_file_metadata_response import DataFileMetadataResponse


T = TypeVar("T", bound="DataFilesResponse")


@_attrs_define
class DataFilesResponse:
    """
    Attributes:
        data_files (list['DataFileMetadataResponse']):
    """

    data_files: list["DataFileMetadataResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_files = []
        for data_files_item_data in self.data_files:
            data_files_item = data_files_item_data.to_dict()
            data_files.append(data_files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_files": data_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_file_metadata_response import DataFileMetadataResponse

        d = dict(src_dict)
        data_files = []
        _data_files = d.pop("data_files")
        for data_files_item_data in _data_files:
            data_files_item = DataFileMetadataResponse.from_dict(data_files_item_data)

            data_files.append(data_files_item)

        data_files_response = cls(
            data_files=data_files,
        )

        data_files_response.additional_properties = d
        return data_files_response

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
