import configparser
import time
config = configparser.ConfigParser()
print("Welcome to the Setup!")
print("\n")
print("First the program needs to know the order of your characters in the "
      "choose screen in Valorant! Go to this screen and setup the program!")
time.sleep(8)
print("\n")
print("Pay Attention! The order will change if you buy a new character! To "
      "change the order, simply run setup.exe again!")
time.sleep(8)
print("\n")
print("These are the number. Every number stands for a character!")
print("1  = Brimstone")
print("2  = Cypher")
print("3  = Jett")
print("4  = Omen")
print("5  = Phoenix")
print("6  = Sage")
print("7  = Sova")
print("8  = Breach")
print("9  = Killjoy")
print("10 = Raze")
print("11 = Reyna")
print("12 = Viper")

time.sleep(0.5)
time.sleep(1)


order1 = input("Who is you first character?[enter the number from above]")
order2 = input("Who is you second character?[enter the number from above]")
order3 = input("Who is you third character?[enter the number from above]")
order4 = input("Who is you fourth character?[enter the number from above]")
order5 = input("Who is you fifth character?[enter the number from above]")
order6 = input("Who is you sixth character?[enter the number from above]")
order7 = input("Who is you seventh character?[enter the number from above]")
order8 = input("Who is you eighth character?[enter the number from above]")
order9 = input("Who is you ninth character?[enter the number from above]")
order10 = input("Who is you tenth character?[enter the number from above]")
order11= input("Who is you eleventh character?[enter the number from above]")
order12 = input("Who is you twelfth character?[enter the number from above]")


config['main'] = {'1': order1,
                        '2': order2,
                        '3': order3,
                        '4': order4,
                        '5': order5,
                        '6': order6,
                        '7': order7,
                        '8': order8,
                        '9': order9,
                        '10': order10,
                        '11': order11,
                        '12': order12}

configfile = open('config.ini', 'w')
config.write(configfile)

exit()
