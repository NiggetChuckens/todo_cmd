def save_tasks(task, filepath='./tasks.txt'):
    file = open(filepath, 'a')
    file.write(f'{task}\n')
    file.close()
    
def read_tasks(filepath='./tasks.txt'):
    file = open(filepath, 'r')
    for task in file.readlines():
        print(task)
        
if __name__ == '__main__':
    def menu():
        try:
            selection = int(input("select what to do:\n1) add a task\n2) read all the saved tasks\n\n"))
            return selection
        except:
            menu()   
    selection = menu()
    if selection == 1:
        task = input("insert a task to save: ")
        save_tasks(task)
    elif selection == 2:
        read_tasks()
    else:
        menu()