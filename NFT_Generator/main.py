from ExtendedClasses import *

# controller instance 생성
myController = Controller()

# 사용자가 Community 모델의 코드를 통해 register 이전의 과정 마쳤다고 가정
# 사용자 정보 가정하기
userInfo = UserInfo(userName="Yejin", userEmail="oipivigui@cau.ac.kr.", isValidUser=True)
audio = Audio(file="https://www.youtube.com/watch?v=c7ZxSTxfScA")
combined = Combined(userInfo=userInfo, rawMusic=audio, musicAddress="https://www.youtube.com/watch?v=c7ZxSTxfScA")

# 사용자가 Analyzer 모델의 코드를 통해 analyze 마쳤다고 가정
analyzedResult = Analyzed(["유사도 0%", "유사도 3%", "유사도 2%"])

# 패킷 생성 됨
p = Packet(information=combined, analyedResult=analyzedResult, approvedDegree=100, isApproved=True)

# 패킷 등록하기
myController.doRegister(p)

# 블록체인에서 승인결과 받아서 controller에 등록하기
standard = ERC721Standard()
standard.approveForAll(controller=myController)

