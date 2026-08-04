
import json
import os

file_name = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r") as file: #opens the file for reading if available
            return json.load(file)
    return []  #Load tasks from the file if it exists in os; otherwise start with an empty list.

# Save tasks to file
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file)
    #Basically 'dumps' the inputted tasks into the file    

# Add task
def add_task(tasks):
    task_input = input("Enter tasks separated by commas: ")

    new_tasks = [task.strip() for task in task_input.split(",")] #.strip() removes spaces at the beginning and end of a string.
                                #.split() turns the given input into a list separating each letter or word by what is in the ()
    tasks.extend(new_tasks)
    save_tasks(tasks)
    print("Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1): #enumerate() adds numbering to the system. then we added start from 1
        """enumerate(tasks, start=1) returns 
           (1, "Study")
           (2, "Read")
           (3, "Exercise")
           for index, task gives: (index, task) = (1, "Study") etc
        """
        print(f"{index}. {task}")
    """For gives an iteration over the numbering of each task.
    f string injects variable into texts.
    example:   the for loop gives 
    index = 1
    task = "Study"
    then the print(f"{index}. {task}") produces: 1. Study"""


# Delete task
def delete_task(tasks):
    task_name = input("Enter task name to delete: ").strip().lower()
    for task in tasks:
        if task.lower() == task_name:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Task not found.")



# Main program
tasks = load_tasks()

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

