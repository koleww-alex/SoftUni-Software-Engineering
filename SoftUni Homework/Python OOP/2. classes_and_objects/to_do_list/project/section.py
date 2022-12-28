from Classes_and_Objects.to_do_list.project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        cleared_task = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                cleared_task += 1

        return f'Cleared {cleared_task} tasks.'

    def view_section(self):
        section_info = [f'Section {self.name}:']

        for task in self.tasks:
            section_info.append(task.details())

        return '\n'.join(section_info)

