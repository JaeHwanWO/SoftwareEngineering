import jellyfish

class LyricsAnalyzer:
    def __init__(self):
        self.origin=""              #처리할 음원
        self.db=""                  #db내 음원
        self.originLyrics=[]        #처리할 음원 가사 파싱 후 저장할 리스트
        self.dbLyrics=[]            #db내 음원 가사 파싱 후 저장할 리스트
        self.simularities=[]        #파싱한 가사들의 유사도 저장할 리스트

    def parser(self,str):
        result=[]
        result=str.split('.')       #가사를 온점으로 구분하여 파싱
        return result      

    def analyze(self, strOrigin,strDb):
        self.origin=strOrigin       
        self.db=strDb               
        self.originLyrics=self.parser(self.origin)
        self.dbLyrics=self.parser(self.db)
        for i in self.originLyrics:
            for j in self.dbLyrics:
                self.simularities.append(jellyfish.jaro_distance(i,j))
        simularity=self.returnResult()
        print(simularity)
        return simularity
    
    def returnResult(self):
        sum=0
        for i in self.simularities:
            sum+=i
        return (sum)/len(self.simularities)



a="hello.my name.is.quardbitch"

b="good.nice.is.quardbeach"

analyzer=LyricsAnalyzer()
analyzer.analyze(a,b)


