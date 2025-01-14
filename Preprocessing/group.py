import os
from random import random

image_dir="../../FER/FER"
list_dir="../../FER/lists"
list_emotion = ["anger", "contempt", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

if os.path.exists(list_dir) is False:
    os.makedirs(list_dir)

# def age_to_group(age):
#     if age<=20:
#         return 0
#     elif age>20 and age<=30:
#         return 1
#     elif age>30 and age<=40:
#         return 2
#     elif age>40 and age<=50:
#         return 3
#     elif age>50:
#         return 4

train_txt=[]
test_txt=[]
train_emo_group0=[]
train_emo_group1=[]
train_emo_group2=[]
train_emo_group3=[]
train_emo_group4=[]
train_emo_group5=[]
train_emo_group6=[]
train_emo_group7=[]
test_emo_group0=[]
test_emo_group1=[]
test_emo_group2=[]
test_emo_group3=[]
test_emo_group4=[]
test_emo_group5=[]
test_emo_group6=[]
test_emo_group7=[]

for idx, emo in enumerate(list_emotion):
    for filename in os.listdir(os.path.join(image_dir, emo)):
        # age=int(filename.split('_')[0])
        group=idx
        strline = filename + ' %d\n' % group
        if random()<0.9:
            if group==0:
                train_emo_group0.append(strline)
            elif group==1:
                train_emo_group1.append(strline)
            elif group==2:
                train_emo_group2.append(strline)
            elif group==3:
                train_emo_group3.append(strline)
            elif group==4:
                train_emo_group4.append(strline)
            elif group==5:
                train_emo_group5.append(strline)
            elif group==6:
                train_emo_group6.append(strline)
            elif group==7:
                train_emo_group7.append(strline)
            train_txt.append(strline)
        else:
            if group==0:
                test_emo_group0.append(strline)
            elif group==1:
                test_emo_group1.append(strline)
            elif group==2:
                test_emo_group2.append(strline)
            elif group==3:
                test_emo_group3.append(strline)
            elif group==4:
                test_emo_group4.append(strline)
            elif group==5:
                test_emo_group5.append(strline)
            elif group==6:
                test_emo_group6.append(strline)
            elif group==7:
                test_emo_group7.append(strline)
            test_txt.append(strline)

print(len(train_txt))
print(len(test_txt))    
print(len(train_emo_group0))
print(len(train_emo_group1))
print(len(train_emo_group2))
print(len(train_emo_group3))
print(len(train_emo_group4))
print(len(train_emo_group5))
print(len(train_emo_group6))
print(len(train_emo_group7))
print(len(test_emo_group0))
print(len(test_emo_group1))
print(len(test_emo_group2))
print(len(test_emo_group3))
print(len(test_emo_group4))
print(len(test_emo_group5))
print(len(test_emo_group6))
print(len(test_emo_group7))

# with open(list_dir + '/train_emo_group_0.txt','w') as f:
#     f.writelines(train_emo_group0)

# with open(list_dir + '/train_emo_group_1.txt','w') as f:
#     f.writelines(train_emo_group1)

# with open(list_dir + '/train_emo_group_2.txt','w') as f:
#     f.writelines(train_emo_group2)

# with open(list_dir + '/train_emo_group_3.txt','w') as f:
#     f.writelines(train_emo_group3)

# with open(list_dir + '/train_emo_group_4.txt','w') as f:
#     f.writelines(train_emo_group4)

# with open(list_dir + '/train_emo_group_5.txt','w') as f:
#     f.writelines(train_emo_group5)

# with open(list_dir + '/train_emo_group_6.txt','w') as f:
#     f.writelines(train_emo_group6)

# with open(list_dir + '/train_emo_group_7.txt','w') as f:
#     f.writelines(train_emo_group7)

# with open(list_dir + '/train.txt','w') as f:
#     f.writelines(train_txt)

# with open(list_dir + '/test_emo_group_0.txt','w') as f:
#     f.writelines(test_emo_group0)

# with open(list_dir + '/test_emo_group_1.txt','w') as f:
#     f.writelines(train_emo_group1)

# with open(list_dir + '/test_emo_group_2.txt','w') as f:
#     f.writelines(train_emo_group2)

# with open(list_dir + '/test_emo_group_3.txt','w') as f:
#     f.writelines(train_emo_group3)

# with open(list_dir + '/test_emo_group_4.txt','w') as f:
#     f.writelines(test_emo_group4)   

# with open(list_dir + '/test_emo_group_5.txt','w') as f:
#     f.writelines(test_emo_group5)

# with open(list_dir + '/test_emo_group_6.txt','w') as f:
#     f.writelines(test_emo_group6)

# with open(list_dir + '/test_emo_group_7.txt','w') as f:
#     f.writelines(test_emo_group7)

# with open(list_dir + '/test.txt','w') as f:
#     f.writelines(test_txt)