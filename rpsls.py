#coding=gbk
"""
石头剪刀布蜥蜴史波克游戏设置
作者：赖垚旭
"""


def name_to_number(choice_name):
	if choice_name=="石头":# 0 - 石头
		return 0
	if choice_name=="史波克":# 1 - 史波克
		return 1
	if choice_name=="纸":# 2 - 纸
		return 2
	if choice_name=="蜥蜴":# 3 - 蜥蜴
		return 3
	if choice_name=="剪刀":# 4 - 剪刀
		return 4
		
def number_to_name(comp_number):
	if comp_number==0:
		return "石头"
	if comp_number==1:
		return "史波克"
	if comp_number==2:
		return "纸"
	if comp_number==3:
		return "蜥蜴"
	if comp_number==4:
		return "剪刀"


    
def rpsls(player_choice):
	print("计算机的选择是:",computer_number)
	if comp_number==player_choice_number:
		print("您和计算机出的一样呢")
	if comp_number==0 and player_choice_number==4:
		print("机器赢了")
	if comp_number==0 and player_choice_number==3:
		print("机器赢了")
	if comp_number==1 and player_choice_number==0: 
		print("机器赢了")
	if comp_number==1 and player_choice_number==4:
		print("机器赢了")
	if comp_number==2 and player_choice_number==0:
		print("机器赢了")
	if comp_number==2 and player_choice_number==1:
		print("机器赢了")
	if comp_number==3 and player_choice_number==1: 
		print("机器赢了")
	if comp_number==3 and player_choice_number==2: 
		print("机器赢了")
	if comp_number==4 and player_choice_number==2:
		print("机器赢了")
	if comp_number==4 and player_choice_number==3:
		print("机器赢了")
	if comp_number==4 and player_choice_number==0:
		print("您赢了！")
	if comp_number==3 and player_choice_number==0:
		print("您赢了！")
	if comp_number==0 and player_choice_number==1:
		print("您赢了！")
	if comp_number==4 and player_choice_number==1:
		print("您赢了！")
	if comp_number==0 and player_choice_number==2:
		print("您赢了！")
	if comp_number==1 and player_choice_number==2:
		print("您赢了！")
	if comp_number==1 and player_choice_number==3:
		print("您赢了！")
	if comp_number==2 and player_choice_number==3:
		print("您赢了！")
	if comp_number==2 and player_choice_number==4:
		print("您赢了！")
	if comp_number==3 and player_choice_number==4:
		print("您赢了！")



import random
comp_number=random.randint(0,5)
   
   
    
# 输出"-------- "进行分割
# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_numbercomp_number
# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
# 在屏幕上显示计算机选择的随机对象
# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
player_choice_number=name_to_number(choice_name)
computer_number=number_to_name(comp_number)


if choice_name in ["石头","史波克","纸","蜥蜴","剪刀"]:
	rpsls(choice_name)
else:
	print("Error: No Correct Name")






