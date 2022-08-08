import curses
import time, json


TODOS = []

# Screen Funtions #
def all_view(stdscr):
    stdscr.refresh()
    y, x = stdscr.getmaxyx()

    todos = []

    if len(TODOS) < 1:
        todos = load(0)
    else:
        todos = TODOS
    
    height = int(len(todos) * 4)
    to_y = y // 25
    to_x = x // 50


    win = curses.newwin(height, 50, to_y, to_x)
    win.clear()
 
    for i in range(0, len(todos)):
        TODOS.append(todos[i])
        win.addstr(f" [ - ]: {todos[i]}\n")
    
    win.border()
    win.refresh()
    del win

def add_todo(stdscr):
    y, x = stdscr.getmaxyx()

    to_y = y // 10
    to_x = x // 10

    win = curses.newwin(50, 100, to_y, to_x)
    win.erase()
    
    curses.echo(True)
    win.addstr(1, 2, "Input todo: ")
    
    inpt = win.getstr(2, 2, 2000)

    win.border()
    win.refresh()

    curses.echo(False)
    return inpt

# \\ MAIN FUNCTION // #
def main(stdscr):
   
    stdscr = curses.initscr()
    
    while True:
        stdscr.clear()
        stdscr.refresh()
    

        all_view(stdscr)
        stdscr.refresh()

        key = stdscr.getkey()

        if key == 'q' or key == 'Q':
            break
        elif key == 'a' or key == 'A':
            inp = str(add_todo(stdscr)).replace("b", "").replace("'", "")
            TODOS.append(inp)
        else:
            continue



# JSON load and deload functions #
def load(mode): 

    if mode == 0:
        with open("data.json", "r") as f:
            data = json.load(f)
            data = data["todos"]
    else:
         with open("data.json", "r") as f:
            data = json.load(f)
            data = data["done"]

    return data










if __name__ == "__main__":    curses.wrapper(main)
