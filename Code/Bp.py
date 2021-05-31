class Bp:
    def __init__(self,limit=50,genre=50):
        self.limit=limit
        self.genrePercent=genre
    
    def getLimit(self):
        return self.limit
    
    def getGenrePercent(self):
        return self.genrePercent