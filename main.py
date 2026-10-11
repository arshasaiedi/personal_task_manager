import os
from dotenv import load_dotenv
from tasks import add_task, show_tasks

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_pasword = input("enter admin password: ")
    if entered_pasword == admin_password:
        print("entered admin mode")
    else:
        print("wrong password")

name = input("what is your name? ")
print("welcome,", name)

tasks = []
how_many = int(input("how many tasks? "))

for i in range(how_many):
    task = input("enter a task: ")
    priority = input("enter the priority of the task (low/medium/high): ")
    while priority != "low" and priority != "medium" and priority != "high":
        print("Wrong priority. Please type low, medium, or high.")
        priority = input("enter the priority of the task (low/medium/high): ")
    add_task(tasks, task, priority)

show_tasks(tasks)

with open("tasks.txt", "a") as file:
    file.write(f"{name}'s tasks: {tasks}\n")