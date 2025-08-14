# print("-" * 10, "TO DO LIST", "-" * 10)

def show_task(tasks:list):
   if tasks :
       print("YOUR TASKS -")
       for i in tasks :
           print(f"\t- {i}")
   else:
       print("YOU HAVE NO TASKS IN THE LIST...")

def add_task(tasks:list):
    add = input("ENTER A TASK -").lower()
    tasks.append(add)

def remove_task(tasks:list):
    remove_1 = input("ENTER THE TASK WHICH YOU WANT TO REMOVE -").lower()
    tasks.remove(remove_1)
    print("THE TASK IS REMOVED SUCCESSFULLY.")

tasks = []

while True:
    print("-" * 10, "TO DO LIST", "-" * 10)
    print("1.SHOW TASK")
    print("2.ADD THE TASK")
    print("3.REMOVE A TASK FROM LIST.")
    print("4.EXIT")
    option = int(input("ENTER THE OPTION :"))

    if option == 1:
        show_task(tasks)
        print("")

    elif option == 2:
        add_task(tasks)
        print("")

    elif option == 3:
        remove_task(tasks)
        print("")

    elif option == 4:
        break

    else:
        print("YOU ENTERED THE WRONG OPTION...")


