import json
import requests

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

# loads() reading from a string
todos = json.loads(response.text)

todos_by_user = {}

for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

top_users = sorted(todos_by_user.items(),
                   key = lambda x: x[1],
                   reverse = True)

max_complete = top_users[0][1]

users = []

for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print(f"user(s) {max_users} completed {max_complete} TODOs")

def keep(todo):
    is_completed = todo['completed']
    has_max_count = str(todo['userId']) in users
    return is_completed and has_max_count

with open("json_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent = 2)
