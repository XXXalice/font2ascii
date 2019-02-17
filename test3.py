import curses
import sys
from pyfiglet import Figlet


class Test():
    def __init__(self):
        self.notify_messages = {
        'init':
"""

[test_notify]
Test enabled.

""",

        'pprint':
"""
        
[test_notify]
Execute pprint.
            
"""}
        print(self.notify_messages['init'])

    def test_show_pprint(self, item):
        print(self.notify_messages['pprint'])
        import pprint
        pprint.pprint(item)


class RenderAscii(Test):

    def __init__(self):
        # Test.__init__(self)
        self.stdscr = curses.initscr()

    def ascii_main(self):
        self.stdscr.clear()
        self.stdscr.addstr('hello')
        self.stdscr.refresh()
        self.stdscr.getkey()

    def get_ascii_art(self, title, *args_font):
        self.aa_container = []
        for font in args_font:
            try:
                self.aa_container.append(Figlet(font=font))
            except:
                continue
        print('generated {} figlets.'.format(len(self.aa_container)))
        self.rendered_aa_container = []
        for figlet in self.aa_container:
            self.rendered_aa_container.append(figlet.renderText(str(title)))
        # Test.test_show_pprint(self.rendered_aa_container)



def main():
    aa = RenderAscii()
    # aa.ascii_main()
    target = 'KANE NENDAWA.'
    aa.get_ascii_art(target, 'standard', 'slant')

if __name__ == '__main__':
    main()