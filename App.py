def task():
    tasks = []  # empty list
    print(f" -------WELCOME TO THE TASK MANAGEMENT APP-------")

    total_task = int(input(f"Enter how many task you want to add: "))  # 5
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")  # enter task 1 =
        tasks.append(task_name)

    print(f"Today's task are \n{tasks}")

    while True:
        operation = int(input("\nEnter \n1-Add\n2-Update\n3-Delete\n4-View\n5-exit/stop"))
        if operation == 1:
            add = input(f"Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task is now {up} at {ind} ")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input(f"Enter task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total tasks = {len(tasks)}")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

        elif operation == 5:
            print(f"Closing the tasks")
            break

if __name__ == "__main__":
    task()