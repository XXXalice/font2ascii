import curses
import time

def main(stdscr):
    stdscr.clear()
    for i in range(50):
        stdscr.addstr(1, 1, '##')
        stdscr.refresh()
        time.sleep(0.5)
    stdscr.getkey()


if __name__ == '__main__':
    curses.wrapper(main)