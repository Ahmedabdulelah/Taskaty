from argparse import ArgumentParser
from .TaskControllers import TaskController

def main():
    controller = TaskController('tasks.txt')
    parsers = ArgumentParser(description = 'This Is Simple CLI Task Manager')
    subparser = parsers.add_subparsers()

    add_task = subparser.add_parser('add', help = 'Add The Given Task')
    add_task.add_argument('title', help = 'Title Of The Task', type = str)
    add_task.add_argument('-d','--description',help = 'Short Description Of The Task' ,type = str, default = None)
    add_task.add_argument('-s','--start_date', help = 'Date Of Begin The Task', type = str,default = None)
    add_task.add_argument('-e','--end_date', help = 'Date Of End The Task', type = str,default = None)
    add_task.add_argument('--done',help ='Check Whether the Task Done or Not',default = False )
    add_task.set_defaults(func = controller.add_task)

    list_tasks = subparser.add_parser('list', help = 'List Unfinished Tasks')
    list_tasks.add_argument('-a','--all',help = 'List All The Tasks', action = 'store_true')
    list_tasks.set_defaults(func = controller.display)
    
    check_task = subparser.add_parser('check', help = 'Check The Given The Task')
    check_task.add_argument('-t','--task',help = 'Number Of The Task To Be Done, If Not Specified, Last Task Will Be Removed.', type=int)
    check_task.set_defaults(func = controller.check_task)

    remove_task = subparser.add_parser('remove' ,help = 'Remove A Task')
    remove_task.add_argument('-t','--task', help ='The Task To Be Removed (Number)',type = int)
    remove_task.set_defaults(func = controller.remove)

    reset = subparser.add_parser('reset', help = 'Remove All Tasks')
    reset.set_defaults(func = controller.reset)

    args = parsers.parse_args()  
    args.func(args)


if __name__ == '__main__':
    main()