from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interactive_session_info_response_arguments import InteractiveSessionInfoResponseArguments


T = TypeVar("T", bound="InteractiveSessionInfoResponse")


@_attrs_define
class InteractiveSessionInfoResponse:
    """
    Attributes:
        session_id (str):
        client_private_inbox (str):
        command_name (str):
        arguments (InteractiveSessionInfoResponseArguments):
        application_slug (Union[None, Unset, str]):
        application_version (Union[None, Unset, str]):
    """

    session_id: str
    client_private_inbox: str
    command_name: str
    arguments: "InteractiveSessionInfoResponseArguments"
    application_slug: Union[None, Unset, str] = UNSET
    application_version: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        client_private_inbox = self.client_private_inbox

        command_name = self.command_name

        arguments = self.arguments.to_dict()

        application_slug: Union[None, Unset, str]
        if isinstance(self.application_slug, Unset):
            application_slug = UNSET
        else:
            application_slug = self.application_slug

        application_version: Union[None, Unset, str]
        if isinstance(self.application_version, Unset):
            application_version = UNSET
        else:
            application_version = self.application_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "client_private_inbox": client_private_inbox,
                "command_name": command_name,
                "arguments": arguments,
            }
        )
        if application_slug is not UNSET:
            field_dict["application_slug"] = application_slug
        if application_version is not UNSET:
            field_dict["application_version"] = application_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interactive_session_info_response_arguments import InteractiveSessionInfoResponseArguments

        d = dict(src_dict)
        session_id = d.pop("session_id")

        client_private_inbox = d.pop("client_private_inbox")

        command_name = d.pop("command_name")

        arguments = InteractiveSessionInfoResponseArguments.from_dict(d.pop("arguments"))

        def _parse_application_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        application_slug = _parse_application_slug(d.pop("application_slug", UNSET))

        def _parse_application_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        application_version = _parse_application_version(d.pop("application_version", UNSET))

        interactive_session_info_response = cls(
            session_id=session_id,
            client_private_inbox=client_private_inbox,
            command_name=command_name,
            arguments=arguments,
            application_slug=application_slug,
            application_version=application_version,
        )

        interactive_session_info_response.additional_properties = d
        return interactive_session_info_response

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
