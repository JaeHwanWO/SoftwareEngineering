import Bp
import LyricsAnalyzer
import glob

class Result:
    def init(self,input):
        self.lyricFiles = glob.glob('/Users/82109/db/*.txt')        #가사파일이 저장되어있는 경로
        self.lyrics=[]                                              #저장되어 있는 음원들의 가사 파싱한것 저장
        self.resultList=[]                                          #임계치 이상인 것들 저장
        self.input=input                                            #사용자가 입력한 가사

    def fetchLyrics(self):
        for file_name in self.lyricFiles:
            f= open(file_name, 'r')
            lst=[]                                          #곡 하나에 대한 가사 문장별 저장 리스트
            for line in f:
                line.strip()                                #저장되어 있는 가사파일 들의 공백제거 
                line = line.replace("\n" ,'')
                line = line.replace("//" , '')
                lst.append(line)                            #공백 제거한 가사들을 문장 별로 lst에 저장
            f.close()
            self.lyrics.append(lst)                         #문장별로 파싱한 리스트lst를 각각의 노래별로 리스트에 저장 (2차원) 
        return self.lyrics

    def compareMusic(self):
        lyricsAnalyzer= LyricsAnalyzer.LyricsAnalyzer()
        bp=Bp.Bp()                                          #임계치 받아오기 위해 bp객체생성

        self.fetchLyrics()
        inputParser=[]
        inputParser=self.input.split('\n')                  #사용자가 제공한 가사들 개행별로 파싱
        limit=bp.getLimit()                                 #Bp에서 제공하는 임계치 

        for lyric in self.lyrics:
            analysis=lyricsAnalyzer.analyze(inputParser,lyric)
            if analysis>=limit:                             #임계치 보다 높은것만 resultList에 저장
                self.resultList.append(analysis)
        return self.resultList
