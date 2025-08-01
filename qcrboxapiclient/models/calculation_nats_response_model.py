from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calculation_nats_response_model_arguments import CalculationNatsResponseModelArguments


T = TypeVar("T", bound="CalculationNatsResponseModel")


@_attrs_define
class CalculationNatsResponseModel:
    """
    Attributes:
        calculation_id (str):
        application_slug (str):
        application_version (str):
        command_name (str):
        arguments (CalculationNatsResponseModelArguments):
        status (str):
        output_dataset_id (Union[None, Unset, str]):
    """

    calculation_id: str
    application_slug: str
    application_version: str
    command_name: str
    arguments: "CalculationNatsResponseModelArguments"
    status: str
    output_dataset_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculation_id = self.calculation_id

        application_slug = self.application_slug

        application_version = self.application_version

        command_name = self.command_name

        arguments = self.arguments.to_dict()

        status = self.status

        output_dataset_id: Union[None, Unset, str]
        if isinstance(self.output_dataset_id, Unset):
            output_dataset_id = UNSET
        else:
            output_dataset_id = self.output_dataset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculation_id": calculation_id,
                "application_slug": application_slug,
                "application_version": application_version,
                "command_name": command_name,
                "arguments": arguments,
                "status": status,
            }
        )
        if output_dataset_id is not UNSET:
            field_dict["output_dataset_id"] = output_dataset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calculation_nats_response_model_arguments import CalculationNatsResponseModelArguments

        d = dict(src_dict)
        calculation_id = d.pop("calculation_id")

        application_slug = d.pop("application_slug")

        application_version = d.pop("application_version")

        command_name = d.pop("command_name")

        arguments = CalculationNatsResponseModelArguments.from_dict(d.pop("arguments"))

        status = d.pop("status")

        def _parse_output_dataset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output_dataset_id = _parse_output_dataset_id(d.pop("output_dataset_id", UNSET))

        calculation_nats_response_model = cls(
            calculation_id=calculation_id,
            application_slug=application_slug,
            application_version=application_version,
            command_name=command_name,
            arguments=arguments,
            status=status,
            output_dataset_id=output_dataset_id,
        )

        calculation_nats_response_model.additional_properties = d
        return calculation_nats_response_model

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
