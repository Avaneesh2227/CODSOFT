def check_current_doc():
    with open("To-do-list.txt") as todo:
        data = todo.readlines()
        num_questions = len(data)
    return [data, num_questions]


def choose_option():
    global done
    choice = input('''
        1. View your tasks
        2. Mark a task as finished
        3. Add a task
        4. Delete a task
        5. Edit a task
        6. Clear all tasks
        7. Type "x" to exit the program
        Choose one of the following: 1/2/3/4/5/6/x  
        '''
                   )
    if choice == "1":
        view_tasks()
    elif choice == "2":
        finish = input("Which task have you finished? Enter the task number: ")
        finish_task(finish)
    elif choice == "3":
        task = input("Enter your task: ")
        add_task(task)
    elif choice == "4":
        delete = input("Which task do you want to delete? Enter the task number: ")
        delete_task(delete)
    elif choice == "5":
        edit = input("Which task do you want to edit?: ")
        edited = input("Type updated task: ")
        edit_task(edit, f"{edited}\n")
    elif choice == "6":
        clear_tasks()
    elif choice.lower() == "x":
        done = True
        return
    else:
        print("Please enter a valid input")
        return


def add_task(task):
    num = check_current_doc()[1]
    with open("To-do-list.txt", "a") as add:
        add.write(f"{num + 1}. {task}\n")
    return


def edit_task(edit, edited):
    num = check_current_doc()[1]
    data = check_current_doc()[0]
    if edit.isnumeric() and int(edit) <= num:
        with open("To-do-list.txt", "w") as h:
            count = 1
            for i in range(num):
                if i + 1 == int(edit):
                    h.write(f"{count}. {edited}")
                else:
                    h.write(f"{count}. {data[i][3:]}")
                    count += 1
        return
    else:
        print("Please enter a valid task number")
        return


def delete_task(delete):
    num = check_current_doc()[1]
    data = check_current_doc()[0]
    if delete.isnumeric() and int(delete) <= num:
        with open("To-do-list.txt", "w") as g:
            count = 1
            for i in range(num):
                if i + 1 == int(delete):
                    continue
                else:
                    g.write(f"{count}. {data[i][3:]}")
                    count += 1
        return
    else:
        print("Please enter a valid task number")
        return


def finish_task(finish):
    num = check_current_doc()[1]
    data = check_current_doc()[0]
    if finish.isnumeric() and int(finish) <= num:
        with open("Finished tasks.txt", "a") as f:
            f.write(f"• {data[int(finish) - 1]}\n")
        delete_task(finish)
    else:
        print("Please enter a valid task number")
    return


def view_tasks():
    data = check_current_doc()[0]
    str = ""
    for i in data:
        str += i
    print(str)
    return


def clear_tasks():
    with open("To-do-list.txt", "w") as f:
        f.write("")
    return


done = False
try:
    with open("To-do-list.txt", "r") as file:
        pass
    with open("Finished tasks.txt", "r") as file2:
        pass
except FileNotFoundError:
    with open("To-do-list.txt", "w") as file:
        file.write("")
    with open("Finished tasks.txt", "w") as file2:
        file2.write("")
else:
    while not done:
        choose_option()
