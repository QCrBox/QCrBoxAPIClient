import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_spec_with_parameters_response import CommandSpecWithParametersResponse


T = TypeVar("T", bound="ApplicationSpecWithCommandsResponse")


@_attrs_define
class ApplicationSpecWithCommandsResponse:
    """
    Attributes:
        name (str):
        slug (str):
        version (str):
        id (int):
        registered_at (datetime.datetime):
        commands (list['CommandSpecWithParametersResponse']):
        pyqcrbox_version (Union[Unset, str]):  Default: '2026.dev173+g9330da815.d19800101'.
        description (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        doi (Union[None, Unset, str]):
        yaml_file_path (Union[None, Unset, str]):
        gui_port (Union[None, Unset, str]):
    """

    name: str
    slug: str
    version: str
    id: int
    registered_at: datetime.datetime
    commands: list["CommandSpecWithParametersResponse"]
    pyqcrbox_version: Union[Unset, str] = "2026.dev173+g9330da815.d19800101"
    description: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    doi: Union[None, Unset, str] = UNSET
    yaml_file_path: Union[None, Unset, str] = UNSET
    gui_port: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        version = self.version

        id = self.id

        registered_at = self.registered_at.isoformat()

        commands = []
        for commands_item_data in self.commands:
            commands_item = commands_item_data.to_dict()
            commands.append(commands_item)

        pyqcrbox_version = self.pyqcrbox_version

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        doi: Union[None, Unset, str]
        if isinstance(self.doi, Unset):
            doi = UNSET
        else:
            doi = self.doi

        yaml_file_path: Union[None, Unset, str]
        if isinstance(self.yaml_file_path, Unset):
            yaml_file_path = UNSET
        else:
            yaml_file_path = self.yaml_file_path

        gui_port: Union[None, Unset, str]
        if isinstance(self.gui_port, Unset):
            gui_port = UNSET
        else:
            gui_port = self.gui_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "version": version,
                "id": id,
                "registered_at": registered_at,
                "commands": commands,
            }
        )
        if pyqcrbox_version is not UNSET:
            field_dict["pyqcrbox_version"] = pyqcrbox_version
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if email is not UNSET:
            field_dict["email"] = email
        if doi is not UNSET:
            field_dict["doi"] = doi
        if yaml_file_path is not UNSET:
            field_dict["yaml_file_path"] = yaml_file_path
        if gui_port is not UNSET:
            field_dict["gui_port"] = gui_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_spec_with_parameters_response import CommandSpecWithParametersResponse

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        version = d.pop("version")

        id = d.pop("id")

        registered_at = isoparse(d.pop("registered_at"))

        commands = []
        _commands = d.pop("commands")
        for commands_item_data in _commands:
            commands_item = CommandSpecWithParametersResponse.from_dict(commands_item_data)

            commands.append(commands_item)

        pyqcrbox_version = d.pop("pyqcrbox_version", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_doi(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doi = _parse_doi(d.pop("doi", UNSET))

        def _parse_yaml_file_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        yaml_file_path = _parse_yaml_file_path(d.pop("yaml_file_path", UNSET))

        def _parse_gui_port(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gui_port = _parse_gui_port(d.pop("gui_port", UNSET))

        application_spec_with_commands_response = cls(
            name=name,
            slug=slug,
            version=version,
            id=id,
            registered_at=registered_at,
            commands=commands,
            pyqcrbox_version=pyqcrbox_version,
            description=description,
            url=url,
            email=email,
            doi=doi,
            yaml_file_path=yaml_file_path,
            gui_port=gui_port,
        )

        application_spec_with_commands_response.additional_properties = d
        return application_spec_with_commands_response

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
