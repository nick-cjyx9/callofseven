import random
import card.characters as chrs
DEBUGMODE=True
# 控制游戏流程
class Game:
    def __init__(self):
        self.players=[]
        self.event_handlers=[]
    def add_player(self,*playerl):
        for player in playerl:
            self.players.append(player)

    def add_npc(self):
        pass


class Player:
    def __init__(self,*chars):
        #角色卡
        self.char_cards=chars
        #前台角色卡
        self.front_char=None
        #action卡卡堆
        self.action_cards=[]
        #是否已宣告回合结束
        self.isend=False
    def choose_front(self,user_input):
        if self.char_cards[user_input].isdead:
            return -1
        else:
            self.front_char=self.char_cards[user_input]

class Observer:
    def __init__(self):
        self.actions=[]
    def notify(self):
        for action in self.actions:
            action()
    def attach(self,action):
        self.actions.append(action)
    def detach(self)->int:
        return self.actions.pop()

class Damage:
    def __init__(self,sender,tgt,type):
        self.sender=sender
        self.tgt=tgt
        self.type=type
    def caculate(self):
        
        

if (__name__=='__main__') and DEBUGMODE:
    #init
    gpc=Game()
    ply1,ply2=Player()
    gpc.add_player(ply1,ply2)
    #start
