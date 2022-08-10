import curses

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
    
    win.addstr(2, 2, "Add a todo: ")
    win.refresh()
    inp = win.getstr(4, 2, 2000)

    curses.echo(False)

    return str(inp)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    curr_row = 0

    while True:

        stdscr.clear()

        print_todo(stdscr, menu, curr_row)
        stdscr.refresh() 
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            curr_row -= 1
        elif key == curses.KEY_DOWN:
            curr_row += 1

        if curr_row < 0 or curr_row > len(menu) - 1: curr_row = 0

        # Main functions #
        if chr(key) == 'q' or chr(key) == 'Q': break
        if chr(key) == 'a' or chr(key) == 'A': 
            inp = str(add_todo(stdscr))
            inp = inp[2:-1]

            menu.append(inp)

curses.wrapper(main)
