from tasks import add_task, show_tasks

name = input("what is your name? ")
print("welcome,", name)

tasks = []
how_many = int(input("how many tasks? "))

for i in range(how_many):
    task = input("enter a task: ")
    add_task(tasks, task)

show_tasks(tasks)