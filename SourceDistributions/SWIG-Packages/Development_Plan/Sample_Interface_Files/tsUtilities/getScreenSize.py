import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

cols = curses.COLS
rows = curses.LINES

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()

print('Screen Size (X = %d cols; Y = %d rows)' % (cols, rows))
