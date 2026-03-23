"""
An Insurance company follows following rules to calculate premium.
    - If a person's health is excellent and the person is between 25 and 35 years of age and lives in a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.
    - If a person satisfies all the above conditions except that the sex is female then the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
    - If a person's health is poor and the person is between 25 and 35 years of age and lives in a village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
    - In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and maximum amount for which he/she can be insured.
"""

age = int(input("Enter your age: "))

if age >= 25 and age <= 35:
    health = input("Enter your health (excellent or poor): ")
    
    if health == "excellent":
        place = input("Enter your place: (city or village): ")
        
        if place == "city":
            gender = input("Enter your gender (M or F): ")
            
            if gender == "M":
                print("You are eligible for insurance.")
                print("Policy amount cannot exceed Rs. 2 lakhs.")
                amount = int(input("Enter your amount: "))

                if amount < 200000:
                    print("Your premium is", (amount * 4) // 1000)
                else:
                    print("Your amount limit exceeded")
            else:
                print("You are eligible for insurance.")
                print("Policy amount cannot exceed Rs. 1 lakhs.")
                amount = int(input("Enter your amount: "))

                if amount < 100000:
                    print("Your premium is", (amount * 3) // 1000)
                else:
                    print("Your amount limit exceeded")
        else:
            print("You are not eligible for insurance")
    else:
        place = input("Enter your place: (city or village): ")
        
        if place == "city":
            print("You are not eligible for insurance")
        else:
            gender = input("Enter your gender (M or F): ")
            
            if gender == "M":
                print("You are eligible for insurance.")
                print("Policy amount cannot exceed Rs. 10,000.")
                amount = int(input("Enter your amount: "))

                if amount < 10000:
                    print("Your premium is", (amount * 6) // 1000)
                else:
                    print("Your amount limit exceeded")
            else:
                print("You are not eligible for insurance")
else:
    print("You are not eligible for insurance")
