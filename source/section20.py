#%% �ּҷ� �˻� �޼ҵ�
class AdderssBook:
    def search(self):
        print("===�ּҷϰ˻�===")
        name = input("ã�� �̸�")
        if not name :
            print("�Էµ� �̸��� ����")
            return
        exist =False
        for person in self.address_list:
            if name == person.name:
                person.info()
                exist=True
        if not exist:
            print("{}�� ������ ����".format(name))