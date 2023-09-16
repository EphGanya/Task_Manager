#importing current date

from datetime import date


#login section
passwords = dict()                                  # dictonary with username as key and passwords as value
with open('user.txt', 'r') as user:                   # open file user.txt in read mode  
    for line in user:                                 # read file linewise       
        user = line.split(',')[0].strip()           # split at comma and store value at index 0 as user  
        password = line.split(',')[1].strip()       # split at comma and store value at index 1 as password 
        passwords[user] = password                  # create key with user and assign password as value
        
while True:                                          # indefinitely loop
    print(f'''          LOGIN       ''')                
    username = input('Enter your username: ')       # input username 
    password = input('Enter your password: ')       # input password    
    if username in passwords:                       # if username is present in dictionary 
        if passwords[username] == password:         # check if password matches  
            print("\n Login successful!\n")
            break                                   # exit loop    
        else:                                       # indicate that password does not match   
            print('Wrong password!\n')                
    else:                                           # indicate that username not found in dictionary 
        print('Username not found!\n')                 


#choices for the user to choose from
while True:
    if username=="admin":
        menu = input('''Select option one of the options below:

r - register username

a - add task

va - view all tasks

vm - view my tasks

e - exit

s - stats

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
    

        if username == "admin":

            new_userLogin = False

            new_usersName = input("Enter username: ")
            if new_usersName==username:
                print ("username already exists")
                new_userLogin = False

            while new_userLogin == False:

                new_userPass = input("Enter password: ")

                validate = input("Confirm password: ")

                if new_userPass == validate:

                    new_userLogin = True

                if new_userPass != validate:

                    print("password did not match. Try again")

            if new_userPass == validate:

                print("password matches. New user created")

                append_me = open("user.txt", "a")

                append_me.write("\n" + str(new_usersName) + ", " + str(validate))

                append_me.close()

        if   username != "admin":
            print("Only admin can add a new user.")
        pass
#if user selects "a" he/she will have to enter input

#input will be written in 'tasks'_file


    elif menu == "a":
    
        tasks = open("tasks.txt", "a")

        username = input("Enter the usersname of which task is assigned to: ")

        title = input("Enter the title of the task: ")

        description = input("Enter task description: ")

        due_date = input("Enter task due date YYYY-MM-DD: ")

        current_date = date.today()

        completed = input("Please indicate if task is completed or not (Yes/No): ")

        tasks.write(str(username) + ", " + str(title) + ", " + str(description) + ", " + str(due_date) + ", " + str(current_date) + ", " + str(completed) + "\n")

        tasks.close()
        pass

#if user selects "va" he/she will be given info of every file in an easy to read format

    elif menu == "va":

        tasks_file = open("tasks.txt", "r+")

#loop to print out details in proper manner

        for line in tasks_file:

            username, title, description, due_date, date, completed = line.split(", ")

            print(f'''
                Assigned To:    {username} 

                Task:   {title}

                Task description:   {description}

                Due Date:   {due_date}

                Date Assigned:  {date}

                Task Complete:  {completed}

                ''')

        tasks_file.close()
    pass
#if user selects "vm" program   will desplay specific user task


    if menu == "vm":

        view = open("tasks.txt", "r")

        for line in view:

            user_name, title, description, due_date, date, completed = line.split(", ")

            if username == user_name:

                print(f'''

        Assigned To:    {user_name}

        Task:   {title}

        Task description:   {description}

        Due Date:   {due_date}

        Date Assigned:  {date}

        Task Complete:  {completed}

        ''')

        view.close()

#if the user selects "e" program breaks

    pass

    if menu == "e":

        print('Goodbye!!!')
        exit()

#if user selects "s". number of tasks and number of users are displayed


    if menu == "s":
            if username ==  'admin':
                print('Statistics')      
                with open('tasks.txt', 'r') as task:                              # open tasks.txt in read mode 
                    print('Total number of tasks is:', len(task.readlines()))                  # calculate the total number of lines in the file, which is the number of tasks    
                with open('user.txt', 'r') as task:                               # open user.txt in read mode 
                    print('Total number of user is:', len(task.readlines()))                  # calculate the total number of lines in the file, which is the number of users   
    
    pass
