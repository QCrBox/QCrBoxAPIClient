from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.invoke_command_parameters_arguments import InvokeCommandParametersArguments


T = TypeVar("T", bound="InvokeCommandParameters")


@_attrs_define
class InvokeCommandParameters:
    """
    Attributes:
        application_slug (str):
        application_version (str):
        command_name (str):
        arguments (InvokeCommandParametersArguments):
    """

    application_slug: str
    application_version: str
    command_name: str
    arguments: "InvokeCommandParametersArguments"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_slug = self.application_slug

        application_version = self.application_version

        command_name = self.command_name

        arguments = self.arguments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application_slug": application_slug,
                "application_version": application_version,
                "command_name": command_name,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoke_command_parameters_arguments import InvokeCommandParametersArguments

        d = dict(src_dict)
        application_slug = d.pop("application_slug")

        application_version = d.pop("application_version")

        command_name = d.pop("command_name")

        arguments = InvokeCommandParametersArguments.from_dict(d.pop("arguments"))

        invoke_command_parameters = cls(
            application_slug=application_slug,
            application_version=application_version,
            command_name=command_name,
            arguments=arguments,
        )

        invoke_command_parameters.additional_properties = d
        return invoke_command_parameters

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
