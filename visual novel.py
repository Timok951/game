import getpass
karma = 0
food = {"сыр", "пицца", "паста"}
user = getpass.getuser()

info = {"имя":user, "карма": karma} 

def read():
	userinput = input("ввод:")
	return userinput

def deathbullet():
	print("Пуля попала в вас. Вы упали и понял, что двигаться не можете, ваше сознание затихает.")

def deathbite():  
	print("Вас укусили, это конец, неважно что будет дальше.")

def write():
	print(karma)
	numbers = [1,2,3,4, 5]
	for i in numbers:
		print(numbers[i-1])

def end():
	print (f"{info}, {karma}, спасибо за прохождение этой прекрасной игры.")
	read()

while karma <= 0 and read() != "!":

	try:
		print("Вы проснулись в своей кровати")
		read()
		print("Вы встали \nСегодня у вас очень важно дело нужно занять место умершого сотрудника.")
		read()
		print("Ладно, так как вы работаете в IT компании надо захватить ноутбук.\nЧто выберите 1-метро или 2-автобус.")

		if (read() == "1"):
			print("Поездка прошла спокойно. За исключением толкучки, которая была меньше обычного.")
			info["выбор 1"] = 1

		else:
			print("Было на удивление не так много людей. Были видны кареты скорой помощи и полицейские машины\nПод конец какие-то люди в камуфляже, с автоматами, начали бежать за какое-то здание\nНа остановке вы спросили устаого полицейского в чём дело. Тот ответил что кто-то безобразничает в городе и он бы сегодня не выходил бы на работу.")
			karma = karma + 1
			info["выбор 1"] = 2
				
		print(f"Вы вошли в оффис, поздоровавшись с довольно нервным охранником.\nСев за свой стол вы увидели надпись \"{user}\" И начали работать.")
		read()
		print(f"День был напряженным, работа тоже что-то совсем не клеилось. Код вечно ломался. Вам бдыло дано меню,{food}, требовалось настроить ии что-бы он сумел правильно различать эти продукты \n 1-Продолжите или 2-сделаете перерыв ?")

		if (read() == "1"):
			food.add("сырники, блины")
			print(f"Получилось нормально.{food}. Ну, пора немного отдохнуть.")
			karma = karma + 1
			info["выбор 2"] = 1

		else:
			print("Ну и правльно, может быть свежий вохдух вас успокоит.")
			info["выбор 2"] = 2

		print("Вы вышли на веранду и поняли что дела не очень. Над вами пролетел Вертолёт. А рядом был клуб дыма. Ладно, осталось чуть-чуть, доработать и домой.")
		print("Вы сели за свой компьютер, зашибись. Теперь сервер начал выдавать дичь.")
		write()
		print("Ладно и не такое случалось. Но можно пойти 1-домой 2-либо спростить у совего коллеги. ")

		if (read() == "1"): 
			print("Вы подошли к своему коллеге, Майку, он был бледен.")
			read()
			print("Вы спросили что с ним. Он указал на женщину, которая лежала на полу.")
			read()
			print("Одна из сотрудниц. Видимо ей плохо.")
			karma = karma + 1
			info["выбор 3"] = 1

		else:
			info["выбор 3"] = 2
			print("Возможно так и надо, не нужно быть особо умным что бы догадаться, сегодня день не очень.")
			read()
			print("Нужно взять такси, добраться до дома, а там видно будет.")
			read()
			print("Вы увидели лежащию женищину на полу, вохможно её плохо.")

		print("Нужно что-то делать. 1-Помочь, 2-Вызвать помощь")

		if (read() == "1"): 
			info["выбор 4"] = 1
			print("Вы подошли к женщине. Пульса не было")
			read()
			print("Дыхания тоже не было. Значит нежно его сделать.")
			read()
			print("Вы решаете сделать искусственное дахание")
			read()
			print("Видимо вы до сих пор не поняли что происходить. Женщина оживает и кусает вас.")
			break
			deathbite()

		else:
			info["выбор 4"] = 2
			print("Сказав Майку, что у вас нет нужных навыков вы решаете позвать на помощь.")
			read()
			print("Мак подождал минуту и сказал: Погоди, я понял что это.")
			read()
			print("Майк: Я позвоню в скорую, там должны знать что делать.")

		print("Кто-то начинает кричать и раздаётся взрыв.")
		read()
		pritn("Толпа:А-а-а-а")
		read()
		pritn("Майк: Хороший сегодня денёк, что взорвалось то ? Час от часу не легче.")
		read()
		print("Майк:Бэкапы на диск, нет...")
		read()
		print("Майк: Слушай, бэкапы копируй на диск и вытаскивай его как можно быстрее. Жду тебя у входа, повезу к себе домой.")
		read()
		print("Вы: Так точно")
		read()
		print("На вашем правом пути к компьютеру встаёт женщина, а на левом толпа, что выберете ? Правый-1 или Левый-2")

		if (read() == "1" ):
			info["выбор 5"] = 1
			print("Вы перепрыгиваете женщину и бежите к компьютеру.")
			read()

		else:
			info["выбор 5"] = 2
			print("В толпе вы замечаете охраника, вы хотите ему что-то скзать, но его перепуганное лицо заставляет вас не говорить.")
			read()
			print("Вы поднимаете к нему руки, слашите выстрел.")
			read()
			print("выходит у него был пистолет и вы его чем-то напугали. Наверное это был просто несчастный случай, но пуле это не обьяснишь.")
			read()
			deathbullet()
			break

		print("Подбежва к своему компьютеру вы сохраняете свой проэкт.")
		read()
		print("К вам кто-то идёт, нельзя отвлекаться.")
		read()
		print("Вы открыли крышку корпуса.")
		read()
		print("Шерк, шерк....")
		read()
		print("Раз провод, два провод")
		read()
		print("Шерк, у-у-у-у-у-у")
		read()
		print("Вы видите ту самую женщину.Вот только с глазами что-то не так....")
		read()
		print("Они как у Акулы....как будто она вас хочет съесть, нет...")
		read()
		print("Она уже вас есть, кажись уже кем-то закусила. Рот весь в крови.")
		read()
		print("Нужно что-то делать....соображай")
		read()
		print("Кинуть жестким диском в тварь -1, Отступить и найти альтернативу-2")

		if(read() == "1"): 
			info["выбор 6"] = 1
			print("Вы кидаете в тварь жестким диском, она теряет ранвовесие.")
			read()
			print("Вы бежите черз неё")
			read()
		else:
			info["выбор 6"] = 2
			karma = karma + 1
			print("Нет, вы справитесь и так. Слишком дорогая цена")
			read()
			print("Вы отступаете, но под руку ничего не попадаеться.")
			read()
			print("Но тут в тварь что-то попадет и она теряет ранвовесие")
			read()
			pritn("Вы бежите и не оглядываетесь.")

		print("Тут вы натыкаетесь на Майка. Оказываеться он вас ждал.")
		read()
		print("Майк: Сторож охранник совсем слетел, стреляет во всё.")
		read()
		print("Майк: Сваливаем, у меня в гараже машина. Старьё, но едет.")
		read()
		print("Вы слишите вытрелы")
		read()
		print("Через несколько секунд вы бежите с майком к лифтам.")
		read()
		print("Майк: Что будем использовать 1-лифт или 2-лестницу ?")

		if(read == "1"): 
			info["выбор 7"] = 1
			print("Вы забегаете в лифт.")
			read()
			print("До закрытия дверей успевают ещё несколько работников-везунчики.")
			read()
			print("Вы спокойно доезжаете до нижнего этажа, Но там вас ожидает толпа монстров, которая не даёт вам выйти из лифта.")
			deathbite()
			break

		else:
			info["выбор 7"] = 2
			print("Вы решаете бежать по лестнице.")
			read()
			print("Раз пролёт, два пролёт.")
			read()
			print("Четрые, восемь.")
			read()
			print("Справа тварь, не останавливаться.")
			read()
			print("Вы тяжело дашите, Майк тоже. Нуно бежать осталось немного.")
			read()

		print("Вы на паркове, но тут их ещё больше, чем на лестнице")
		read()
		pritn("Вы бежите к машине. Надо отрыть двери.")
		read()
		print("Майк их быстро открывает. Вы заваливаетесь в машину. Майк проворачивет ключ.")
		read()
		print("Машина тарахтит и заводиться, вы раскидываете тварей и выезжате.")
		read()
		pritn("Майк: знаешь, я думаю жёсткие диски были не так выжны....")
		read()
		print("Вы: Да, мы почти погибли, я думал навсегда на лестнице останусь.")
		read()
		print("Ваш диалог прерывает радио")
		read()
		print("Радио:BZzzzzt, this is emergency broadcast...")
		read()
		print("Майк: не знал что всё настолько серьёзно, думаю будет эвакуация....")
		read()
		print("Майк:хотя куда и кто отличит заражённых от здровых ?")
		read()
		print("Вы: согласен..., но возможно это что-то")
		read()
		print("Майк:Ладно, надо узнать что скажут")
		read()
		print("Радио: the extaraction point for strict \"Finewood\" in the park \"Biglake\" ")
		read()
		print("Нам туда, отлично, с учётом что творится на улицах, там должет быть блокпост и вертолёты.")
		read()

		if (karma < 1):
			print("Я согласен, гони.")
			read()
			print("Майк: понял. Военные лучше чем эти красавцы.")
			read()
			print("Мимо вас проносилсь дома, обедающие твари, очаги сопротивления, стреляющая полиция")
			read()
			print("Кто-то кидал молотовы в тварей, а кто-то кинул в машину, благо Майк быстро увернулся.")
			read()
			print("Через час вы были в точке эвакуцации.")
			read()
			print("Это место был хорошо заметно каждую секунду оттду стартовали вертолёты.")
			read()
			print("Вас оглядели с головы до пят и отправили в вертолёт")
			read()
			prin("Через минуту в иилюминаторе показался город, полыхаюший огнём")
			break

		else:
			print("Вы: нет, я лучше останусь")
			read()
			print("Майк: Да ты спятил")
			read()
			print("Вы: нет, это как раз мудрое решение")
			read()
			print("Майк: как хочешь, но я эвакуируюсь")
			read()
			print("Вы вышли из машины, а перед вами был дивный новый мир.")
			read()
			pritn("Насколько это было возможно")
			read()
			pritn("Вы пошли по шоссе, а перед вами открывался город охваченный огнём")
			break


	except:
		print("Произошла ошибка")
		read()
		print("Перезапустите приложение")
end()