#(4) input，print，変数の 3 つだけで借金返済計画を立てるプログラムを作りたい．
# 簡単のため，利子は無しとする．まず，借金の総額と，ひと月に返済する金額を入力すると，
# 返済にかかる年数を表示し，さらに，毎年のボーナスから返済する金額を入力すると，
# 返済完了が何年早まるかを表示し，その次に返済を完了したい年数を入力すると，
# ボーナスからいくら返せばよいかを表示するプログラムを作成せよ．
import math
num=0
year2=0
x=input('借金の総額：')
y=input('1ヶ月の返済する金額：')



num= int(x)/int(y)
year=(num/12)
month=(float(year)-int(year))*12
if math.ceil(month)==12:
    year+=1
    month=0

print('%d年%dヶ月で返済完了します'%(year,math.ceil(month)))

print('毎年のボーナス')
bonus=input()
year2= int(x)/(int(y)*12+int(bonus))
year2 = year-year2
month2=(float(year2)-int(year2))*12
if math.ceil(month)==12:
    year+=1
    month=0

print('%d年%dヶ月早まります'%(year2,math.ceil(month2)))
#if month < month2:
#    year-=1
#    month+=12
#year3=year-year2
#month3=month-month2
#print('最短で%d年%dヶ月で返済可能です'%(year3,month3))

print('希望の返済年数を入力してください')
year4=int(input('年'))
month4= int(input('月'))
amari=(int(x)-int(y)*(12*year4+month4))/year4   #ボーナスで返す残り金額
if int(bonus) > int(amari):
    print('ボーナスで毎年%d円支払うと%d年%dヶ月で返済可能です'%(amari,year4,month4))
else:
    print('あなたのボーナスでは希望返済年数では返済できません')
