# -*- coding: utf-8 -*-
from pycobot import Handler

class example:
    def __init__(self, bot):
        pass
    
    @Handler("welcome")
    def testcommand(self, bot, cli, ev):
        print("PO TA TO ES")
        print(_("WOOOOOOOOOOOOO IT WOORKS"))
