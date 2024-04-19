from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.galaxy_stats import GalaxyStats
    from ..models.planet_stats import PlanetStats


T = TypeVar("T", bound="WarSummary")


@_attrs_define
class WarSummary:
    """Gets general statistics about the galaxy and specific planets.

    Attributes:
        galaxy_stats (Union[Unset, GalaxyStats]): Represents galaxy wide statistics.
        planets_stats (Union[Unset, List['PlanetStats']]): Contains statistics for specific planets.
    """

    galaxy_stats: Union[Unset, "GalaxyStats"] = UNSET
    planets_stats: Union[Unset, List["PlanetStats"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        galaxy_stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.galaxy_stats, Unset):
            galaxy_stats = self.galaxy_stats.to_dict()

        planets_stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.planets_stats, Unset):
            planets_stats = []
            for planets_stats_item_data in self.planets_stats:
                planets_stats_item = planets_stats_item_data.to_dict()
                planets_stats.append(planets_stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if galaxy_stats is not UNSET:
            field_dict["galaxy_stats"] = galaxy_stats
        if planets_stats is not UNSET:
            field_dict["planets_stats"] = planets_stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.galaxy_stats import GalaxyStats
        from ..models.planet_stats import PlanetStats

        d = src_dict.copy()
        _galaxy_stats = d.pop("galaxy_stats", UNSET)
        galaxy_stats: Union[Unset, GalaxyStats]
        if isinstance(_galaxy_stats, Unset):
            galaxy_stats = UNSET
        else:
            galaxy_stats = GalaxyStats.from_dict(_galaxy_stats)

        planets_stats = []
        _planets_stats = d.pop("planets_stats", UNSET)
        for planets_stats_item_data in _planets_stats or []:
            planets_stats_item = PlanetStats.from_dict(planets_stats_item_data)

            planets_stats.append(planets_stats_item)

        war_summary = cls(
            galaxy_stats=galaxy_stats,
            planets_stats=planets_stats,
        )

        return war_summary
