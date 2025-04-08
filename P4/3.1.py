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


messages['weekday'] = messages['time'].dt.day_name()
weekday_counts = messages['weekday'].value_counts()
plt.figure(figsize=(10, 5))
weekday_counts.sort_index().plot(kind='bar', title='Активность студентов по дням недели')
plt.xticks(rotation=45)
plt.show()