from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.command_spec_with_parameters_implemented_as import CommandSpecWithParametersImplementedAs
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_spec_with_parameters_parameters import CommandSpecWithParametersParameters


T = TypeVar("T", bound="CommandSpecWithParameters")


@_attrs_define
class CommandSpecWithParameters:
    """
    Attributes:
        name (str):
        implemented_as (CommandSpecWithParametersImplementedAs):
        parameters (CommandSpecWithParametersParameters):
        id (int):
        application_id (int):
        application (str):
        version (str):
        cmd_name (str):
        description (Union[Unset, str]):  Default: ''.
        merge_cif_su (Union[Unset, bool]):  Default: False.
        doi (Union[None, Unset, str]):
    """

    name: str
    implemented_as: CommandSpecWithParametersImplementedAs
    parameters: "CommandSpecWithParametersParameters"
    id: int
    application_id: int
    application: str
    version: str
    cmd_name: str
    description: Union[Unset, str] = ""
    merge_cif_su: Union[Unset, bool] = False
    doi: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        implemented_as = self.implemented_as.value

        parameters = self.parameters.to_dict()

        id = self.id

        application_id = self.application_id

        application = self.application

        version = self.version

        cmd_name = self.cmd_name

        description = self.description

        merge_cif_su = self.merge_cif_su

        doi: Union[None, Unset, str]
        if isinstance(self.doi, Unset):
            doi = UNSET
        else:
            doi = self.doi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "implemented_as": implemented_as,
                "parameters": parameters,
                "id": id,
                "application_id": application_id,
                "application": application,
                "version": version,
                "cmd_name": cmd_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if merge_cif_su is not UNSET:
            field_dict["merge_cif_su"] = merge_cif_su
        if doi is not UNSET:
            field_dict["doi"] = doi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_spec_with_parameters_parameters import CommandSpecWithParametersParameters

        d = dict(src_dict)
        name = d.pop("name")

        implemented_as = CommandSpecWithParametersImplementedAs(d.pop("implemented_as"))

        parameters = CommandSpecWithParametersParameters.from_dict(d.pop("parameters"))

        id = d.pop("id")

        application_id = d.pop("application_id")

        application = d.pop("application")

        version = d.pop("version")

        cmd_name = d.pop("cmd_name")

        description = d.pop("description", UNSET)

        merge_cif_su = d.pop("merge_cif_su", UNSET)

        def _parse_doi(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doi = _parse_doi(d.pop("doi", UNSET))

        command_spec_with_parameters = cls(
            name=name,
            implemented_as=implemented_as,
            parameters=parameters,
            id=id,
            application_id=application_id,
            application=application,
            version=version,
            cmd_name=cmd_name,
            description=description,
            merge_cif_su=merge_cif_su,
            doi=doi,
        )

        command_spec_with_parameters.additional_properties = d
        return command_spec_with_parameters

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
