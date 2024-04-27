from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.biome import Biome
    from ..models.event import Event
    from ..models.hazard import Hazard
    from ..models.position import Position
    from ..models.statistics import Statistics


T = TypeVar("T", bound="Planet")


@_attrs_define
class Planet:
    """Contains all aggregated information AH has about a planet.

    Attributes:
        index (Union[Unset, int]): The unique identifier ArrowHead assigned to this planet.
        name (Union[Unset, str]): The name of the planet, as shown in game.
        sector (Union[Unset, str]): The name of the sector the planet is in, as shown in game.
        biome (Union[Unset, Biome]): Represents information about a biome of a planet.
        hazards (Union[Unset, List['Hazard']]): All Hazards that are applicable to this planet.
        hash_ (Union[Unset, int]): A hash assigned to the planet by ArrowHead, purpose unknown.
        position (Union[Unset, Position]): Represents a position on the galactic war map.
        waypoints (Union[Unset, List[int]]): A list of Index of all the planets to which this planet is connected.
        max_health (Union[Unset, int]): The maximum health pool of this planet.
        health (Union[Unset, int]): The current planet this planet has.
        disabled (Union[Unset, bool]): Whether or not this planet is disabled, as assigned by ArrowHead.
        initial_owner (Union[Unset, str]): The faction that originally owned the planet.
        current_owner (Union[Unset, str]): The faction that currently controls the planet.
        regen_per_second (Union[Unset, float]): How much the planet regenerates per second if left alone.
        event (Union['Event', None, Unset]): Information on the active event ongoing on this planet, if one is active.
        statistics (Union[Unset, Statistics]): Contains statistics of missions, kills, success rate etc.
        attacking (Union[Unset, List[int]]): A list of Index integers that this planet is currently attacking.
    """

    index: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    sector: Union[Unset, str] = UNSET
    biome: Union[Unset, "Biome"] = UNSET
    hazards: Union[Unset, List["Hazard"]] = UNSET
    hash_: Union[Unset, int] = UNSET
    position: Union[Unset, "Position"] = UNSET
    waypoints: Union[Unset, List[int]] = UNSET
    max_health: Union[Unset, int] = UNSET
    health: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    initial_owner: Union[Unset, str] = UNSET
    current_owner: Union[Unset, str] = UNSET
    regen_per_second: Union[Unset, float] = UNSET
    event: Union["Event", None, Unset] = UNSET
    statistics: Union[Unset, "Statistics"] = UNSET
    attacking: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.event import Event

        index = self.index

        name = self.name

        sector = self.sector

        biome: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.biome, Unset):
            biome = self.biome.to_dict()

        hazards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hazards, Unset):
            hazards = []
            for hazards_item_data in self.hazards:
                hazards_item = hazards_item_data.to_dict()
                hazards.append(hazards_item)

        hash_ = self.hash_

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        waypoints: Union[Unset, List[int]] = UNSET
        if not isinstance(self.waypoints, Unset):
            waypoints = self.waypoints

        max_health = self.max_health

        health = self.health

        disabled = self.disabled

        initial_owner = self.initial_owner

        current_owner = self.current_owner

        regen_per_second = self.regen_per_second

        event: Union[Dict[str, Any], None, Unset]
        if isinstance(self.event, Unset):
            event = UNSET
        elif isinstance(self.event, Event):
            event = self.event.to_dict()
        else:
            event = self.event

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        attacking: Union[Unset, List[int]] = UNSET
        if not isinstance(self.attacking, Unset):
            attacking = self.attacking

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if sector is not UNSET:
            field_dict["sector"] = sector
        if biome is not UNSET:
            field_dict["biome"] = biome
        if hazards is not UNSET:
            field_dict["hazards"] = hazards
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if position is not UNSET:
            field_dict["position"] = position
        if waypoints is not UNSET:
            field_dict["waypoints"] = waypoints
        if max_health is not UNSET:
            field_dict["maxHealth"] = max_health
        if health is not UNSET:
            field_dict["health"] = health
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if initial_owner is not UNSET:
            field_dict["initialOwner"] = initial_owner
        if current_owner is not UNSET:
            field_dict["currentOwner"] = current_owner
        if regen_per_second is not UNSET:
            field_dict["regenPerSecond"] = regen_per_second
        if event is not UNSET:
            field_dict["event"] = event
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if attacking is not UNSET:
            field_dict["attacking"] = attacking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.biome import Biome
        from ..models.event import Event
        from ..models.hazard import Hazard
        from ..models.position import Position
        from ..models.statistics import Statistics

        d = src_dict.copy()
        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        sector = d.pop("sector", UNSET)

        _biome = d.pop("biome", UNSET)
        biome: Union[Unset, Biome]
        if isinstance(_biome, Unset):
            biome = UNSET
        else:
            biome = Biome.from_dict(_biome)

        hazards = []
        _hazards = d.pop("hazards", UNSET)
        for hazards_item_data in _hazards or []:
            hazards_item = Hazard.from_dict(hazards_item_data)

            hazards.append(hazards_item)

        hash_ = d.pop("hash", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        waypoints = cast(List[int], d.pop("waypoints", UNSET))

        max_health = d.pop("maxHealth", UNSET)

        health = d.pop("health", UNSET)

        disabled = d.pop("disabled", UNSET)

        initial_owner = d.pop("initialOwner", UNSET)

        current_owner = d.pop("currentOwner", UNSET)

        regen_per_second = d.pop("regenPerSecond", UNSET)

        def _parse_event(data: object) -> Union["Event", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                event_type_0 = Event.from_dict(data)

                return event_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Event", None, Unset], data)

        event = _parse_event(d.pop("event", UNSET))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Statistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Statistics.from_dict(_statistics)

        attacking = cast(List[int], d.pop("attacking", UNSET))

        planet = cls(
            index=index,
            name=name,
            sector=sector,
            biome=biome,
            hazards=hazards,
            hash_=hash_,
            position=position,
            waypoints=waypoints,
            max_health=max_health,
            health=health,
            disabled=disabled,
            initial_owner=initial_owner,
            current_owner=current_owner,
            regen_per_second=regen_per_second,
            event=event,
            statistics=statistics,
            attacking=attacking,
        )

        return planet
