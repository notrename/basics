import datetime

from lib.client.client import App

app = App(
    username='ogmnogoel',
    age=22,
)

app.create_task(
    name='test',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)
print(app.get_achievements())
print(app.get_tasks())
