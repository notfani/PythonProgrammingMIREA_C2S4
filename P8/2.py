import pytest
from datetime import datetime


class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def authenticate(self, login_attempt, password_attempt):
        if self.login == login_attempt and self.password == password_attempt:
            return True
        else:
            return False

    def authorize(self, required_roles):
        if self.role in required_roles:
            return True
        else:
            return False


class Project:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def find_task_by_name(self, name):
        return [task for task in self.tasks if task.name == name]

    def find_task_by_start_date(self, start_date):
        return [task for task in self.tasks if task.start_date == start_date]

    def find_task_by_end_date(self, end_date):
        return [task for task in self.tasks if task.end_date == end_date]

    def is_completed(self):
        return all(task.status for task in self.tasks)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'tasks': [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        for task_data in data['tasks']:
            task = Task.from_dict(task_data)
            project.add_task(task)
        return project


class Task:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = False
        self.performers = []

    def change_status(self):
        self.status = not self.status

    def add_performer(self, performer):
        self.performers.append(performer)

    def remove_performer(self, performer):
        self.performers.remove(performer)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'status': self.status,
            'performers': self.performers
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        task.status = data['status']
        task.performers = data['performers']
        return task

# Тесты для класса User
def test_user_authentication():
    user = User("test_user", "password123", "developer")
    assert user.authenticate("test_user", "password123") is True
    assert user.authenticate("test_user", "wrong_password") is False

def test_user_authorization():
    user = User("test_user", "password123", "developer")
    assert user.authorize(["developer", "admin"]) is True
    assert user.authorize(["admin"]) is False

# Тесты для класса Task
def test_task_creation():
    task = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    assert task.name == "Task 1"
    assert task.description == "Description of Task 1"
    assert task.status is False

def test_task_status_change():
    task = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    task.change_status()
    assert task.status is True
    task.change_status()
    assert task.status is False

def test_task_performer_management():
    task = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    task.add_performer("User A")
    assert "User A" in task.performers
    task.remove_performer("User A")
    assert "User A" not in task.performers

# Тесты для класса Project
def test_project_creation():
    project = Project("Project 1", "Description of Project 1", datetime.now(), datetime.now())
    assert project.name == "Project 1"
    assert project.description == "Description of Project 1"
    assert project.tasks == []

def test_project_task_management():
    project = Project("Project 1", "Description of Project 1", datetime.now(), datetime.now())
    task = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    project.add_task(task)
    assert len(project.tasks) == 1
    project.remove_task(task)
    assert len(project.tasks) == 0

def test_project_completion_status():
    project = Project("Project 1", "Description of Project 1", datetime.now(), datetime.now())
    task1 = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    task2 = Task("Task 2", "Description of Task 2", datetime.now(), datetime.now())
    project.add_task(task1)
    project.add_task(task2)
    assert project.is_completed() is False
    task1.change_status()  # Завершим одну задачу
    assert project.is_completed() is False
    task2.change_status()  # Завершим вторую задачу
    task2.change_status()  # Вернем статус второй задачи обратно
    assert project.is_completed() is False
    task2.change_status()  # Завершим вторую задачу
    assert project.is_completed() is True

# Тесты для сериализации и десериализации
def test_task_serialization():
    task = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    task_dict = task.to_dict()
    new_task = Task.from_dict(task_dict)
    assert new_task.name == task.name
    assert new_task.description == task.description
    assert new_task.status == task.status

def test_project_serialization():
    project = Project("Project 1", "Description of Project 1", datetime.now(), datetime.now())
    task = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    project.add_task(task)
    project_dict = project.to_dict()
    new_project = Project.from_dict(project_dict)
    assert new_project.name == project.name
    assert new_project.description == project.description
    assert len(new_project.tasks) == len(project.tasks)

def test_find_task_by_name():
    project = Project("Project 1", "Description of Project 1", datetime.now(), datetime.now())
    task1 = Task("Task 1", "Description of Task 1", datetime.now(), datetime.now())
    task2 = Task("Task 2", "Description of Task 2", datetime.now(), datetime.now())
    project.add_task(task1)
    project.add_task(task2)

    # Проверка поиска по имени
    found_tasks = project.find_task_by_name("Task 1")
    assert len(found_tasks) == 1
    assert found_tasks[0].name == "Task 1"

    found_tasks = project.find_task_by_name("Non-existent Task")
    assert len(found_tasks) == 0

def test_find_task_by_start_date():
    start_date = datetime.now()
    project = Project("Project 1", "Description of Project 1", start_date, datetime.now())
    task1 = Task("Task 1", "Description of Task 1", start_date, datetime.now())
    task2 = Task("Task 2", "Description of Task 2", datetime.now(), datetime.now())
    project.add_task(task1)
    project.add_task(task2)

    # Проверка поиска по дате начала
    found_tasks = project.find_task_by_start_date(start_date)
    assert len(found_tasks) == 1
    assert found_tasks[0].name == "Task 1"

    found_tasks = project.find_task_by_start_date(datetime.now())
    assert len(found_tasks) == 0

def test_find_task_by_end_date():
    end_date = datetime.now()
    project = Project("Project 1", "Description of Project 1", datetime.now(), end_date)
    task1 = Task("Task 1", "Description of Task 1", datetime.now(), end_date)
    task2 = Task("Task 2", "Description of Task 2", datetime.now(), datetime.now())
    project.add_task(task1)
    project.add_task(task2)

    # Проверка поиска по дате окончания
    found_tasks = project.find_task_by_end_date(end_date)
    assert len(found_tasks) == 1
    assert found_tasks[0].name == "Task 1"

    found_tasks = project.find_task_by_end_date(datetime.now())
    assert len(found_tasks) == 0
