import curses
import sys
from pyfiglet import Figlet

class RenderAscii():

    def __init__(self):
        self.stdscr = curses.initscr()

    def ascii_main(self):
        self.stdscr.clear()
        self.stdscr.addstr('hello')
        self.stdscr.refresh()
        self.stdscr.getkey()

def main():
    aa = RenderAscii()
    aa.ascii_main()

if __name__ == '__main__':
    main()