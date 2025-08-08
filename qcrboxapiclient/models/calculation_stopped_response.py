from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stopped_calculation_response import StoppedCalculationResponse


T = TypeVar("T", bound="CalculationStoppedResponse")


@_attrs_define
class CalculationStoppedResponse:
    """
    Attributes:
        calculations (list['StoppedCalculationResponse']):
    """

    calculations: list["StoppedCalculationResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculations = []
        for calculations_item_data in self.calculations:
            calculations_item = calculations_item_data.to_dict()
            calculations.append(calculations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculations": calculations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stopped_calculation_response import StoppedCalculationResponse

        d = dict(src_dict)
        calculations = []
        _calculations = d.pop("calculations")
        for calculations_item_data in _calculations:
            calculations_item = StoppedCalculationResponse.from_dict(calculations_item_data)

            calculations.append(calculations_item)

        calculation_stopped_response = cls(
            calculations=calculations,
        )

        calculation_stopped_response.additional_properties = d
        return calculation_stopped_response

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
