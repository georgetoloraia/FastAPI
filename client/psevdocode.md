this is the user input program

help usage == "choise"

we need four funqtion, 1. read 2. insert 3. update 4. remove

#1. def main():
        client = TaskClient

        while True:
            print("Command Prompt - Task Management")
            print("1. Create a task")
            print("2. Get a task by ID")
            print("3. Get all tasks")
            print("4. Update a task")
            print("5. Delete a task")
            print("0. Exit")

            choise = ("Enter your choice: ")

            if choise == "1":
                title = input("Enter the task title: ")
                completed = ("Enter, is the task completed/uncompleted? (True/False): ")
                task = {"title": title, "completed": completed}
                response = client.create_task(**task)
                print("Task created successfully.")
                print(f"Task ID: {response['id']}")
                print(f"Title: {response['title']}")
                print(f"Completed: {response['completed']}")

3. greatind def funqtions

def create_task():
    client_input = client.TaskClient()
    title = input("Enter the task title: ")
    completed = input("Is the task completed? (True/False): ")
    task = {"title": title, "completed": completed}
    response = client_input.create_task(**task)
    print("Task created successfully.")
    print(f"Task ID: {response['id']}")
    print(f"Title: {response['title']}")
    print(f"Completed: {response['completed']}")

def get_task_id():
    client_input = client.TaskClient()
    task_id = input("Enter the task ID: ")
    response = client_input.get_task(task_id)
    if "detail" in response:
        print(response["detail"])
    else:
        print(f"Task ID: {response['id']}")
        print(f"Title: {response['title']}")
        print(f"Completed: {response['completed']}")

def get_all_tacks():
    client_input = client.TaskClient()     
    tasks = client_input.get_all_tasks()
    print(tasks)

def update_tack():
    client_input = client.TaskClient()
    task_id = input("Enter the task ID: ")
    title = input("Enter the updated task title: ")
    completed = input("Is the task completed? (True/False): ")
    task = {"title": title, "completed": completed}
    response = client.update_task(task_id, **task)
    if "detail" in response:
        print(response["detail"])
    else:
        print("Task updated successfully.")
        print(f"Task ID: {response['id']}")
        print(f"Title: {response['title']}")
        print(f"Completed: {response['completed']}")
    
def delete_tack():
    client_input = client.TaskClient()
    task_id = input("Enter the task ID: ")
    response = client.delete_task(task_id)
    if "detail" in response:
        print(response["detail"])
    else:
        print("Task deleted successfully.")
        print(f"Deleted Task ID: {response}")

4. greting returns from def main():
    while True:
        print("Command Prompt - Task Management")
        print("1. Create a task")
        print("2. Get a task by ID")
        print("3. Get all tasks")
        print("4. Update a task")
        print("5. Delete a task")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            return create_task()
        if choice == "2":
            return get_task_id()
        if choice == "3":
            return get_all_tacks()
        if choice == "4":
            return update_tack()
        if choice == "5":
            return delete_tack()
        if choice == "0":
            break
        else:
            return ("invalid usage, please input valid command :)")
