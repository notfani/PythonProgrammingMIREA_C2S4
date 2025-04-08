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

success_rate = checks.groupby('message_id')['status'].apply(lambda x: (x == 2).mean())
success_rate = success_rate.dropna()
print('Самые сложные задачи:', success_rate.nsmallest(5))
print('Самые легкие задачи:', success_rate.nlargest(5))