from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.interactive_session_create_arguments import InteractiveSessionCreateArguments


T = TypeVar("T", bound="InteractiveSessionCreate")


@_attrs_define
class InteractiveSessionCreate:
    """
    Attributes:
        application_slug (str):
        application_version (str):
        arguments (InteractiveSessionCreateArguments):
    """

    application_slug: str
    application_version: str
    arguments: "InteractiveSessionCreateArguments"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_slug = self.application_slug

        application_version = self.application_version

        arguments = self.arguments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application_slug": application_slug,
                "application_version": application_version,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interactive_session_create_arguments import InteractiveSessionCreateArguments

        d = dict(src_dict)
        application_slug = d.pop("application_slug")

        application_version = d.pop("application_version")

        arguments = InteractiveSessionCreateArguments.from_dict(d.pop("arguments"))

        interactive_session_create = cls(
            application_slug=application_slug,
            application_version=application_version,
            arguments=arguments,
        )

        interactive_session_create.additional_properties = d
        return interactive_session_create

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
