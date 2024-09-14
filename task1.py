def tasks():
    tasks = [] #empty list
    print("-----TO-DO LIST APPLICATION------")

    total_tasks= int(input("Enter number of taks yo want to add="))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter \n 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been added successfully...")

        elif operation == 2:
            update_val = input("Enter the task you want to update = ")
            if update_val in tasks:
                upd = input("Enter new task = ")
                ind = tasks.index(update_val)
                tasks[ind] = upd
                print(f"Updated task {upd}")

        elif operation == 3:
            del_val = input("Enter the task yo want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task{del_val} has been deleted = ")

        elif operation == 4:
            print(f"Total Tasks = {tasks}")

        elif operation == 5:
            print("Closing the application....")
            break
        else:
            print("Invalid Input")


tasks()
