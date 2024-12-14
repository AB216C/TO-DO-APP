tasks = []
#Creating empty list main goals is to make sure all tasks added using add functions are stored and be able to be viewed or deleted by view and delete functions.
user_input = 0

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task has been added")
    
def view_task():
    if len(tasks)==0:
        print("Unable to view tasks. Task list is empty")
    else:
        print("TO DO LIST INCLUDE:")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}-{task}")
def delete_task():
    if len(tasks)==0:
        print(" Unable to delete. Your task list is empty")
    else:
        tasks.clear()
        print("Your tasks have been deleted")
#so far, the goal was define function to add, view, and delete tasks so they can be called anytime within the while loop
while True:
    
    print("""
          1. Add tasks
          2. View tasks
          3. Delete tasks
          4. Quit Application
          """)
    
    user_input=int(input("Enter your choice: "))

        
    if user_input == 1:
        add_task()
    elif user_input == 2:
        view_task()
    elif user_input == 3:
        delete_task()
    elif user_input == 4:
        print("Bye, don't hesitae to use this app next time")
        break
    else:
        print("You input is invalid. Please try again ")
#while loop is used here to display menu until user_input enters 4 to stop the loop from runnning. 
#if conditions below are they to connect menu and call functions depending on the user-s choice on the TO DO Menu.