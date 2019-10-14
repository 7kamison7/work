#7
# 文字列をFloatまたはIntegerに変換する．入力文字：”246.2458”
a = "246.2458"
print(type(a))
print(a)

b = float(a)                #intに変換するため  floatには必要なし
print(type(float(a)))
print(a)

c = int(b)                  #小数点付きの文字列ではfloat→intと2回変換が必要
print(type(int(c)))
print(c)