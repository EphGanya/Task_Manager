import datetime 
from datetime import datetime as dt

#login section
passwords = dict()                                  
with open('user.txt', 'r') as user:                     
    for line in user:                                       
        user = line.split(',')[0].strip()           
        password = line.split(',')[1].strip()        
        passwords[user] = password                  
        
while True:                                         
    print(f'''          LOGIN       ''')                
    username = input('Enter your username: ')      
    password = input('Enter your password: ')         
    if username in passwords:                       
        if passwords[username] == password:         
            print("\n Login successful!\n")
            break                                    
        else:                                         
            print('Wrong password!\n')                
    else:                                          
        print('Username not found!\n')                 


# Function to register a user
def reg_user():
     # Only admin can register a new user
    if username != "admin":
        print("Access denied! Only admin has permission to perform this operation.")
        return

    # Prompt for new user's details
    new_username = input("Enter username: ")
    # Check if username already exists
    with open("user.txt", "r") as f:
        for line in f:
            existing_username, _ = line.strip().split(", ")
            if existing_username == new_username:
                print("Username already exists. Please try again.")
                return
    
        new_password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        # Validate new user's details
        if new_password != confirm_password:
            print("Passwords don't match. Please try again.")
            return

        # Add new user to user.txt
        with open("user.txt", "a") as f:
            f.write(f"{new_username}, {new_password}\n")
        print("User registered successfully.")
    return (" ")

# Function to add a task
def add_task():
    # Prompt for task details
    assigned_to = input("Enter username of person task is assigned to: ")
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    today= datetime.date.today()
    date_assigned = today.strftime("%d %b %Y")
    due_date = input("Enter due date (d% b% Y%) e.g (1 Jan 2020): ")
    task_status = "No"
    
    # Add new task to tasks.txt
    with open("tasks.txt", "a") as f:
        f.write(str(assigned_to) + ", " + str(task_name) + ", " + str(task_description) + ", " + str(date_assigned) + ", " + str(due_date) + ", " + str(task_status) + "\n")
    print("Task added successfully.")
    return (" ")

# Function to view all tasks
def view_all():
    tasks_file = open("tasks.txt", "r")
#loop to print out details in proper manner
    for line in tasks_file:

        username, name, description, date, due_date , completed = line.split(", ")

        print(f'''
            Assigned To:    {username} 

            Task:   {name}

            Task description:   {description}

            Date Assigned:  {date}

            Due Date:   {due_date}

            Task Complete:  {completed}

            ''')

    tasks_file.close() 
    return (" ")

# Function to view tasks assigned to current user
def view_mine():
    tasks = read_tasks()
    assigned_tasks = []

    for i, task in enumerate(tasks):
        if task[0] == username:
            assigned_tasks.append(task)
            print(f"{i+1} - Assigned to: {task[0]}")
            print(f"  Title: {task[1]}")
            print(f"  Description: {task[2]}")
            print(f"  Date Assigned: {task[3]}")
            print(f"  Due Date: {task[4]}")
            print(f"  Completed: {task[5]}\n")
           
    print("Enter the number of the desired task to interact with it.")
    print("Enter '-1' to return to the main menu.")

    task_number = int(input("Enter your choice: "))

    if task_number == -1:
        return
    else:
        task_index = task_number - 1
        selected_task = tasks[task_index]
        interact_with_task(selected_task)

    return (" ")

#Function to read tasks from the text file
def read_tasks():
    tasks = []
    with open("tasks.txt", "r") as tasksfile:
        for line in tasksfile:
            task = line.strip().split(", ")
            tasks.append(task)
    return tasks

#Function to allow user to interact with tasks assigned to them
def interact_with_task(task):
    tasks= read_tasks()
    task_index = tasks.index(task) 
    completed = task[5]
   
    print(f"Selected Task - Assigned to: {task[0]}")
    print(f"  Title: {task[1]}")
    print(f"  Description: {task[2]}")
    print(f"  Date Assigned: {task[3]}")
    print(f"  Due Date: {task[4]}")
    print(f"  Completed: {completed}\n")
   
    if completed == "No":
        mark_completed = input("\nWould you like to mark this task as completed? (Y/N): ")
        if mark_completed.lower() == "y":
            tasks[task_index][5] = "Yes"
            write_tasks(tasks)
            print("\nTask marked as completed!")
   
    edit_task = input("\nWould you like to edit this task? (Y/N): ")
    if edit_task.lower() == "y":
        new_user = input("\nEnter the new username to which the assignment will be assigned: ")
        new_due_date = input("Enter the new due date (dd-mm-yyyy) e.g 1 Jan 2023: ")
   
        tasks[task_index][0] = new_user
        tasks[task_index][4] = new_due_date
   
        write_tasks(tasks)
        print("\nTask updated successfully!")

