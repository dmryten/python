import sys

username = input("username:")
password = input("password:")

with open('./log.txt', 'r', encoding='utf-8') as f:
    result = dict(line.strip().split(":") for line in f if line)

count = 0
def if_user_exit():
    count = 0
    for key in result:
        if username == key:
            count += 1
    if count == 0:
        print("The user is not exist")
    sys.exit()
def if_user_lock():
    ('./ lock_log.txt', 'r')
    for line in f.readlines():
        if username == line.strip():
            print("The user is locked")
            sys.exit()
        if_user_exit()
        if_user_lock()

while count < 3:
    if password == result.get(username):
        info='''welcome user {_username} login'''.format(_username=username)
        print(info)
    break

    if_user_exit()
    count += 1

    print ('извините, пользователь заблокирован')
    ('./ lock_log.txt', 'a')
    f_lock.write(username+'\n')
else:
    print("login filed:three filed will be lock,only have {_count} changes".format(_count=3-count))
    username = input("username:")
    password = input("password:")
