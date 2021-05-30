from AbstractClasses import *
from ClassDef import *
from TypeDef import *


# 자식 클래스
class Controller(Publisher):
    token = None
    packet = None

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    def didSubmit(self):
        pass

    def destroyUInfo(self):
        pass

    def destroyM(self):
        pass

    def destroyU(self):
        pass

    def doRegister(self, p: Packet):

        pass

    def prompt(self):
        pass

    # 토큰 설정하기
    def set_token(self, t: Token):
        self.token = t


# 자식 클래스
class UserControl(Subscriber):
    def receive(self):
        pass

    def enterUserInfo(self, u: UserInfo):
        pass


# 자식 클래스
class Combiner(Decorator):
    def activate(self):
        pass

    def combine(self, u: Combined):
        pass


class Analyzer(Decorator):
    def activate(self):
        pass

    def analyze(self, an: Analyzed):
        pass


class ERC721Standard(Decorator):
    def activate(self):
        pass

    def buildPacket(self, p: Packet):
        # p에 있는 정보들이 유효한지 검사한다.
        if p._information.isSafe() and p._analyzedResult.isSafe() and p._approvedDegree.isSafe() and p._isApproved:
            return p
        else:
            return None

    def approveForAll(self, controller: Controller):
        pass

    def register(self):
        pass
