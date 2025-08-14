from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_file_info_response import DataFileInfoResponse


T = TypeVar("T", bound="DatasetInfoResponseDataFiles")


@_attrs_define
class DatasetInfoResponseDataFiles:
    """ """

    additional_properties: dict[str, "DataFileInfoResponse"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_file_info_response import DataFileInfoResponse

        d = dict(src_dict)
        dataset_info_response_data_files = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DataFileInfoResponse.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        dataset_info_response_data_files.additional_properties = additional_properties
        return dataset_info_response_data_files

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DataFileInfoResponse":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DataFileInfoResponse") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
