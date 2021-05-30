from TypeDef import *


class UserInfo:
    def __init__(self, userName: str, userEmail: str, isValidUser: bool):
        self._userName = userName
        self._userEmail = userEmail
        self._isValidUser = isValidUser

    @property
    def userName(self):
        return self._userName

    @property
    def userEmail(self):
        return self._userEmail

    @property
    def isValidUser(self):
        return self._isValidUser


class Combined:
    def __init__(self, userInfo: UserInfo, rawMusic: Audio, musicAddress: str):
        self._userInfo = userInfo
        self._rawMusic = rawMusic
        self._musicAddress = musicAddress

    def isSafe(self):
        # userInfo 확인하기
        if not self._userInfo.userName.isascii():
            raise Exception("유저 이름이 유효하지 않습니다.")

        if not self._userInfo.userEmail.isValidEmail():
            raise Exception("이메일이 유효하지 않습니다.")

        if not self._userInfo.isValidUser:
            raise Exception("유저 정보가 유효하지 않습니다.")

        # rawMusic 확인하기
        if not self._rawMusic.file.count() > 0:
            raise Exception("rawMusic이 유효하지 않습니다.")

        # musicAddress 확인하기


class Analyzed:
    def __init__(self, result: [str]):
        self._result = result


class Packet:
    def __init__(self, information: Combined, analyedResult: Analyzed, approvedDegree: int, isApproved: bool):
        self._information = information
        self._analyzedResult = analyedResult
        self._approvedDegree = approvedDegree
        self._isApproved = isApproved
