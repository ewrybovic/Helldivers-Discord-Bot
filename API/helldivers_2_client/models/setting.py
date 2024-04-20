from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reward import Reward
    from ..models.task import Task


T = TypeVar("T", bound="Setting")


@_attrs_define
class Setting:
    """Contains the details of an Assignment like reward and requirements.

    Attributes:
        type (Union[Unset, int]): The type of assignment, values unknown at the moment.
        override_title (Union[Unset, str]): The title of this assignment.
        override_brief (Union[Unset, str]): The briefing (description) of this assignment.
        task_description (Union[Unset, str]): A description of what is expected of Helldivers to complete the
            assignment.
        tasks (Union[Unset, List['Task']]): A list of Tasks describing the assignment requirements.
        reward (Union[Unset, Reward]): Represents the reward of an Assignment.
        flags (Union[Unset, int]): Flags, suspected to be a binary OR'd value, purpose unknown.
    """

    type: Union[Unset, int] = UNSET
    override_title: Union[Unset, str] = UNSET
    override_brief: Union[Unset, str] = UNSET
    task_description: Union[Unset, str] = UNSET
    tasks: Union[Unset, List["Task"]] = UNSET
    reward: Union[Unset, "Reward"] = UNSET
    flags: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        override_title = self.override_title

        override_brief = self.override_brief

        task_description = self.task_description

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        reward: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reward, Unset):
            reward = self.reward.to_dict()

        flags = self.flags

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if override_title is not UNSET:
            field_dict["overrideTitle"] = override_title
        if override_brief is not UNSET:
            field_dict["overrideBrief"] = override_brief
        if task_description is not UNSET:
            field_dict["taskDescription"] = task_description
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if reward is not UNSET:
            field_dict["reward"] = reward
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reward import Reward
        from ..models.task import Task

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        override_title = d.pop("overrideTitle", UNSET)

        override_brief = d.pop("overrideBrief", UNSET)

        task_description = d.pop("taskDescription", UNSET)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        _reward = d.pop("reward", UNSET)
        reward: Union[Unset, Reward]
        if isinstance(_reward, Unset):
            reward = UNSET
        else:
            reward = Reward.from_dict(_reward)

        flags = d.pop("flags", UNSET)

        setting = cls(
            type=type,
            override_title=override_title,
            override_brief=override_brief,
            task_description=task_description,
            tasks=tasks,
            reward=reward,
            flags=flags,
        )

        return setting
