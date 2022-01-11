#改行を取り除く場合print()の命令にオプションを渡す
#カンマで区切って『end=""』とすると、末尾に何も追加しないという意味
print("Your name? ", end="")
name = input()

print("hello %s" %name)
print("hello %s again!" %name)