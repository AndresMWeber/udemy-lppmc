



# menu = []
# menu.append(["eggs", "spam", "suassage"])
# menu.append(["eggs", "eggs", "suassage"])
# menu.append(["eggs", "spam", "spam"])
# menu.append(["eggs", "spam", "eggs"])
# menu.append(["suassage", "spam", "suassage"])
#
#
#
# for meal in menu:
#     if not "spam" in meal:
#        for ingredients in meal:
#            print(ingredients)
#
#
#
#
#

# quote = input("hej hopp skriv vad du vill så räknar jag ut procenten vokaler och konsonanter :)")
# konsonant = 0
# vokal = 0
# antal = 0
# procentVokal = 0
# procentkonsonant = 0
#
# for i in quote:
#     if i in "qwrtpdfgklvbnm":
#         konsonant += 1
#         antal += 1
#
#     if i in "eyuioaåäö":
#         vokal += 1
#         antal += 1
#
#
# procentVokal = (antal/vokal)*10
# procentkonsonant = (antal/konsonant)*10
# # procentVokal = round(procentVokal)
# # procentkonsonant = round(procentkonsonant)
#
# print("Det finns {0} konsonanter i meningen och {1} volkaler" .format(konsonant, vokal))
# print(" {0} procent av bokstäverna är vokaler" .format(procentVokal))
# print(" {0} procent av bokstäverna är konsonanter" .format(procentkonsonant))

# print(list("flkwmnfksnsefs"))


# even = [2, 4, 6, 8]
# odd =[1, 3, 5, 7]
# number = [even, odd]
#
# for numberSet in number:
#     for value in numberSet:
#             print(value)


menu = []
menu.append(["eggs", "spam", "suassage"])
menu.append(["eggs", "eggs", "suassage"])
menu.append(["eggs", "spam", "spam"])
menu.append(["eggs", "spam", "eggs"])
menu.append(["suassage", "spam", "suassage"])
menu.append(["suassage", "banana", "suassage"])

mealNr = 0
for meal in menu:
    if not "spam"  in meal:
        mealNr += 1

        if mealNr == 1:
            print(" \nmeal one \n")

        if mealNr == 2:
                print(" \nmeal two \n")


        for ingridients in meal:
            print(ingridients)

choice = input("do you like meal one or two?")



if choice == "1":
    print("eggs eggs and suassage then :)")
elif choice == "2":
    print("alright here's the banana")
else:
    print("get out")



