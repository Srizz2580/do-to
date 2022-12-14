import curses
import json, time

menu = []

# PRINT
def print_todo(stdscr, menu, selected_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) + idx

        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.border()
    stdscr.refresh()

# ADD
def add_todo(stdscr):
    h, w = stdscr.getmaxyx()
    
    x = (w // 2) - 30
    y = (h // 2) - 5

    curses.echo(True)

    win = curses.newwin(10, 60, y, x)
    win.refresh()
    
    
    win.border()
    win.refresh()
    
    win.addstr(2, 2, "Add a todo: ", curses.A_UNDERLINE)
    
    win.addstr(4, 2, ">>", curses.A_BOLD)
    
    win.refresh()
    inp = win.getstr(4, 5, 2000)

    curses.echo(False)
    if str(inp) == "b''": return
    else: return inp

# DELETE
def del_todo(stdscr, menu, selected_idx):
    stdscr.refresh()
    
    for idx, row in enumerate(menu):
        if idx == selected_idx:
            menu.pop(idx)
    
    stdscr.refresh()
    print_todo(stdscr, menu, 0)



# SAVE
def save_todo(stdscr):
    stdscr.clear()
    
    h, w = stdscr.getmaxyx()
    text = "Adding data to data.json ..."

    x = w // 2 - len(text) // 2
    y = h // 2

    stdscr.addstr(y, x, text, curses.A_BOLD)
    stdscr.refresh()

    time.sleep(2)

    dictionary = {"todos": menu}

    with open('./data/data.json', 'w') as f:
        json.dump(dictionary, f)
    
    stdscr.clear()
    print_todo(stdscr, menu, 0)

# LOAD
def load_todo(stdscr):
    global menu

    stdscr.clear()

    h, w = stdscr.getmaxyx()
    text = "Loading data from data.json ..."

    x = w // 2 - len(text) // 2
    y = h // 2

    stdscr.addstr(y, x, text, curses.A_BOLD)
    stdscr.refresh()

    time.sleep(2)
    with open('./data/data.json', 'r') as f:
        data = json.load(f)
        
    menu = data["todos"]


# EDIT
def edit_todo(stdscr, selected_row):
    global menu

    for idx, row in enumerate(menu):
        if idx == selected_row:
            stdscr.clear()
            h, w = stdscr.getmaxyx()

            x = (w // 2) - 30
            y = (h // 2) - 5

            curses.echo(True)

            win = curses.newwin(10, 60, y, x)
            win.refresh()


            win.border()
            win.refresh()

            win.addstr(2, 2, "Edit the todo: ", curses.A_UNDERLINE)

            win.addstr(4, 2, "+>", curses.A_BOLD)

            win.refresh()
            inp = win.getstr(4, 5, 2000)

            curses.echo(False)
            if str(inp) == "b''": return

            else: 
                xd = str(inp)
                xd = xd[2:-1].strip()
                if xd != "n":
                    menu.pop(idx)
                    menu.insert(idx, xd)

                    stdscr.refresh()

                else: return


# // MAIN // #
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    h, w = stdscr.getmaxyx()
    text = "Press 'l' for help. Press 'Enter' to continue."
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text, curses.A_BOLD)
    key = stdscr.getch()
    if chr(key) == 'l' or chr(key) == 'L': load_todo(stdscr)

    curr_row = 0

    while True:

        stdscr.clear()

        print_todo(stdscr, menu, curr_row)
        stdscr.refresh()

        key = stdscr.getch()
        
        if key == curses.KEY_UP: curr_row -= 1
        elif key == curses.KEY_DOWN: curr_row += 1

        if curr_row < 0 or curr_row > len(menu) - 1: curr_row = 0

        # Main functions #
        if chr(key) == 'q' or chr(key) == 'Q': break
        if chr(key) == 'a' or chr(key) == 'A':
            inp = str(add_todo(stdscr))
            
            inp = inp[2:-1].strip()
            if inp != "n": menu.append(inp) 

        if chr(key) == 'd' or chr(key) == 'D': del_todo(stdscr, menu, curr_row)
        if chr(key) == 's' or chr(key) == 'S': save_todo(stdscr)
        if chr(key) == 'l' or chr(key) == 'L': load_todo(stdscr)
        if chr(key) == 'e' or chr(key) == 'E': edit_todo(stdscr, curr_row)

curses.wrapper(main)
