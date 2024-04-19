from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="JointOperation")


@_attrs_define
class JointOperation:
    """Represents a joint operation.

    Attributes:
        id (Union[Unset, int]):
        planet_index (Union[Unset, int]):
        hq_node_index (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    planet_index: Union[Unset, int] = UNSET
    hq_node_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        planet_index = self.planet_index

        hq_node_index = self.hq_node_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if planet_index is not UNSET:
            field_dict["planetIndex"] = planet_index
        if hq_node_index is not UNSET:
            field_dict["hqNodeIndex"] = hq_node_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        planet_index = d.pop("planetIndex", UNSET)

        hq_node_index = d.pop("hqNodeIndex", UNSET)

        joint_operation = cls(
            id=id,
            planet_index=planet_index,
            hq_node_index=hq_node_index,
        )

        return joint_operation
