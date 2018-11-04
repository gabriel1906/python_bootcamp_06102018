import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = "dane/logs.txt"

user_last_login = {}
user_total_time = {}

with open(file_name) as f:
    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action == "LOGIN":
            user_last_login[login] = time
        if action == "LOGOUT":
            user_total_time[login] = user_total_time.get(login, 0) + time - user_last_login[login]


def sort_key(x):
    return x[1]


print("Czas przebywania w systemie:")
for item in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(item)
    # print(f"- {login}: {user_total_time[login]}")
