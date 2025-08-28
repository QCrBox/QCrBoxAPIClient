from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_file_response import DataFileResponse
    from ..models.dataset_response import DatasetResponse


T = TypeVar("T", bound="DatasetsWithDataFilesResponse")


@_attrs_define
class DatasetsWithDataFilesResponse:
    """
    Attributes:
        datasets (list['DatasetResponse']):
        data_files (list['DataFileResponse']):
    """

    datasets: list["DatasetResponse"]
    data_files: list["DataFileResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasets = []
        for datasets_item_data in self.datasets:
            datasets_item = datasets_item_data.to_dict()
            datasets.append(datasets_item)

        data_files = []
        for data_files_item_data in self.data_files:
            data_files_item = data_files_item_data.to_dict()
            data_files.append(data_files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasets": datasets,
                "data_files": data_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_file_response import DataFileResponse
        from ..models.dataset_response import DatasetResponse

        d = dict(src_dict)
        datasets = []
        _datasets = d.pop("datasets")
        for datasets_item_data in _datasets:
            datasets_item = DatasetResponse.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        data_files = []
        _data_files = d.pop("data_files")
        for data_files_item_data in _data_files:
            data_files_item = DataFileResponse.from_dict(data_files_item_data)

            data_files.append(data_files_item)

        datasets_with_data_files_response = cls(
            datasets=datasets,
            data_files=data_files,
        )

        datasets_with_data_files_response.additional_properties = d
        return datasets_with_data_files_response

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
