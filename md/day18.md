# 18�� - �÷��� - list2
### list ���
dataList=[1,2,3]
- �� �ֱ� 
    - �߰� `dataList.append(4)`
        - [1,2,3,4]
    - ���� `dataList.insert(�ε�����ȣ,��) `
        - dataList.insert(1,1.5)
        - [1,1.5,2,3]
- �� ����
    - `dataList.remove(��)`
        - [1,2,3,4].remove(1)
        - [2,3,4] : �ش簪 ����
        - �ߺ��� �¿��� �� �������� ���� ���� ���� ���� �ε����� �����´�.

    - `del dataList[�ε�����ȣ]`
        - del dataList[1]
        -[1,3] : �ش� �ε��� �� ����

    - `dataList.clear()`
        - ��� �� ����
- �� �˻�
    - `dataList.index(��)`
        - dataList.index(3)
        - 2 : �ش簪�� �ε��� ���� ����
        - �ߺ��� �¿��� �� �������� ���� ���� ���� ���� �ε����� �����´�.
- �� ����
    - `dataList[�ε�����ȣ] = ���ο`
    - dataList[0]=10
    - [10,2,3]

### for �� ���
- 0, ?, 1 �� ��밡��
```
for i in range(len(list��)):
    list��[i]
```
- ���� for�� (���� for��, forEach ��)
    ```
    for i in list��:
        i 
    ```
    - list���ִ� ������ ��Ұ� i�� ����

### ���� ���� Ȯ��
- �� in list�� : ���ǽ�(�� �Ǵ� ������ ��) list�ȿ� ���� ������ True
- �� not in list�� : list�ȿ� ���� ������ True
