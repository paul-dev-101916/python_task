from task import TaskType
from project import ProjectType

from datetime import datetime

my_project = ProjectType()
my_project.set_project_name("Home Task")
my_project.set_project_description("This is a project of doing home stuff")
taskManagerDAO = TaskManagerDAO()

taskManagerDAO.insert_project(my_project)

my_task = TaskType()
my_task.set_task_name("Take out trash")
my_task.set_task_description("This is a task to take out the trash")
my_task.set_task_due_date(datetime(2018, 4, 3, 12, 35))

print(my_task.task_due_date)
