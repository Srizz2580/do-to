import curses
import time, json

 # Screen Funtions #
def all_view(stdscr):
    y, x = stdscr.getmaxyx()

    todo_win = curses.newwin(100, 50, 50, 50)
    # done_win = curses.newwin(curses.LINES, curses.COLS)

    todo_win.border()
    # done_win.border()

    todos = load(0)
    done = load(1)

    for i in range(0, len(todos)):
        todo_win.addstr(f"[ - ]: {todos[i]}\n")

    # for i in range(0, len(done)):
        # done_win.addstr(f"[ X ]: {done[i]}\n")
    stdscr.border() 
    todo_win.refresh()
    # done_win.refresh()


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