#function to write the edited tasks back to tyhe text file  
def write_tasks(tasks):
    with open("tasks.txt", "w") as tasks_file:
        for task in tasks:
            tasks_file.write(", ".join(task) + "\n")

def generate_reports():
    # Open the tasks.txt file for reading
    with open("tasks.txt", "r") as tasks_file:
        tasks = tasks_file.readlines()
        total_tasks = len(tasks)
        total_completed_tasks = 0
        total_uncompleted_tasks = 0
        total_overdue_tasks = 0
        overdue_tasks = 0
    
        #identifying due date by idexing for dates comparison to detect if task is overdue
        tasks_file.seek(0)
        for line in tasks_file:
            line = line.strip().split(", ")
            #indexing the due date from the text file
            overdue_date=line[4]
            #parse a string representing a time according to a format
            date_obj=datetime.datetime.strptime(overdue_date,'%d %b %Y').date()
            #convert dates to strings and format it for comparison with today's date
            date_fmt=date_obj.strftime('%Y-%m-%d')
            due_date= datetime.datetime.strptime(date_fmt,'%Y-%m-%d').date()
            today=datetime.date.today()
            
        
        tasks_file.seek(0)
        for task in tasks:
            task = task.strip().split(", ") 
            if task[-1] == "No":
                total_uncompleted_tasks += 1
            elif task [-1]== "Yes" :
                total_completed_tasks += 1
            elif due_date < today :
                overdue_tasks += 1
                total_overdue_tasks += 1    
        
         # Open the tasks.txt file for reading
        with open('tasks.txt', 'r') as f:
            # Read all lines in the file
            lines = f.readlines()

        # Count the total number of tasks and total number of users
        total_tasks = len(lines)
        users = set()
        
        for line in lines:
            users.add(line.split(', ')[0])

            # Get the total number of tasks assigned to each user and count the number of completed and overdue tasks
            user_tasks = {}
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue_tasks = 0
    
        for line in lines:
            fields = line.split(', ')
            user = fields[0]
            status = fields[-1].strip()

            # Increase the task count for the user
            if user in user_tasks:
                user_tasks[user] += 1
            else:
                user_tasks[user] = 1
  
            # Check if the task is completed or overdue
            due_date_str = fields[-2]
            due_date = datetime.datetime.strptime(due_date_str, '%d %b %Y').date()
            if due_date < datetime.date.today():
                overdue_tasks += 1
            if status == 'No':
                uncompleted_tasks += 1
            else :
                completed_tasks +=1

        incomplete_percent = round(total_uncompleted_tasks / total_tasks * 100, 2)
        overdue_percent= round(overdue_tasks/total_tasks *100, 2)

            # Open the task_overview.txt file for writing
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write(f"Number of tasks: {total_tasks}\n")
            task_overview_file.write(f"Number of completed tasks: {total_completed_tasks}\n")
            task_overview_file.write(f"Number of uncompleted tasks: {total_uncompleted_tasks}\n")
            task_overview_file.write(f"Number of tasks overdue: {overdue_tasks}\n")
            task_overview_file.write(f"Percentage of incomplete tasks: {incomplete_percent}%\n")
            task_overview_file.write(f"Percentage of overdue tasks: {overdue_percent}%\n")

        with open ("task_overview.txt", "r") as task_overview:
            task_overview = task_overview.read()
            print("\n           TASK OVERVIEW           ")
            print(task_overview)

    # Define a function to calculate task statistics for each user
    def calculateuserstats(tasks, username):
        usertasks = [task for task in tasks if task['username'] == username]
        tot_tasks= len(tasks)
        total_tasks = len(usertasks)
        completedtasks = sum(1 for task in usertasks if task['status'] == 'Yes')
        outstanding_tasks = total_tasks - completedtasks
        overduetasks = sum(1 for task in usertasks if task['status'] == 'No' and dt.strptime(task['due_date'], '%d %b %Y').date() < dt.today().date())
        # Calculate percentage completed, outstanding, and overdue tasks
        try:
            percent_assigned = (total_tasks / tot_tasks)* 100
        except ZeroDivisionError:
            percent_assigned = 0    
        try:
            percent_completed = (completedtasks / total_tasks)* 100
        except ZeroDivisionError:
            percent_completed = 0
        try:
            percent_outstanding = (outstanding_tasks / total_tasks)* 100
        except ZeroDivisionError:
            percent_outstanding = 0
        try:
            percent_overdue = (overduetasks / total_tasks) * 100
        except ZeroDivisionError:
            percent_overdue = 0

        return (tot_tasks,total_tasks,percent_assigned, percent_completed, percent_outstanding, percent_overdue)

    # Read data from tasks.txt
    with open('tasks.txt', 'r') as f:
        lines = f.readlines()

    # Parse data into list of dictionaries
    tasks = []
    for line in lines:
        task_data = line.strip().split(', ')
        tasks.append({
            'username': task_data[0],
            'task': task_data[1],
            'task_desc': task_data[2],
            'date_assigned': task_data[3],
            'due_date': task_data[4],
            'status': task_data[5]
            })

    task_total=len(tasks)

    # Get a list of all unique usernames
    with open ('user.txt', 'r') as g:
        users = g.readlines()
        usernames = list(set([task['username'] for task in tasks]))
        num_users=len(users)

    # Calculate statistics for each user
    user_stats = {}
    for username in usernames:
        user_stats[username] = calculateuserstats(tasks, username)

    #write to task_overview text file
    with open('user_overview.txt', 'w') as f:
        # Write the header
        f.write(f'Total number of users: {num_users}\n')
        f.write(f'Total number of tasks: {task_total}\n\n')

        for username, stats in user_stats.items():

            f.write(f'{username}:\n')
            f.write(f'Total tasks assigned: {stats[1]}\n')
            f.write(f'Percentage of total tasks assigned: {stats[2]}%\n')
            f.write(f'Percentage of tasks completed: {stats[3]}%\n')
            f.write(f'Percentage of tasks still to be completed: {stats[4]}%\n')
            f.write(f'Percentage of tasks overdue: {stats[5]}%\n\n')     

    with open ('user_overview.txt', 'r') as user_overview:
        user_overview = user_overview.read()
        print(f"            USER OVERVIEW           ")
        print(user_overview)           
    
    return (" ")

            
                        
