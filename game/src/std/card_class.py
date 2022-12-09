#卡牌类
class Buff:
    def __init__(self):
        self.name=""
    def effect(self):
        pass

class CharCard:
    def __init__(self) -> None:
        self.name=""
        self.skills=[]
        self.element_type=""
        self.hp=10
        self.isdead=False
        self.weapon=""
        #身上的元素类型
        self.elements=[""]
        #盾/支援buff=后台减伤buff/武器
        self.buffs=[]

        self.belong_to=[""]
        self.cover_img=r""
        self.type="Character"
    def be_damaged(self,num):
        if self.hp-num>0:
            self.hp-=num
        else:
            # 宣告死亡
            self.isdead=True

class WeaponCard(Buff):
    def __init__(self):
        self.__init__()
        self.name=""
        self.type=""
        self.activate=[]
        # self.activate=["charDamage","afterSkill"]
        # 前台攻击,技能后