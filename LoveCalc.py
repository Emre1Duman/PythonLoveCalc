# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combined_names = name1.lower() + name2.lower()

x = 0
x += combined_names.count("t")
x += combined_names.count("r")
x += combined_names.count("u")
x += combined_names.count("e")

y = 0
y += combined_names.count("l")
y += combined_names.count("o")
y += combined_names.count("v")
y += combined_names.count("e")

love_score_str = str(x) + str(y)

love_score = int(love_score_str)

print(love_score)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 or love_score <= 50:
    print(f"your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")





