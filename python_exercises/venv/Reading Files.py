employees_list = open("employees", "r")
print(employees_list.readable())
print(employees_list.read())
print(employees_list.readline())
print(employees_list.readlines()[2])


employees_list.close()