FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a todo file and return the list of todos.
    """
    with open(filepath, 'r') as l_file:
        l_todos = l_file.readlines()
    return l_todos


def write_todos(todos_arg: object, filepath: object = FILEPATH) -> object:
    """
    Write a list of todos to the todo file.
    """
    with open(filepath, 'w') as l_file:
        l_file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())

