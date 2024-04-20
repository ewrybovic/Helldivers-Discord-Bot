from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.home_world import HomeWorld
    from ..models.planet_info import PlanetInfo


T = TypeVar("T", bound="WarInfo")


@_attrs_define
class WarInfo:
    """Represents mostly static information of the current galactic war.

    Attributes:
        war_id (Union[Unset, int]): The identifier of the war season this WarInfo represents.
        start_date (Union[Unset, int]): A unix timestamp (in seconds) when this season started.
        end_date (Union[Unset, int]): A unix timestamp (in seconds) when this season will end.
        minimum_client_version (Union[Unset, str]): A version string indicating the minimum game client version the API
            supports.
        planet_infos (Union[Unset, List['PlanetInfo']]): A list of planets involved in this season's war.
        home_worlds (Union[Unset, List['HomeWorld']]): A list of homeworlds for the races (factions) involved in this
            war.
    """

    war_id: Union[Unset, int] = UNSET
    start_date: Union[Unset, int] = UNSET
    end_date: Union[Unset, int] = UNSET
    minimum_client_version: Union[Unset, str] = UNSET
    planet_infos: Union[Unset, List["PlanetInfo"]] = UNSET
    home_worlds: Union[Unset, List["HomeWorld"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        war_id = self.war_id

        start_date = self.start_date

        end_date = self.end_date

        minimum_client_version = self.minimum_client_version

        planet_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.planet_infos, Unset):
            planet_infos = []
            for planet_infos_item_data in self.planet_infos:
                planet_infos_item = planet_infos_item_data.to_dict()
                planet_infos.append(planet_infos_item)

        home_worlds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.home_worlds, Unset):
            home_worlds = []
            for home_worlds_item_data in self.home_worlds:
                home_worlds_item = home_worlds_item_data.to_dict()
                home_worlds.append(home_worlds_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if war_id is not UNSET:
            field_dict["warId"] = war_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if minimum_client_version is not UNSET:
            field_dict["minimumClientVersion"] = minimum_client_version
        if planet_infos is not UNSET:
            field_dict["planetInfos"] = planet_infos
        if home_worlds is not UNSET:
            field_dict["homeWorlds"] = home_worlds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.home_world import HomeWorld
        from ..models.planet_info import PlanetInfo

        d = src_dict.copy()
        war_id = d.pop("warId", UNSET)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        minimum_client_version = d.pop("minimumClientVersion", UNSET)

        planet_infos = []
        _planet_infos = d.pop("planetInfos", UNSET)
        for planet_infos_item_data in _planet_infos or []:
            planet_infos_item = PlanetInfo.from_dict(planet_infos_item_data)

            planet_infos.append(planet_infos_item)

        home_worlds = []
        _home_worlds = d.pop("homeWorlds", UNSET)
        for home_worlds_item_data in _home_worlds or []:
            home_worlds_item = HomeWorld.from_dict(home_worlds_item_data)

            home_worlds.append(home_worlds_item)

        war_info = cls(
            war_id=war_id,
            start_date=start_date,
            end_date=end_date,
            minimum_client_version=minimum_client_version,
            planet_infos=planet_infos,
            home_worlds=home_worlds,
        )

        return war_info
