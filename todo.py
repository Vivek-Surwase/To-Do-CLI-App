
import sys                        # importing required libraries
from datetime import date

def show():
    s = '''
    Usage :-
     python todo.py add "todo item"      # Add a new todo
     python todo.py ls tasks             # Show remaining todos
     python todo.py del NUMBER           # Delete a todo
     python todo.py done NUMBER          # Complete a todo
     python todo.py show commands        # Show usage
     python todo.py report tasks         # Statistics
    '''
    print(s)

def add(todo):
    with open('todo.txt' ,'a') as f:      #opening file as file object,append mode
        f.write("\n" + todo)
    print("You added the task :" + todo)

def ls():
    with open('todo.txt' ,'r') as f:
       lines = f.readlines()            #reading the file and storing them as list of strings
       for i in range(1,len(lines)):
           print("[" + str(i) + "]" +" " + lines[i])

def delete(number):
    with open('todo.txt' ,'r') as f:
       lines = f.readlines()
    lines.remove(lines[number])
    
    newContent = ""
    for line in lines:
        newContent = newContent + line
    with open('todo.txt' ,'w') as f:
        f.write(newContent)

def done(number):
    with open('todo.txt' ,'r') as f:
       lines = f.readlines()
    taskCompleted = lines[number]
    delete(number)

    with open('done.txt' ,'r') as g:
       dones = g.readlines()

    newContent = ""
    for d in dones:
        newContent = newContent + d
    newContent = newContent + taskCompleted    
    with open('done.txt' ,'w') as g:
        g.write(newContent)

def report():                     #This presents the status of the to do app
    today = date.today()
    today= today.strftime("%d/%m/%Y")
    with open('todo.txt' ,'r') as f:
       pendingTasks = f.readlines()
    with open('done.txt' ,'r') as g:
       completedTasks = g.readlines()
    print(str(today) + " Pending: " + str(len(pendingTasks) -1) + " Completed: " + str(len(completedTasks)))
    
function = sys.argv[1]                 #Taking arguments from command line
argument = sys.argv[2]

if(function.strip() == "show"):      #if-elif loop to execute the task 
    show()
elif(function.strip() == "add"):
    add(argument)
elif(function.strip() == "ls"):
    ls()
elif(function.strip() == "delete"):
    delete(int(argument))
elif(function.strip() == "done"):
    done(int(argument))
elif(function.strip() == "report"):
    report()            