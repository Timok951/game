def read():
	userinput = input("input:")
	return userinput
try:
	print("Вы проснулись в своей кровати")
	read()
	print("Вы встали")
except:
	print("an error has accured")