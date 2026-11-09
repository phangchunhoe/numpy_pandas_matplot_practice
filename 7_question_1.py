class ProfileTools:
    def findAge(birthDate):
        return 2026 - birthDate

    def convertFarenheit(celsius):
        return celsius * 9 / 5 + 32

    def addTax(original):
        return original * 1.07



# Test 
print(ProfileTools.findAge(2007))
print(ProfileTools.convertFarenheit(20))
print(f"${ProfileTools.addTax(100)}")