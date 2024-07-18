#%% 주소록 검색 메소드
class AdderssBook:
    def search(self):
        print("===주소록검색===")
        name = input("찾을 이름")
        if not name :
            print("입력된 이름이 없음")
            return
        exist =False
        for person in self.address_list:
            if name == person.name:
                person.info()
                exist=True
        if not exist:
            print("{}의 정보가 없다".format(name))