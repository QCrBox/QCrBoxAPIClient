from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calculation_status_details_status import CalculationStatusDetailsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calculation_status_details_extra_info import CalculationStatusDetailsExtraInfo


T = TypeVar("T", bound="CalculationStatusDetails")


@_attrs_define
class CalculationStatusDetails:
    """
    Attributes:
        calculation_id (str):
        status (CalculationStatusDetailsStatus):
        stdout (Union[None, Unset, str]):  Default: ''.
        stderr (Union[None, Unset, str]):  Default: ''.
        output_dataset_id (Union[None, Unset, str]):
        extra_info (Union[Unset, CalculationStatusDetailsExtraInfo]):
        timestamp (Union[None, Unset, str]):
    """

    calculation_id: str
    status: CalculationStatusDetailsStatus
    stdout: Union[None, Unset, str] = ""
    stderr: Union[None, Unset, str] = ""
    output_dataset_id: Union[None, Unset, str] = UNSET
    extra_info: Union[Unset, "CalculationStatusDetailsExtraInfo"] = UNSET
    timestamp: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculation_id = self.calculation_id

        status = self.status.value

        stdout: Union[None, Unset, str]
        if isinstance(self.stdout, Unset):
            stdout = UNSET
        else:
            stdout = self.stdout

        stderr: Union[None, Unset, str]
        if isinstance(self.stderr, Unset):
            stderr = UNSET
        else:
            stderr = self.stderr

        output_dataset_id: Union[None, Unset, str]
        if isinstance(self.output_dataset_id, Unset):
            output_dataset_id = UNSET
        else:
            output_dataset_id = self.output_dataset_id

        extra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extra_info, Unset):
            extra_info = self.extra_info.to_dict()

        timestamp: Union[None, Unset, str]
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculation_id": calculation_id,
                "status": status,
            }
        )
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if output_dataset_id is not UNSET:
            field_dict["output_dataset_id"] = output_dataset_id
        if extra_info is not UNSET:
            field_dict["extra_info"] = extra_info
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calculation_status_details_extra_info import CalculationStatusDetailsExtraInfo

        d = dict(src_dict)
        calculation_id = d.pop("calculation_id")

        status = CalculationStatusDetailsStatus(d.pop("status"))

        def _parse_stdout(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stdout = _parse_stdout(d.pop("stdout", UNSET))

        def _parse_stderr(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stderr = _parse_stderr(d.pop("stderr", UNSET))

        def _parse_output_dataset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output_dataset_id = _parse_output_dataset_id(d.pop("output_dataset_id", UNSET))

        _extra_info = d.pop("extra_info", UNSET)
        extra_info: Union[Unset, CalculationStatusDetailsExtraInfo]
        if isinstance(_extra_info, Unset):
            extra_info = UNSET
        else:
            extra_info = CalculationStatusDetailsExtraInfo.from_dict(_extra_info)

        def _parse_timestamp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        calculation_status_details = cls(
            calculation_id=calculation_id,
            status=status,
            stdout=stdout,
            stderr=stderr,
            output_dataset_id=output_dataset_id,
            extra_info=extra_info,
            timestamp=timestamp,
        )

        calculation_status_details.additional_properties = d
        return calculation_status_details

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
