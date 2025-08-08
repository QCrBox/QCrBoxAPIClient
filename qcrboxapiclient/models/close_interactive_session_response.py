from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloseInteractiveSessionResponse")


@_attrs_define
class CloseInteractiveSessionResponse:
    """
    Attributes:
        session_id (str):
        status (str):
        output_dataset_id (Union[None, Unset, str]):
        error_msg (Union[None, Unset, str]):
    """

    session_id: str
    status: str
    output_dataset_id: Union[None, Unset, str] = UNSET
    error_msg: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        status = self.status

        output_dataset_id: Union[None, Unset, str]
        if isinstance(self.output_dataset_id, Unset):
            output_dataset_id = UNSET
        else:
            output_dataset_id = self.output_dataset_id

        error_msg: Union[None, Unset, str]
        if isinstance(self.error_msg, Unset):
            error_msg = UNSET
        else:
            error_msg = self.error_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "status": status,
            }
        )
        if output_dataset_id is not UNSET:
            field_dict["output_dataset_id"] = output_dataset_id
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        status = d.pop("status")

        def _parse_output_dataset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output_dataset_id = _parse_output_dataset_id(d.pop("output_dataset_id", UNSET))

        def _parse_error_msg(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_msg = _parse_error_msg(d.pop("error_msg", UNSET))

        close_interactive_session_response = cls(
            session_id=session_id,
            status=status,
            output_dataset_id=output_dataset_id,
            error_msg=error_msg,
        )

        close_interactive_session_response.additional_properties = d
        return close_interactive_session_response

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
