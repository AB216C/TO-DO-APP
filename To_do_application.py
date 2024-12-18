tasks = []
#Creating empty list main goals is to make sure all tasks added using add functions are stored and be able to be viewed or deleted by view and delete functions.
def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task has been added")
    
def view_task():
    if len(tasks)==0:
        print("Unable to view tasks. Task list is empty")
    else:
        print("TO DO LIST INCLUDE:")
        for index, task in enumerate(tasks):
            print(f"{index}-{task}")
def delete_task():
    if 0<=index<len(tasks):
        return tasks.pop(index)
    elif len(tasks)==0:
        print("Unable to delete. Task list is empty")
    else:
        print("You entered wrong index. Please try again")
#The goal was to define function(add, view, and delete tasks functions) so they can be called anytime within the while loop
while True:
    
    print("""
          TASK MENU
          1. Add tasks
          2. View tasks
          3. Delete tasks
          4. Quit Application
          """)
    try:
        user_input=int(input("Enter your choice: "))

            
        if user_input == 1:
            add_task()
        elif user_input == 2:
            view_task()
        elif user_input == 3:
            index=int(input("What index of a task do you want to delete?  "))
            delete_task()
            print("To view the remaining tasks, choose 2 from Task Menu")
        elif user_input == 4:
            print("Bye, don't hesitae to use this app next time")
            break
        else:
            print("You input is invalid. Please try again ")
    except ValueError:
        print("Your input result in error. Please try again")
#While loop is used here to display menu  indefinitely until user_input enters 4 to stop the loop from runnning. 
#If conditions were used to connect task menu with functions to respond directly to the user's request.