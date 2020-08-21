import configparser
config = configparser.ConfigParser()

print("Welcome to the Agent Select!")
print("\n")
print("Choose YOUR Agent")
print("\n")
print("These are the numbers. Every number stands for an agent!")
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

agent = input("Which agent do you want to play? [enter a number]")

config['agent'] = {'selected': agent}

configfile = open('config.ini', 'a')
config.write(configfile)
