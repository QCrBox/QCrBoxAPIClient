from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_response_data_files import DatasetResponseDataFiles


T = TypeVar("T", bound="DatasetResponse")


@_attrs_define
class DatasetResponse:
    """
    Attributes:
        qcrbox_dataset_id (str):
        data_files (DatasetResponseDataFiles):
    """

    qcrbox_dataset_id: str
    data_files: "DatasetResponseDataFiles"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qcrbox_dataset_id = self.qcrbox_dataset_id

        data_files = self.data_files.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "qcrbox_dataset_id": qcrbox_dataset_id,
                "data_files": data_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_response_data_files import DatasetResponseDataFiles

        d = dict(src_dict)
        qcrbox_dataset_id = d.pop("qcrbox_dataset_id")

        data_files = DatasetResponseDataFiles.from_dict(d.pop("data_files"))

        dataset_response = cls(
            qcrbox_dataset_id=qcrbox_dataset_id,
            data_files=data_files,
        )

        dataset_response.additional_properties = d
        return dataset_response

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
