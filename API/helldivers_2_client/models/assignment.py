from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setting import Setting


T = TypeVar("T", bound="Assignment")


@_attrs_define
class Assignment:
    """Represents an assignment given from Super Earth to the Helldivers.

    Attributes:
        id32 (Union[Unset, int]): Internal identifier of this assignment.
        progress (Union[Unset, List[int]]): A list of numbers, how they represent progress is unknown.
        expires_in (Union[Unset, int]): The amount of seconds until this assignment expires.
        setting (Union[Unset, Setting]): Contains the details of an Assignment like reward and requirements.
    """

    id32: Union[Unset, int] = UNSET
    progress: Union[Unset, List[int]] = UNSET
    expires_in: Union[Unset, int] = UNSET
    setting: Union[Unset, "Setting"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id32 = self.id32

        progress: Union[Unset, List[int]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress

        expires_in = self.expires_in

        setting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.setting, Unset):
            setting = self.setting.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id32 is not UNSET:
            field_dict["id32"] = id32
        if progress is not UNSET:
            field_dict["progress"] = progress
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if setting is not UNSET:
            field_dict["setting"] = setting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.setting import Setting

        d = src_dict.copy()
        id32 = d.pop("id32", UNSET)

        progress = cast(List[int], d.pop("progress", UNSET))

        expires_in = d.pop("expiresIn", UNSET)

        _setting = d.pop("setting", UNSET)
        setting: Union[Unset, Setting]
        if isinstance(_setting, Unset):
            setting = UNSET
        else:
            setting = Setting.from_dict(_setting)

        assignment = cls(
            id32=id32,
            progress=progress,
            expires_in=expires_in,
            setting=setting,
        )

        return assignment
