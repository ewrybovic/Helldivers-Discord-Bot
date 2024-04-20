from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Statistics")


@_attrs_define
class Statistics:
    """Contains statistics of missions, kills, success rate etc.

    Attributes:
        missions_won (Union[Unset, int]): The amount of missions won.
        missions_lost (Union[Unset, int]): The amount of missions lost.
        mission_time (Union[Unset, int]): The total amount of time spent planetside (in seconds).
        terminid_kills (Union[Unset, int]): The total amount of bugs killed since start of the season.
        automaton_kills (Union[Unset, int]): The total amount of automatons killed since start of the season.
        illuminate_kills (Union[Unset, int]): The total amount of Illuminate killed since start of the season.
        bullets_fired (Union[Unset, int]): The total amount of bullets fired
        bullets_hit (Union[Unset, int]): The total amount of bullets hit
        time_played (Union[Unset, int]): The total amount of time played (including off-planet) in seconds.
        deaths (Union[Unset, int]): The amount of casualties on the side of humanity.
        revives (Union[Unset, int]): The amount of revives(?).
        friendlies (Union[Unset, int]): The amount of friendly fire casualties.
        mission_success_rate (Union[Unset, int]): A percentage indicating how many started missions end in success.
        accuracy (Union[Unset, int]): A percentage indicating average accuracy of Helldivers.
        player_count (Union[Unset, int]): The total amount of players present (at the time of the snapshot).
    """

    missions_won: Union[Unset, int] = UNSET
    missions_lost: Union[Unset, int] = UNSET
    mission_time: Union[Unset, int] = UNSET
    terminid_kills: Union[Unset, int] = UNSET
    automaton_kills: Union[Unset, int] = UNSET
    illuminate_kills: Union[Unset, int] = UNSET
    bullets_fired: Union[Unset, int] = UNSET
    bullets_hit: Union[Unset, int] = UNSET
    time_played: Union[Unset, int] = UNSET
    deaths: Union[Unset, int] = UNSET
    revives: Union[Unset, int] = UNSET
    friendlies: Union[Unset, int] = UNSET
    mission_success_rate: Union[Unset, int] = UNSET
    accuracy: Union[Unset, int] = UNSET
    player_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        missions_won = self.missions_won

        missions_lost = self.missions_lost

        mission_time = self.mission_time

        terminid_kills = self.terminid_kills

        automaton_kills = self.automaton_kills

        illuminate_kills = self.illuminate_kills

        bullets_fired = self.bullets_fired

        bullets_hit = self.bullets_hit

        time_played = self.time_played

        deaths = self.deaths

        revives = self.revives

        friendlies = self.friendlies

        mission_success_rate = self.mission_success_rate

        accuracy = self.accuracy

        player_count = self.player_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if missions_won is not UNSET:
            field_dict["missionsWon"] = missions_won
        if missions_lost is not UNSET:
            field_dict["missionsLost"] = missions_lost
        if mission_time is not UNSET:
            field_dict["missionTime"] = mission_time
        if terminid_kills is not UNSET:
            field_dict["terminidKills"] = terminid_kills
        if automaton_kills is not UNSET:
            field_dict["automatonKills"] = automaton_kills
        if illuminate_kills is not UNSET:
            field_dict["illuminateKills"] = illuminate_kills
        if bullets_fired is not UNSET:
            field_dict["bulletsFired"] = bullets_fired
        if bullets_hit is not UNSET:
            field_dict["bulletsHit"] = bullets_hit
        if time_played is not UNSET:
            field_dict["timePlayed"] = time_played
        if deaths is not UNSET:
            field_dict["deaths"] = deaths
        if revives is not UNSET:
            field_dict["revives"] = revives
        if friendlies is not UNSET:
            field_dict["friendlies"] = friendlies
        if mission_success_rate is not UNSET:
            field_dict["missionSuccessRate"] = mission_success_rate
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if player_count is not UNSET:
            field_dict["playerCount"] = player_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        missions_won = d.pop("missionsWon", UNSET)

        missions_lost = d.pop("missionsLost", UNSET)

        mission_time = d.pop("missionTime", UNSET)

        terminid_kills = d.pop("terminidKills", UNSET)

        automaton_kills = d.pop("automatonKills", UNSET)

        illuminate_kills = d.pop("illuminateKills", UNSET)

        bullets_fired = d.pop("bulletsFired", UNSET)

        bullets_hit = d.pop("bulletsHit", UNSET)

        time_played = d.pop("timePlayed", UNSET)

        deaths = d.pop("deaths", UNSET)

        revives = d.pop("revives", UNSET)

        friendlies = d.pop("friendlies", UNSET)

        mission_success_rate = d.pop("missionSuccessRate", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        player_count = d.pop("playerCount", UNSET)

        statistics = cls(
            missions_won=missions_won,
            missions_lost=missions_lost,
            mission_time=mission_time,
            terminid_kills=terminid_kills,
            automaton_kills=automaton_kills,
            illuminate_kills=illuminate_kills,
            bullets_fired=bullets_fired,
            bullets_hit=bullets_hit,
            time_played=time_played,
            deaths=deaths,
            revives=revives,
            friendlies=friendlies,
            mission_success_rate=mission_success_rate,
            accuracy=accuracy,
            player_count=player_count,
        )

        return statistics