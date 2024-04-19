import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistics import Statistics


T = TypeVar("T", bound="War")


@_attrs_define
class War:
    """Global information of the ongoing war.

    Attributes:
        started (Union[Unset, datetime.datetime]): When this war was started.
        ended (Union[Unset, datetime.datetime]): When this war will end (or has ended).
        now (Union[Unset, datetime.datetime]): The time the snapshot of the war was taken, also doubles as the timestamp
            of which all other data dates from.
        client_version (Union[Unset, str]): The minimum game client version required to play in this war.
        factions (Union[Unset, List[str]]): A list of factions currently involved in the war.
        impact_multiplier (Union[Unset, float]): A fraction used to calculate the impact of a mission on the war effort.
        statistics (Union[Unset, Statistics]): Contains statistics of missions, kills, success rate etc.
    """

    started: Union[Unset, datetime.datetime] = UNSET
    ended: Union[Unset, datetime.datetime] = UNSET
    now: Union[Unset, datetime.datetime] = UNSET
    client_version: Union[Unset, str] = UNSET
    factions: Union[Unset, List[str]] = UNSET
    impact_multiplier: Union[Unset, float] = UNSET
    statistics: Union[Unset, "Statistics"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        started: Union[Unset, str] = UNSET
        if not isinstance(self.started, Unset):
            started = self.started.isoformat()

        ended: Union[Unset, str] = UNSET
        if not isinstance(self.ended, Unset):
            ended = self.ended.isoformat()

        now: Union[Unset, str] = UNSET
        if not isinstance(self.now, Unset):
            now = self.now.isoformat()

        client_version = self.client_version

        factions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.factions, Unset):
            factions = self.factions

        impact_multiplier = self.impact_multiplier

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if started is not UNSET:
            field_dict["started"] = started
        if ended is not UNSET:
            field_dict["ended"] = ended
        if now is not UNSET:
            field_dict["now"] = now
        if client_version is not UNSET:
            field_dict["clientVersion"] = client_version
        if factions is not UNSET:
            field_dict["factions"] = factions
        if impact_multiplier is not UNSET:
            field_dict["impactMultiplier"] = impact_multiplier
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.statistics import Statistics

        d = src_dict.copy()
        _started = d.pop("started", UNSET)
        started: Union[Unset, datetime.datetime]
        if isinstance(_started, Unset):
            started = UNSET
        else:
            started = isoparse(_started)

        _ended = d.pop("ended", UNSET)
        ended: Union[Unset, datetime.datetime]
        if isinstance(_ended, Unset):
            ended = UNSET
        else:
            ended = isoparse(_ended)

        _now = d.pop("now", UNSET)
        now: Union[Unset, datetime.datetime]
        if isinstance(_now, Unset):
            now = UNSET
        else:
            now = isoparse(_now)

        client_version = d.pop("clientVersion", UNSET)

        factions = cast(List[str], d.pop("factions", UNSET))

        impact_multiplier = d.pop("impactMultiplier", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Statistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Statistics.from_dict(_statistics)

        war = cls(
            started=started,
            ended=ended,
            now=now,
            client_version=client_version,
            factions=factions,
            impact_multiplier=impact_multiplier,
            statistics=statistics,
        )

        return war
