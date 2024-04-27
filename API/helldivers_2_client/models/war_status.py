from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign import Campaign
    from ..models.joint_operation import JointOperation
    from ..models.planet_attack import PlanetAttack
    from ..models.planet_event import PlanetEvent
    from ..models.planet_status import PlanetStatus


T = TypeVar("T", bound="WarStatus")


@_attrs_define
class WarStatus:
    """Represents a snapshot of the current status of the galactic war.

    Attributes:
        war_id (Union[Unset, int]): The war season this snapshot refers to.
        time (Union[Unset, int]): The time this snapshot was taken.
        impact_multiplier (Union[Unset, float]): This is the factor by which influence at the end of a mission is
            multiplied to calculate the impact on liberation
        story_beat_id_32 (Union[Unset, int]): Internal identifier, purpose unknown.
        planet_status (Union[Unset, List['PlanetStatus']]): A list of statuses for planets.
        planet_attacks (Union[Unset, List['PlanetAttack']]): A list of attacks currently ongoing.
        campaigns (Union[Unset, List['Campaign']]): A list of ongoing campaigns in the galactic war.
        joint_operations (Union[Unset, List['JointOperation']]): A list of JointOperations.
        planet_events (Union[Unset, List['PlanetEvent']]): A list of ongoing PlanetEvents.
    """

    war_id: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    impact_multiplier: Union[Unset, float] = UNSET
    story_beat_id_32: Union[Unset, int] = UNSET
    planet_status: Union[Unset, List["PlanetStatus"]] = UNSET
    planet_attacks: Union[Unset, List["PlanetAttack"]] = UNSET
    campaigns: Union[Unset, List["Campaign"]] = UNSET
    joint_operations: Union[Unset, List["JointOperation"]] = UNSET
    planet_events: Union[Unset, List["PlanetEvent"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        war_id = self.war_id

        time = self.time

        impact_multiplier = self.impact_multiplier

        story_beat_id_32 = self.story_beat_id_32

        planet_status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.planet_status, Unset):
            planet_status = []
            for planet_status_item_data in self.planet_status:
                planet_status_item = planet_status_item_data.to_dict()
                planet_status.append(planet_status_item)

        planet_attacks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.planet_attacks, Unset):
            planet_attacks = []
            for planet_attacks_item_data in self.planet_attacks:
                planet_attacks_item = planet_attacks_item_data.to_dict()
                planet_attacks.append(planet_attacks_item)

        campaigns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)

        joint_operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.joint_operations, Unset):
            joint_operations = []
            for joint_operations_item_data in self.joint_operations:
                joint_operations_item = joint_operations_item_data.to_dict()
                joint_operations.append(joint_operations_item)

        planet_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.planet_events, Unset):
            planet_events = []
            for planet_events_item_data in self.planet_events:
                planet_events_item = planet_events_item_data.to_dict()
                planet_events.append(planet_events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if war_id is not UNSET:
            field_dict["warId"] = war_id
        if time is not UNSET:
            field_dict["time"] = time
        if impact_multiplier is not UNSET:
            field_dict["impactMultiplier"] = impact_multiplier
        if story_beat_id_32 is not UNSET:
            field_dict["storyBeatId32"] = story_beat_id_32
        if planet_status is not UNSET:
            field_dict["planetStatus"] = planet_status
        if planet_attacks is not UNSET:
            field_dict["planetAttacks"] = planet_attacks
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns
        if joint_operations is not UNSET:
            field_dict["jointOperations"] = joint_operations
        if planet_events is not UNSET:
            field_dict["planetEvents"] = planet_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.campaign import Campaign
        from ..models.joint_operation import JointOperation
        from ..models.planet_attack import PlanetAttack
        from ..models.planet_event import PlanetEvent
        from ..models.planet_status import PlanetStatus

        d = src_dict.copy()
        war_id = d.pop("warId", UNSET)

        time = d.pop("time", UNSET)

        impact_multiplier = d.pop("impactMultiplier", UNSET)

        story_beat_id_32 = d.pop("storyBeatId32", UNSET)

        planet_status = []
        _planet_status = d.pop("planetStatus", UNSET)
        for planet_status_item_data in _planet_status or []:
            planet_status_item = PlanetStatus.from_dict(planet_status_item_data)

            planet_status.append(planet_status_item)

        planet_attacks = []
        _planet_attacks = d.pop("planetAttacks", UNSET)
        for planet_attacks_item_data in _planet_attacks or []:
            planet_attacks_item = PlanetAttack.from_dict(planet_attacks_item_data)

            planet_attacks.append(planet_attacks_item)

        campaigns = []
        _campaigns = d.pop("campaigns", UNSET)
        for campaigns_item_data in _campaigns or []:
            campaigns_item = Campaign.from_dict(campaigns_item_data)

            campaigns.append(campaigns_item)

        joint_operations = []
        _joint_operations = d.pop("jointOperations", UNSET)
        for joint_operations_item_data in _joint_operations or []:
            joint_operations_item = JointOperation.from_dict(joint_operations_item_data)

            joint_operations.append(joint_operations_item)

        planet_events = []
        _planet_events = d.pop("planetEvents", UNSET)
        for planet_events_item_data in _planet_events or []:
            planet_events_item = PlanetEvent.from_dict(planet_events_item_data)

            planet_events.append(planet_events_item)

        war_status = cls(
            war_id=war_id,
            time=time,
            impact_multiplier=impact_multiplier,
            story_beat_id_32=story_beat_id_32,
            planet_status=planet_status,
            planet_attacks=planet_attacks,
            campaigns=campaigns,
            joint_operations=joint_operations,
            planet_events=planet_events,
        )

        return war_status
