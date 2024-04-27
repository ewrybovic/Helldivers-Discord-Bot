from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanetEvent")


@_attrs_define
class PlanetEvent:
    """An ongoing event on a planet.

    Attributes:
        id (Union[Unset, int]): The unique identifier of this event.
        planet_index (Union[Unset, int]): The index of the planet.
        event_type (Union[Unset, int]): A numerical identifier that indicates what type of event this is.
        race (Union[Unset, int]): The identifier of the faction that owns the planet currently.
        health (Union[Unset, int]): The current health of the event.
        max_health (Union[Unset, int]): The current maximum health of the event.
        start_time (Union[Unset, int]): When this event started.
        expire_time (Union[Unset, int]): When the event will end.
        campaign_id (Union[Unset, int]): The unique identifier of a related campaign.
        joint_operation_ids (Union[Unset, List[int]]): A list of identifiers of related joint operations.
    """

    id: Union[Unset, int] = UNSET
    planet_index: Union[Unset, int] = UNSET
    event_type: Union[Unset, int] = UNSET
    race: Union[Unset, int] = UNSET
    health: Union[Unset, int] = UNSET
    max_health: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    expire_time: Union[Unset, int] = UNSET
    campaign_id: Union[Unset, int] = UNSET
    joint_operation_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        planet_index = self.planet_index

        event_type = self.event_type

        race = self.race

        health = self.health

        max_health = self.max_health

        start_time = self.start_time

        expire_time = self.expire_time

        campaign_id = self.campaign_id

        joint_operation_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.joint_operation_ids, Unset):
            joint_operation_ids = self.joint_operation_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if planet_index is not UNSET:
            field_dict["planetIndex"] = planet_index
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if race is not UNSET:
            field_dict["race"] = race
        if health is not UNSET:
            field_dict["health"] = health
        if max_health is not UNSET:
            field_dict["maxHealth"] = max_health
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if joint_operation_ids is not UNSET:
            field_dict["jointOperationIds"] = joint_operation_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        planet_index = d.pop("planetIndex", UNSET)

        event_type = d.pop("eventType", UNSET)

        race = d.pop("race", UNSET)

        health = d.pop("health", UNSET)

        max_health = d.pop("maxHealth", UNSET)

        start_time = d.pop("startTime", UNSET)

        expire_time = d.pop("expireTime", UNSET)

        campaign_id = d.pop("campaignId", UNSET)

        joint_operation_ids = cast(List[int], d.pop("jointOperationIds", UNSET))

        planet_event = cls(
            id=id,
            planet_index=planet_index,
            event_type=event_type,
            race=race,
            health=health,
            max_health=max_health,
            start_time=start_time,
            expire_time=expire_time,
            campaign_id=campaign_id,
            joint_operation_ids=joint_operation_ids,
        )

        return planet_event
