#name=input("Hey what's your name?")

#def sayHelloToUser(name):
    #print("Hello, ", name)
    #print("I'm glad you're a part of SIP")
    #print("sorry about the bugs")

#sayHelloToUser(name)


loved_ones = {}
loved_ones["Mom"] = 42
loved_ones["Dad"] = 48
loved_ones["Sister"] = 10
loved_ones["Darshna"] = 16
loved_ones["Hana"] = 16
loved_ones["Nimsangh"] = 16
print(loved_ones)


personal_info = {}
personal_info["age"] = 16
personal_info["colleges I visited"] = ["MIT", "NYU", "Columbia", "Harvard", "Princeton", "BU"]
personal_info["fav food"] = "dumplings"
print(personal_info)


print(personal_info["fav food"])
print(personal_info["colleges I visited"][1])
print("Sirasa at age " + str(loved_ones["Sister"]) + " visited " +personal_info["colleges I visited"][0])


info = {}
info["age"] = input("What's your age?")
info["colleges you like"] = input("What colleges have you visited?")
print(info)