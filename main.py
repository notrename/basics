

def get_id(tasks_dict: dict) -> int:
    length_tasks = len(tasks_dict)  # 0
    return length_tasks + 1  # 1



def add_task(name: str = None):
    id_ = get_id(tasks_dict=tasks)
    tasks[id_] = name


def remove_task(id_: int):
    tasks.pop(id_)


tasks = {
    1: 'test1',
    3: 'test3',
    6: 'test6',
    12: 'test12',
    5: 'test5',
}


def sort_tasks():
    values = [*tasks.values()]
    tasks_complete = {}
    for task in range(0,len(tasks)):
        tasks_complete[task+1] = values[task]

    print(tasks_complete)

sort_tasks()

# flag = True
#
# while flag:
#     action = input('Введите действие: ')
#     if action == 'add':
#         task_name = input('Введите название задачи: ')
#         add_task(name=task_name)
#     if action == 'remove':
#         task_id = int(input('Введите id задачи: '))
#         remove_task(task_id)
#     if action == 'show':
#         print(tasks)
#     if action == 'exit':
#         break
#
# print(tasks)

