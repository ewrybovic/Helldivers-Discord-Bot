from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.planet_coordinates import PlanetCoordinates


T = TypeVar("T", bound="PlanetInfo")


@_attrs_define
class PlanetInfo:
    """Represents information of a planet from the 'WarInfo' endpoint returned by ArrowHead's API.

    Attributes:
        index (Union[Unset, int]): The numerical identifier for this planet, used as reference by other properties
            throughout the API (like Waypoints).
        settings_hash (Union[Unset, int]): Purpose unknown at this time.
        position (Union[Unset, PlanetCoordinates]): Represents a set of coordinates returned by ArrowHead's API.
        waypoints (Union[Unset, List[int]]): A list of links to other planets (supply lines).
        sector (Union[Unset, int]): The identifier of the sector this planet is located in.
        max_health (Union[Unset, int]): The 'health' of this planet, indicates how much liberation it needs to switch
            sides.
        disabled (Union[Unset, bool]): Whether this planet is currently considered active in the galactic war.
        initial_owner (Union[Unset, int]): The identifier of the faction that initially owned this planet.
    """

    index: Union[Unset, int] = UNSET
    settings_hash: Union[Unset, int] = UNSET
    position: Union[Unset, "PlanetCoordinates"] = UNSET
    waypoints: Union[Unset, List[int]] = UNSET
    sector: Union[Unset, int] = UNSET
    max_health: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    initial_owner: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        settings_hash = self.settings_hash

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        waypoints: Union[Unset, List[int]] = UNSET
        if not isinstance(self.waypoints, Unset):
            waypoints = self.waypoints

        sector = self.sector

        max_health = self.max_health

        disabled = self.disabled

        initial_owner = self.initial_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if settings_hash is not UNSET:
            field_dict["settingsHash"] = settings_hash
        if position is not UNSET:
            field_dict["position"] = position
        if waypoints is not UNSET:
            field_dict["waypoints"] = waypoints
        if sector is not UNSET:
            field_dict["sector"] = sector
        if max_health is not UNSET:
            field_dict["maxHealth"] = max_health
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if initial_owner is not UNSET:
            field_dict["initialOwner"] = initial_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.planet_coordinates import PlanetCoordinates

        d = src_dict.copy()
        index = d.pop("index", UNSET)

        settings_hash = d.pop("settingsHash", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, PlanetCoordinates]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = PlanetCoordinates.from_dict(_position)

        waypoints = cast(List[int], d.pop("waypoints", UNSET))

        sector = d.pop("sector", UNSET)

        max_health = d.pop("maxHealth", UNSET)

        disabled = d.pop("disabled", UNSET)

        initial_owner = d.pop("initialOwner", UNSET)

        planet_info = cls(
            index=index,
            settings_hash=settings_hash,
            position=position,
            waypoints=waypoints,
            sector=sector,
            max_health=max_health,
            disabled=disabled,
            initial_owner=initial_owner,
        )

        return planet_info
