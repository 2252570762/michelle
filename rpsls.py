#coding=gbk
"""
ʯͷ����������ʷ������Ϸ����
���ߣ�������
"""


def name_to_number(choice_name):
	if choice_name=="ʯͷ":# 0 - ʯͷ
		return 0
	if choice_name=="ʷ����":# 1 - ʷ����
		return 1
	if choice_name=="ֽ":# 2 - ֽ
		return 2
	if choice_name=="����":# 3 - ����
		return 3
	if choice_name=="����":# 4 - ����
		return 4
		
def number_to_name(comp_number):
	if comp_number==0:
		return "ʯͷ"
	if comp_number==1:
		return "ʷ����"
	if comp_number==2:
		return "ֽ"
	if comp_number==3:
		return "����"
	if comp_number==4:
		return "����"


    
def rpsls(player_choice):
	print("�������ѡ����:",computer_number)
	if comp_number==player_choice_number:
		print("���ͼ��������һ����")
	if comp_number==0 and player_choice_number==4:
		print("����Ӯ��")
	if comp_number==0 and player_choice_number==3:
		print("����Ӯ��")
	if comp_number==1 and player_choice_number==0: 
		print("����Ӯ��")
	if comp_number==1 and player_choice_number==4:
		print("����Ӯ��")
	if comp_number==2 and player_choice_number==0:
		print("����Ӯ��")
	if comp_number==2 and player_choice_number==1:
		print("����Ӯ��")
	if comp_number==3 and player_choice_number==1: 
		print("����Ӯ��")
	if comp_number==3 and player_choice_number==2: 
		print("����Ӯ��")
	if comp_number==4 and player_choice_number==2:
		print("����Ӯ��")
	if comp_number==4 and player_choice_number==3:
		print("����Ӯ��")
	if comp_number==4 and player_choice_number==0:
		print("��Ӯ�ˣ�")
	if comp_number==3 and player_choice_number==0:
		print("��Ӯ�ˣ�")
	if comp_number==0 and player_choice_number==1:
		print("��Ӯ�ˣ�")
	if comp_number==4 and player_choice_number==1:
		print("��Ӯ�ˣ�")
	if comp_number==0 and player_choice_number==2:
		print("��Ӯ�ˣ�")
	if comp_number==1 and player_choice_number==2:
		print("��Ӯ�ˣ�")
	if comp_number==1 and player_choice_number==3:
		print("��Ӯ�ˣ�")
	if comp_number==2 and player_choice_number==3:
		print("��Ӯ�ˣ�")
	if comp_number==2 and player_choice_number==4:
		print("��Ӯ�ˣ�")
	if comp_number==3 and player_choice_number==4:
		print("��Ӯ�ˣ�")



import random
comp_number=random.randint(0,5)
   
   
    
# ���"-------- "���зָ�
# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_numbercomp_number
# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
# ����Ļ����ʾ�����ѡ����������
# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
player_choice_number=name_to_number(choice_name)
computer_number=number_to_name(comp_number)


if choice_name in ["ʯͷ","ʷ����","ֽ","����","����"]:
	rpsls(choice_name)
else:
	print("Error: No Correct Name")






