from pyfiglet import Figlet
import sys
try:
    f = Figlet(font=str(sys.argv[1]))
except Exception as e:
    print(e)
    exit()
asc = f.renderText(str(sys.argv[2]))
# print(type(asc))
# print(asc)
# import pprint
# pprint.pprint(asc)
# pprint.pprint(asc.split('\n'))
from time import sleep
for line in asc.split('\n'):
    print(line)
    sleep(0.8)