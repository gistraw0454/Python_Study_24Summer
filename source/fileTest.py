#%% file test
name_file = open("names.txt","a")
name_file.write("write\n")
name_file.close()

name_file = open("names.txt","r")
for i in name_file.readlines():
    print(i,end="")