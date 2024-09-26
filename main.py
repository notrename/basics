import datetime

from lib.task_manager.dataclasses import Task
from lib.task_manager.model import TaskManager


tm = TaskManager()


task = Task(
    name='Решить практическое задание',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

tm.add_task(task)
tm.get_tasks()
tm.remove_task(id_=1)
