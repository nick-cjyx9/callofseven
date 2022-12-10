class event_handler:
    '''
    事件触发器
    '''
    def __init__(self) -> None:
        self.observers=[]
        self.name=""
    def notify(self,name):
        for i in self.observers:
            if i.name==name:
                i.broadcast()
    def attach(self,obs):
        self.observers.append(obs)
    def detach(self):
        return self.observers.pop()

class observer:
    '''
    观察者(事件)
    '''
    def __init__(self) -> None:
        self.actions=[]
        self.name=""
    def attach(self,act):
        self.actions.append(act)
    def detach(self):
        return self.actions.pop()
    def broadcast(self):
        for action in self.actions:
            action()
    
class Game:
    def __init__(self) -> None:
        self.players=[]
        self.event_handlers=[]
        