def generate_statistics():
    with open("tasks.txt", "r") as task_overview_file:
        task_overview = task_overview_file.read()
    with open ("user.txt", "r") as file:
        file= file.readlines()
        users= set()
        for line in file:
            users.add(line.split(', ')[0])

    print("TASK OVERVIEW\n\n")
    print(task_overview)
    print("\n\nUSER OVERVIEW\n")
    print (users)
    return (" ")

#choices for the user to choose from
while True:
    if username=="admin":
        menu = input('''Select an option from one of the options below:

r - register username

a - add task

va - view all tasks

vm - view my tasks

gr - generate reports

ds - display stats

e - exit



:''').lower()
        
    else:
        menu = input('''Select option one of the options below:

r - register username

a - add task

va - view all tasks

vm - view my tasks

e - exit

:''').lower()

#if user selects admin selects "r" and he/she is the admin, they can register a user to user_file

    if menu == "r":
        register=reg_user()
        print (register)
        pass

#if user selects "a" he/she will have to enter input which will be written in 'tasks'_file
    elif menu == "a":
        task_addition=add_task()
        print(task_addition)
        pass

#if user selects "va" he/she will be given info of every file in an easy to read format
    elif menu == "va":
        view_all_tasks=view_all()
        print(view_all_tasks)
        pass

#if user selects "vm" program   will desplay specific user task
    if menu == "vm":
        view_my_tasks=view_mine()
        print (view_my_tasks)
        pass

#if user selects "gr" reports of the tasks will be generated
    if menu == "gr":
        reports=generate_reports()
        print(reports)
        pass

#if user selects "ds". number of tasks and number of users are displayed
    if menu == "ds":
        statistis=generate_statistics()
        print(statistis)
        pass

#if the user selects "e" program breaks
    if menu == "e":
        print('Goodbye!!!')
        exit()

