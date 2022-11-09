#14.1.2  定义父类 User 和继承类 Vip
#User 类
#- 属性：id: str，nickname: str，credits: int
#- 方法：get_info()，打印用户的所有信息；upgrade_to_vip()，将用户修改为 Vip 类型
#Vip 类
#- 属性：父类全部属性、vip_level: int=1
#- 方法：get_info()，打印用户的所有信息；
class User:
    def __init__(self, id:str, nickname:str, credits:int):
        self.id = id
        self.nickname = nickname
        self.credits = credits

    def get_info(self):
        print(self.id, self.nickname, self.credits)

    def upgrade_to_vip(self):
        self=Vip()
        del self


class Vip(User):

    def __init__(self, vip_level:int=1):
        super().__init__()
        self.vip_level = vip_level

    def get_info(self):
        super().get_info()
        print(self.vip_level)

a=User("1","2",3)
a.upgrade_to_vip()


