tasks = {
    1: 'test1',
    14: 'test14',
    1532: 'test1532',
    112: 'test112',
}


def get_id(tasks_dict: dict) -> int:
    length_tasks = len(tasks_dict)  # 0
    return length_tasks + 1  # 1


def add_task(name: str = None):
    id_ = get_id(tasks_dict=tasks)
    tasks[id_] = name


def remove_task(id_: int):
    if id_ < 0:
        return False
    tasks.pop(id_)


def sort_tasks():
    # Получаем значения из словаря tasks и распаковываем их в список, с помощью синтаксического метода *
    values = [*tasks.values()]

    # удаляем данные из нашего словаря tasks
    tasks.clear()

    # Сортировка через обычный цикл
    for task in range(0, len(values)):
        tasks[task+1] = values[task]

    # Сортировка через метод update и генератор словаря
    tasks.update(
        {
            task+1: values[task] for task in range(0,len(values))
        }
    )

    return tasks


def show_tasks() -> str:
    tasks_str = 'Ваши задачи:\n'
    for id_, task_name in tasks.items():
        tasks_str += f'{id_}: {task_name}\n'
    return tasks_str


flag = True
while flag:
    action = input('Введите действие: ')
    if action == 'add':
        task_name = input('Введите название задачи: ')
        add_task(name=task_name)
    if action == 'remove':
        task_id = input('Введите id задачи: ')
        if task_id.isdigit():
            remove_task(int(task_id))
            sort_tasks()
    if action == 'show':
        print(show_tasks())
    if action == 'exit':
        break




# Лямбда функции
# action_scope = {
#     'add': lambda name: add_task(name=name),
#     'remove': lambda id_: remove_task(id_)
# }
# Тут обращаемся к lambda функции из словаря, затем вызываем саму функцию, передавая аргумент name
# action_scope['add']('work')


# lambda_def = lambda x,y: x*y
# lambda_def(2,2)



# Генераторы списков
nums = [i for i in range(0,21)] # Генерируем список от 0 до 20. Где i на каждой итерации принимает число последовательности range


if __name__ == '__main__':
    ...
