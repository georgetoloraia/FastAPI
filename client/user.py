import client

# main function
def main():
    # while loop, include help, choice = user_input, 0 = break.
    while True:
        # this is help for USER:
        print(
            "Command - Task Management",
            "1. Create a task",
            "2. Get a task by ID",
            "3. Get all tasks",
            "4. Update a task",
            "5. Delete a task",
            "0. Exit",
            sep = "\n"
        )
        
        # find functions
        choice = input("Enter your choice: ")

        operations = [create_task, get_task_id, get_all_tasks, update_task, delete_task]
        if choice.isdigit():
            operations[int(choice)-1]()
        elif choice == "0":
            break
        else:
            return "invalid usage, please input valid command :)"

def create_task():
    client_input = client.TaskClient()
    title = input("Enter the task title: ")
    completed = input("Is the task completed? (True/False): ")
    task = {"title": title, "completed": completed}
    response = client_input.create_task(**task)
    
    # print for see results:
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

def get_all_tasks():
    client_input = client.TaskClient()     
    tasks = client_input.get_all_tasks()
    print(tasks)

def update_task():
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
    
def delete_task():
    task_id = input("Enter the task ID: ")
    response = client.delete_task(task_id)
    if "detail" in response:
        print(response["detail"])
    else:
        print("Task deleted successfully.")
        print(f"Deleted Task ID: {response}")

if __name__ == "__main__":
    main()
