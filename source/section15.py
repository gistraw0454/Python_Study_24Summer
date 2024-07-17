#%% 1 책이름 저자 class로 출력하기
class Book:
    def set_info(self,title,author):
        self.title=title
        self.author = author

    def print_info(self):
        print("책제목: "+self.title)
        print("책저자: "+self.author)
book1 = Book()
book2 = Book()

book1.set_info("파이썬","민경태")
book2.set_info("어린왕자","생텍쥐페리")

book1.print_info()
book2.print_info()

#%% 2 시간 계산하기
class Watch:
    def set_time(self):
        now = input("시간을 입력하세요")
        hms= now.split(":")
        self.hour = int(hms[0])
        self.minute = int(hms[1])
        self.second = int(hms[2])

    def add_hour(self,hour):
        if hour<=0:
            return
        self.hour +=hour
        self.hour %=24
    
    def add_minute(self,minute):
        if minute<=0:
            return
        self.minute +=minute
        self.add_hour(self.minute//60)
        self.minute %=60

    def add_second(self,second):
        if second<=0:
            return
        self.second +=second
        self.add_minute(self.second//60)
        self.second %=60

    def see(self):
        print("시간은:\n")
        print("{}시 {}분 {}초".format(self.hour,self.minute,self.second))
    
w = Watch()
w.set_time()
w.add_hour(10)
w.add_minute(70)
w.see()

#%% 3 가수 이름 계산하기
class Song:
    def set_song(self,title,genre):
        self.title=title
        self.genre=genre
    def print_song(self):
        print("노래제목: {}({})".format(self.title,self.genre))
class Singer:
    def set_singer(self,name):
        self.name = name
    def hit_song(self,song):
        self.song = song
    
    def print_singer(self):
        print("가수이름: {}".format(self.name))
        self.song.print_song()
    
song = Song()
song.set_song("나비야","동요")
singer = Singer()
singer.set_singer("어린이")
singer.hit_song(song)
singer.print_singer()