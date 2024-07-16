# 20°­ - listżÍ tuple,dict
- mutable (şŻÇŇźöŔÖ´Â) : list
- immutable (şŻÇŇźöžř´Â) : tuple
```py
#%% mutable
dataList1=[1,2,3]
dataList2=dataList1

dataList2.append(4)
print(dataList1)
# dataList2¸Ś šŮ˛ĺ´ÂľĽ dataList1żĄľľ żľÇâo

#%% immutable
dataTuple1 = (1,2,3)
# print(type(dataTuple1))
dataTuple2 = dataTuple1
dataTuple2 +=4,5

print(dataTuple1)
#dataTuple2¸Ś šŮ˛ĺ´ÂľĽ dataTuple1żĄ żľÇâx
#ŔÖ´ÂľĽŔĚĹÍ¸Ś °ĄÁŽżŔ´Â ¸ńŔű, °Ëťö ¸ńŔű, şŻ°ćx
# dataTuple1[0]=10 ĆŠÇĂŔÇ °ŞŔş şŻ°ć ÇŇ źö žř´Ů.
```
## Dict
- ÇŃ˝ÖŔ¸ˇÎ ŔúŔĺľÇžî °ü¸Ž
- len()Ŕť ťçżëÇĎ¸é ÇŃ˝ÖŔť 1ˇÎ ÄŤżîĆŽ
- Ĺ°°ŞŔş ÁßşšľÉźö žřŔ¸¸ç, °ŞŔş ÁßşšŔĚ °Ą´ÉÇĎ´Ů
- Ĺ° °ŞŔť ÁÖ¸é ą× Ĺ°ŔÇ ÂŚ˛á °ŞŔť °ĄÁö°í żÂ´Ů

###  DIct źąžđ
```
dict ¸í = {Ĺ°:°Ş,Ĺ°:°Ş,...}
```
### Dict ťçżë
- Ăß°Ą (Ĺ°°ŞŔĚ žřŔť ś§)
    - `dict¸í[Ĺ°] =°Ş`
- źöÁ¤ (Ĺ°°ŞŔĚ ŔÖŔť ś§)
    - `dict¸í[Ĺ°] =`
- ťčÁŚ (ÇŃ˝ÖŔĚ ťčÁŚľČ´Ů)
    - `del dict¸í[Ĺ°]`
- °Ëťö
    - `Ĺ° in dict¸í` : Ĺ° °ŞŔĚ ŔÖŔ¸¸é Âü
    - `Ĺ° not in dict¸í` : Ĺ° °ŞŔĚ žřŔ¸¸é Âü

### KEY şĐ¸Ž
- list(dict¸í.keys())
### VALUE şĐ¸Ž
- dict¸í.values()