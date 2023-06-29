import requests
import user

class TaskClient:
    BASE_URL = "http://127.0.0.1:8000/tasks/"

    def create_task(self, **task):
        return requests.post(f"{TaskClient.BASE_URL}", json=task).json()

    def get_task(self, task_id):
        return requests.get(f"{TaskClient.BASE_URL}{task_id}").json()

    def get_all_tasks(self):
        return requests.get(f"{TaskClient.BASE_URL}").json()

    def update_task(self, task_id, **task):
        return requests.put(f"{TaskClient.BASE_URL}{task_id}", json=task).json()

    def delete_task(self, task_id):
        return requests.delete(f"{TaskClient.BASE_URL}{task_id}").json()

client = TaskClient()

# client.create_task(id=22, title="Walk the dog", completed=False)
# print(client.get_all_tasks())
# print(client.update_task(20, id=20, title="Walk the dog again", completed=False))
# print(client.delete_task(19))