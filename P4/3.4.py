import matplotlib.pyplot as plt
import pandas as pd
import datetime
import ast


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename, col_names):
    return pd.read_csv(filename, delimiter=',', names=col_names, encoding='utf8')


messages = load_csv('messages.csv', ['id', 'task', 'variant', 'group', 'time'])
checks = load_csv('checks.csv', ['id', 'message_id', 'time', 'status'])
statuses = load_csv('statuses.csv', ['task', 'variant', 'group', 'time', 'status', 'achievements'])

messages['time'] = pd.to_datetime(messages['time'])
checks['time'] = pd.to_datetime(checks['time'])
statuses['time'] = pd.to_datetime(statuses['time'])

statuses['achievements'] = statuses['achievements'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
statuses['achievements'] = statuses['achievements'].apply(len)

messages['date'] = messages['time'].dt.date
messages_per_day = messages.groupby(['date', 'task'])['id'].count().unstack().fillna(0)
messages_per_day.plot(title='Изменение активности студентов по задачам')
plt.show()