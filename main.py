import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

todo_list = [
    "Hello",
    "There",
    "XD INIT"
]

def todo_view(stdscr):
    stdscr.clear()
    for i in range(0, len(todo_list)):
        stdscr.addstr(f"[ - ]: {todo_list[i]}\n")
    stdscr.refresh()

def get_input(stdscr):

    inp = curses.newwin(8,55, 0,0)
    inp.addstr(1,1, "TODO:")
    
    sub = inp.subwin(3, 41, 2, 1)
    sub.border()

    sub2 = sub.subwin(1, 40, 3, 2)
    tb = Textbox(sub2)

    inp.refresh()
    tb.edit()
    text = tb.gather().strip().replace('\n', '')

    if text[len(text) - 1] == "x":
        text = text[:-1]


    return text






def main(stdscr):
    
    while True:
        stdscr.refresh()

        todo_view(stdscr)

        pressed_key = chr(stdscr.getch())
        
        if pressed_key == 'a':
            inp = get_input(stdscr)
            todo_list.append(inp)
        elif pressed_key == 'q':
            break 
        else:
            continue

wrapper(main)
