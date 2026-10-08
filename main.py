name = input("what is your name")
print("welcome", name)

tasks = []

amount_of_tasks = int(input("how many tasks do you want to add?"))

for i in range(amount_of_tasks):
    task = input("enter task: ")
    tasks.append(task)

print("your tasks are:")
for task in tasks:
    print(task)