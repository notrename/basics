from lib.task_manager.dataclasses import Task
from dataclasses import asdict


class TaskManager:
    __TASKS = {}

    def __init__(self):
        ...

    def __get_id(
            self,
    ) -> int:
        length_tasks = len(self.__TASKS)
        return length_tasks + 1

    def add_task(
            self,
            task: Task,
    ) -> None:
        id_ = self.__get_id()
        task = asdict(task)
        deadline = task.get('deadline')
        if deadline:
            deadline = deadline.strftime('%Y-%m-%d %H:%M')
            task.update(deadline=deadline)
        self.__TASKS[id_] = task

    def remove_task(
        self,
        id_: int,
    ) -> None | bool:
        if id_ < 0:
            return False
        self.__TASKS.pop(id_)
        self.__sort_tasks()

    def __sort_tasks(
        self
    ) -> None:
        """
        Private метод, доступный только из класса.
        Сортирует задачи по id
        :return: None
        """
        values = [*self.__TASKS.values()]
        self.__TASKS.clear()
        self.__TASKS.update(
            {
                task + 1: values[task] for task in range(0, len(values))
            }
        )

    def get_tasks(self) -> str:
        tasks_str = 'Ваши задачи:\n'
        for id_, task_name in self.__TASKS.items():
            tasks_str += f'{id_}: {task_name}\n'
        return tasks_str

    def __str__(self):  # Дандер(Магические) методы
        return 'объект класса TaskManager'

    def __repr__(self):
        ...

    def __bool__(self):
        return self.__TASKS

    def __getattr__(self, item):
        if item == 'tasks':
            return self.get_tasks()
        else:
            return 'Атрибут не существует'


if __name__ == '__main__':
    print('Это модуль!')