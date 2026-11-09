# # Ticket Checker
# ticket = (input("Do you have a ticket (True/False): "))


# if ticket.upper() == "TRUE":
#     ticket = True
# elif ticket.upper() == "FALSE":
#     ticket = False

# if ticket:
#     print("You have a ticket")
# else:
#     print("You do not have a ticket")


########### AGE ###############
name = input("Enter your Name: ")
birthDate = int(input("Enter your date of birth: "))
age = 2026 - birthDate

if 40 < age < 60:
    print("You are a senior citizen")
elif age < 12: 
    print("You are still in primary school,", name)
elif age < 16:
    print("You are still in secondary school,", name)
elif age < 20:
    print("You are still in Singapore Poly,", name)
elif age < 22:
    print("You are in National Service,", name)
elif age < 30:
    print("You are in University,", name)
else:
    print("You are an adult,", name)
