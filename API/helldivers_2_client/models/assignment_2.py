import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reward_2 import Reward2
    from ..models.task_2 import Task2


T = TypeVar("T", bound="Assignment2")


@_attrs_define
class Assignment2:
    """Represents an assignment given by Super Earth to the community.
    This is also known as 'Major Order's in the game.

        Attributes:
            id (Union[Unset, int]): The unique identifier of this assignment.
            progress (Union[Unset, List[int]]): A list of numbers, how they represent progress is unknown.
            title (Union[Unset, str]): The title of the assignment.
            briefing (Union[Unset, str]): A long form description of the assignment, usually contains context.
            description (Union[Unset, str]): A very short summary of the description.
            tasks (Union[Unset, List['Task2']]): A list of tasks that need to be completed for this assignment.
            reward (Union[Unset, Reward2]): The reward for completing an Assignment.
            expiration (Union[Unset, datetime.datetime]): The date when the assignment will expire.
    """

    id: Union[Unset, int] = UNSET
    progress: Union[Unset, List[int]] = UNSET
    title: Union[Unset, str] = UNSET
    briefing: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tasks: Union[Unset, List["Task2"]] = UNSET
    reward: Union[Unset, "Reward2"] = UNSET
    expiration: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        progress: Union[Unset, List[int]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress

        title = self.title

        briefing = self.briefing

        description = self.description

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        reward: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reward, Unset):
            reward = self.reward.to_dict()

        expiration: Union[Unset, str] = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if progress is not UNSET:
            field_dict["progress"] = progress
        if title is not UNSET:
            field_dict["title"] = title
        if briefing is not UNSET:
            field_dict["briefing"] = briefing
        if description is not UNSET:
            field_dict["description"] = description
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if reward is not UNSET:
            field_dict["reward"] = reward
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reward_2 import Reward2
        from ..models.task_2 import Task2

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        progress = cast(List[int], d.pop("progress", UNSET))

        title = d.pop("title", UNSET)

        briefing = d.pop("briefing", UNSET)

        description = d.pop("description", UNSET)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = Task2.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        _reward = d.pop("reward", UNSET)
        reward: Union[Unset, Reward2]
        if isinstance(_reward, Unset):
            reward = UNSET
        else:
            reward = Reward2.from_dict(_reward)

        _expiration = d.pop("expiration", UNSET)
        expiration: Union[Unset, datetime.datetime]
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = isoparse(_expiration)

        assignment_2 = cls(
            id=id,
            progress=progress,
            title=title,
            briefing=briefing,
            description=description,
            tasks=tasks,
            reward=reward,
            expiration=expiration,
        )

        return assignment_2
