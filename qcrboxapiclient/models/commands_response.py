from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.command_spec_with_parameters import CommandSpecWithParameters


T = TypeVar("T", bound="CommandsResponse")


@_attrs_define
class CommandsResponse:
    """
    Attributes:
        commands (list['CommandSpecWithParameters']):
    """

    commands: list["CommandSpecWithParameters"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commands = []
        for commands_item_data in self.commands:
            commands_item = commands_item_data.to_dict()
            commands.append(commands_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commands": commands,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_spec_with_parameters import CommandSpecWithParameters

        d = dict(src_dict)
        commands = []
        _commands = d.pop("commands")
        for commands_item_data in _commands:
            commands_item = CommandSpecWithParameters.from_dict(commands_item_data)

            commands.append(commands_item)

        commands_response = cls(
            commands=commands,
        )

        commands_response.additional_properties = d
        return commands_response

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
