from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.invoke_command_response import InvokeCommandResponse


T = TypeVar("T", bound="QCrBoxResponseInvokeCommandResponse")


@_attrs_define
class QCrBoxResponseInvokeCommandResponse:
    """
    Attributes:
        status (str):
        message (str):
        timestamp (str):
        payload (InvokeCommandResponse):
    """

    status: str
    message: str
    timestamp: str
    payload: "InvokeCommandResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message = self.message

        timestamp = self.timestamp

        payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "message": message,
                "timestamp": timestamp,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoke_command_response import InvokeCommandResponse

        d = dict(src_dict)
        status = d.pop("status")

        message = d.pop("message")

        timestamp = d.pop("timestamp")

        payload = InvokeCommandResponse.from_dict(d.pop("payload"))

        q_cr_box_response_invoke_command_response = cls(
            status=status,
            message=message,
            timestamp=timestamp,
            payload=payload,
        )

        q_cr_box_response_invoke_command_response.additional_properties = d
        return q_cr_box_response_invoke_command_response

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
