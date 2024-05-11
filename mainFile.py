from todoFile import TodoClass
global count
count = 0  # to count the Tasks entered
tasks = []

print("\nWelcome To This TODO List App \n")
def menuFuction():
    print("1: To Add a Task \n"
          "2: To Show All Tasks List \n"
          "3: To Search a Task \n"
          "4: To Update a Task \n"
          "5: To Delete a Single Task \n"
          "6: To Clear a List \n"
          "7: To Exit")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1: addTask()
        case 2: showAllTask()
        case 3: searchTask()
        case 4: updateTask()
        case 5: deleteTask()
        case 6: clearList()
        case _: quit()


def addTask():
    # global taskPriorite
    global  count, taskPriorite

    taskId= input("Enter The Id Of The Task: ")
    chechid = int(checkId(taskId))   #The Id Must be Checked

    if chechid == 1:
        print("\nThe id is reserved Please Change it \n")
        addTask()

    taskName = input("Enter The Name Of The Task: ")
    startTime = input("Enter The Starting Time of The Task: ")
    endTime = input("Enter The Ending Time of The Task: ")
    try:
        taskPriorite = int(input("Enter The Priority of The Task From 1-3: "))
    except:
        print("\n Please Enter All Information Correctly")
        addTask()

    if taskId != '' and taskName != '' and startTime != '' and endTime != '' and taskPriorite != '':
        if 0 < taskPriorite < 4:
            taskItem = TodoClass( taskId, taskName, startTime, endTime, taskPriorite)
            tasks.append(taskItem)

            print("\nThe Task Add Successfully!!\n")
            count += 1
        else:
            print("\nPlease Enter All Information Correctly")
            addTask()
    else:
        print("\nPlease Enter All Information Correctly")
        addTask()

    print("1: To Add Again \n"
          "2. To Back Manu \n"
          "3: To Exit \n")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1: addTask()
        case 2: menuFuction()
        case _: quit()

def showAllTask():

    print("Task Id \t\t Name of Task \t\t Staring Time \t\t Ending Time \t\t Priority ")
    for taskItem in tasks:
        print(taskItem.taskId, "\t\t\t\t", taskItem.taskName, "\t\t\t\t\t", taskItem.startTime, "\t\t\t\t\t",taskItem.endTime, "\t\t\t",taskItem.taskPriorite)

    print("1. To Back Manu \n"
          "2: To Exit \n")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1: menuFuction()
        case _: quit()

def searchTask():
    global count
    idTask = input("Enter The Task Id: ")
    chechid = int(checkId(idTask))  # The Id Must be Checked

    if chechid == 0:
        print("\nThere is No Task In This Id \n")
        menuFuction()
    for taskItem in tasks:
        if idTask == taskItem.taskId:
            print("Task Id \t\t Name of Task \t\t Staring Time \t\t Ending Time \t\t Priority ")
            print(taskItem.taskId, "\t\t\t\t", taskItem.taskName, "\t\t\t\t\t", taskItem.startTime, "\t\t\t\t\t", taskItem.endTime, "\t\t\t", taskItem.taskPriorite)

    print("1. To Back Manu \n"
          "2: To Exit \n")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1: menuFuction()
        case _: quit()

def updateTask():
    global count, taskPriorite
    theid = input("Enter The Task Id: ")
    chechid = int(checkId(theid))  # The Id Must be Checked

    if chechid == 0:
        print("\nThere is No Task In This Id \n")
        menuFuction()
    for taskItem in tasks:
        if theid == taskItem.taskId:
            taskName = input("Enter The Name Of The Task: ")
            startTime = input("Enter The Starting Time of The Task: ")
            endTime = input("Enter The Ending Time of The Task: ")
            try:
                taskPriorite = int(input("Enter The Priority of The Task From 1-3: "))
            except:
                print("\n Please Enter All Information Correctly")
                updateTask()
            if theid != '' and taskName != '' and startTime != '' and endTime != '' and taskPriorite != '':
                if 0 < taskPriorite < 4:
                    taskItem.taskName = taskName
                    taskItem.startTime = startTime
                    taskItem.endTime = endTime
                    taskItem.taskPriorite = taskPriorite
                    print("\nThe Task Updated Successfully!!\n")
                else:
                    print("\nPlease Enter All Information Correctly")
                    updateTask()
            else:
                print("\nPlease Enter All Information Correctly")
                updateTask()

        print("1. To Back Manu \n"
              "2: To Exit \n")
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1:
                menuFuction()
            case _:
                quit()


def deleteTask():
    global count
    theId = input("Enter The Task Id: ")
    chechid = int(checkId(theId))  # The Id Must be Checked

    if chechid == 0:
        print("\nThere is No Task In This Id \n")
        menuFuction()
    for taskItem in tasks:
        if theId == taskItem.taskId:
            tasks.remove(taskItem)

    print("\nThe Task Deleted Successfully!!\n")
    print("1. To Back Manu \n"
          "2: To Exit \n")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1: menuFuction()
        case _: quit()

def clearList():
    tasks.clear()
    print("\nThe Task List Cleared Successfully!!\n")

    print("1. To Back Manu \n"
          "2: To Exit \n")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1: menuFuction()
        case _: quit()

def checkId(theId):
    flag = 0
    for taskItem in tasks:
        if(theId == taskItem.taskId):
            flag = 1
    return flag

menuFuction()




