from collections import deque
from typing import Dict, List

class TaskNode:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.description = ""
        self.children = []
        self.parent = None
        self.priority = -10
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

class TaskListStore:
    def __init__(self):
        self.tasks = deque([])
        self.task_id_counter = 0

    def append(self, task: TaskNode):
        self.tasks.append(task)

    def replace(self, tasks: List[Dict]):
        self.tasks = deque(tasks)

    def popleft(self):
        return self.tasks.popleft()

    def is_empty(self):
        return False if self.tasks else True

    def next_task_id(self):
        self.task_id_counter += 1
        return self.task_id_counter

    def get_task_names(self):
        return [t["task_name"] for t in self.tasks]