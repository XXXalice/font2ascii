import curses
import sys
import time
import math
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
        Test.__init__(self)
        #self.stdscr = curses.initscr() #ダメ
        #コンストラクタでinitscrを実行してしまうとターミナルがバグる（知識不足のため原因究明不可）


    def ascii_main(self, preformatted_aa, mode='static'):

        def _print_static(aa):
            out = '\n'.join(aa[0])
            return out

        def _print_animation(aa, num=math.inf):
            # outs = []
            # for i in aa:
            #     out = '\n'.join(i)
            #     print(out)
            #     outs.append(out)
            outs = ['\n'.join(i) for i in aa]

            return outs

        PRINT_FUNC = {
            'static': lambda aa: _print_static(aa),
            'animation': lambda aa: _print_animation(aa)
        }

        self.stdscr = curses.initscr() #ここでやれ！
        curses.noecho()
        self.stdscr.clear()
        try:
            out = PRINT_FUNC[mode](preformatted_aa)
            if type(out) is list:
                try:
                    while True:
                        for aa in out:
                            self.stdscr.clear()
                            self.stdscr.addstr(aa)
                            self.stdscr.refresh()
                            time.sleep(0.1)
                except Exception as e:

                    curses.nocbreak()
                    curses.echo()
                    self.stdscr.keypad(False)
                    curses.endwin()
                    print(e)
                    exit(0)
            else:
                self.stdscr.addstr('none')
                self.stdscr.refresh()
                self.stdscr.getkey()
        except Exception as e:
            pass
        finally:
            curses.nocbreak()
            curses.echo()
            self.stdscr.keypad(False)
            curses.endwin()
            exit(0)

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
        # Test.test_show_pprint(self, self.rendered_aa_container)

        def _preform_aa(rendered_aa):
            super_container = []
            for aa in rendered_aa:
                container = []
                for line in aa.split('\n'):
                    container.append(line)
                super_container.append(container)
            return super_container

        self.preformatted_aa = _preform_aa(self.rendered_aa_container)
        return self.preformatted_aa

    def test_show(self, item):
        Test.test_show_pprint(self, item)


def main():
    aa = RenderAscii()
    target = 'Syamu'
    preformatted_aa = aa.get_ascii_art(target, 'standard', 'block', 'slant', 'catwalk')
    # aa.test_show(preformatted_aa)
    aa.ascii_main(preformatted_aa, mode='animation')


if __name__ == '__main__':
    main()