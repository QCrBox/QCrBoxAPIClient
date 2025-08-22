from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataFileResponse")


@_attrs_define
class DataFileResponse:
    """
    Attributes:
        qcrbox_file_id (str):
        filename (str):
        filetype (str):
        qcrbox_dataset_id (Union[None, Unset, str]):
    """

    qcrbox_file_id: str
    filename: str
    filetype: str
    qcrbox_dataset_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qcrbox_file_id = self.qcrbox_file_id

        filename = self.filename

        filetype = self.filetype

        qcrbox_dataset_id: Union[None, Unset, str]
        if isinstance(self.qcrbox_dataset_id, Unset):
            qcrbox_dataset_id = UNSET
        else:
            qcrbox_dataset_id = self.qcrbox_dataset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "qcrbox_file_id": qcrbox_file_id,
                "filename": filename,
                "filetype": filetype,
            }
        )
        if qcrbox_dataset_id is not UNSET:
            field_dict["qcrbox_dataset_id"] = qcrbox_dataset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qcrbox_file_id = d.pop("qcrbox_file_id")

        filename = d.pop("filename")

        filetype = d.pop("filetype")

        def _parse_qcrbox_dataset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        qcrbox_dataset_id = _parse_qcrbox_dataset_id(d.pop("qcrbox_dataset_id", UNSET))

        data_file_response = cls(
            qcrbox_file_id=qcrbox_file_id,
            filename=filename,
            filetype=filetype,
            qcrbox_dataset_id=qcrbox_dataset_id,
        )

        data_file_response.additional_properties = d
        return data_file_response

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
