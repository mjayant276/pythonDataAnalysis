'''
Example of gaming 
gaming (Top level directory or folder)
games & admin

gaming/ 
    __init__.py -- initialization file

    games/ --subpackage
       __init__.py   
       askgame.py
       playgame.py
       scoregame.py
    admin/ -- subpackage
       __init__.py
       users.py
       managegames.py    

'''
from gaming.games import askgame as ag
from gaming.admin.managegames import *


if __name__ == '__main__':
    ag.whichgame('F1-Racing')
    addgame('F2_Racing')
    