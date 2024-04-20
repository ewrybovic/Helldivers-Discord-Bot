import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """An ongoing event on a Planet.

    Attributes:
        id (Union[Unset, int]): The unique identifier of this event.
        event_type (Union[Unset, int]): The type of event.
        faction (Union[Unset, str]): The faction that initiated the event.
        health (Union[Unset, int]): The health of the Event at the time of snapshot.
        max_health (Union[Unset, int]): The maximum health of the Event at the time of snapshot.
        start_time (Union[Unset, datetime.datetime]): When the event started.
        end_time (Union[Unset, datetime.datetime]): When the event will end.
        campaign_id (Union[Unset, int]): The identifier of the Campaign linked to this event.
        joint_operation_ids (Union[Unset, List[int]]): A list of joint operation identifier linked to this event.
    """

    id: Union[Unset, int] = UNSET
    event_type: Union[Unset, int] = UNSET
    faction: Union[Unset, str] = UNSET
    health: Union[Unset, int] = UNSET
    max_health: Union[Unset, int] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    campaign_id: Union[Unset, int] = UNSET
    joint_operation_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        event_type = self.event_type

        faction = self.faction

        health = self.health

        max_health = self.max_health

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        campaign_id = self.campaign_id

        joint_operation_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.joint_operation_ids, Unset):
            joint_operation_ids = self.joint_operation_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if faction is not UNSET:
            field_dict["faction"] = faction
        if health is not UNSET:
            field_dict["health"] = health
        if max_health is not UNSET:
            field_dict["maxHealth"] = max_health
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if joint_operation_ids is not UNSET:
            field_dict["jointOperationIds"] = joint_operation_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        event_type = d.pop("eventType", UNSET)

        faction = d.pop("faction", UNSET)

        health = d.pop("health", UNSET)

        max_health = d.pop("maxHealth", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        campaign_id = d.pop("campaignId", UNSET)

        joint_operation_ids = cast(List[int], d.pop("jointOperationIds", UNSET))

        event = cls(
            id=id,
            event_type=event_type,
            faction=faction,
            health=health,
            max_health=max_health,
            start_time=start_time,
            end_time=end_time,
            campaign_id=campaign_id,
            joint_operation_ids=joint_operation_ids,
        )

        return event
