'''
实验目标：RPSLS游戏。
班级：土木3班
作者：陈和轩
'''
import random
print("欢迎使用RPSLS游戏")
print("----------------")
guess_list = ["剪刀", "布", "石头","蜥蜴","史波克"]#限定输入内容
win_combination = [["布", "石头"or"史波克"], ["石头", "剪刀"or"蜥蜴"], ["剪刀", "布"or"蜥蜴"],["蜥蜴","史波克"or"纸"],["史波克","纸"or"石头"]]#设置游戏规则
while True:
    computer = random.choice(guess_list)#限定计算机随机内容
    people = input('请输入：石头,剪刀,布,史波克，蜥蜴\n')#玩家输入
    print("您的选择为", people)
    print("计算机的选择为", computer)
    if people not in guess_list:#玩家输入指定范围外元素显示错误
        print("Error: No Correct Name")
    elif computer == people:#玩家与电脑输入相同，平局说明
        print("您和计算机出的一样呢！")
    elif [computer, people]:
        print("计算机赢了！")
    else:
        print("您赢了！")
