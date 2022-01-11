# 条件を追加してみよう
#!python3.7

# import random

# answer = random.randint(1, 10)

# print("Your guess? ", end="")
# guess = int(input())

# if answer == guess:
#     print("Bingo!")
# elif answer > guess:
#     print("Bigger!")
# else:
#     print("Smaller!")

# print("[Answer: %i]" %answer)

#  ループ処理を使ってみよう

# import random

# answer = random.randint(1, 10)

# while True:
#     print("Your guess? ", end="")
#     guess = int(input())
    
#     if answer == guess:
#         print("Bingo!")
#         break
#     elif answer > guess:
#         print("Bigger!")
#     else:
#         print("Smaller!")

# 正解までの回数を表示しよう

import random

answer = random.randint(1, 10)
count = 0

while True:
    print("Your guess? ", end="")
    guess = int(input())
    # count = count + 1
    count += 1
    
    if answer == guess:
        print("Bingo! It took %i guesses!" %count)
        break
    elif answer > guess:
        print("Bigger!")
    else:
        print("Smaller!")