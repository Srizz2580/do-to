import curses
import time, json

 # Screen Funtions #

def todo_view(stdscr):
    data = load(0)

    for i in range(0, len(data)):
        stdscr.addstr(f" [ - ]: {data[i]}\n")   



# \\ MAIN FUNCTION // #
def main(stdscr):
   
    stdscr = curses.initscr()
    
    while True:
        stdscr.clear()
        stdscr.refresh()

        todo_view(stdscr)   

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
















if __name__ == "__main__":
    curses.wrapper(main)
