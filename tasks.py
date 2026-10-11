def add_task(tasks, task, priority):
    tasks.append(f"{task} - {priority}")

def show_tasks(tasks):
    for task in tasks:
        print(task)