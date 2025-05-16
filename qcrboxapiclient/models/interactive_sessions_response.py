from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.interactive_session_info_response import InteractiveSessionInfoResponse


T = TypeVar("T", bound="InteractiveSessionsResponse")


@_attrs_define
class InteractiveSessionsResponse:
    """
    Attributes:
        interactive_sessions (list['InteractiveSessionInfoResponse']):
    """

    interactive_sessions: list["InteractiveSessionInfoResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interactive_sessions = []
        for interactive_sessions_item_data in self.interactive_sessions:
            interactive_sessions_item = interactive_sessions_item_data.to_dict()
            interactive_sessions.append(interactive_sessions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interactive_sessions": interactive_sessions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interactive_session_info_response import InteractiveSessionInfoResponse

        d = dict(src_dict)
        interactive_sessions = []
        _interactive_sessions = d.pop("interactive_sessions")
        for interactive_sessions_item_data in _interactive_sessions:
            interactive_sessions_item = InteractiveSessionInfoResponse.from_dict(interactive_sessions_item_data)

            interactive_sessions.append(interactive_sessions_item)

        interactive_sessions_response = cls(
            interactive_sessions=interactive_sessions,
        )

        interactive_sessions_response.additional_properties = d
        return interactive_sessions_response

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
