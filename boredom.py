#!python3.6
#名前を伺い年齢入力で来年の年齢を表示する
print("Hello Python")
print('what is your name?')
my_name = input()
print('It is good to meet you,' + my_name)
print('The length of your name is:')
print('what is your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')