### Love Calculator


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


t = "t"
r = "r"
u = "u"
e = "e"

l = "l"
o = "o"
v = "v"
e = "e"

total_true = name1.lower().count(t)+ name1.lower().count(r)+ name1.lower().count(u)+ name1.lower().count(e)+ name2.lower().count(t)+ name2.lower().count(r)+ name2.lower().count(u)+ name2.lower().count(e)
 

total_love = name1.lower().count(l)+ name1.lower().count(o)+ name1.lower().count(v)+ name1.lower().count(e)+ name2.lower().count(l)+ name2.lower().count(o)+ name2.lower().count(v)+ name2.lower().count(e)

Love_Score = int(str(total_true)+str(total_love))

# Love_Score = int(score_as_string)

if Love_Score <10 or Love_Score >90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")

elif Love_Score >=40 and Love_Score <=50:
    print(f"Your score is {Love_Score}, you are alright together.")

else:
    print(f"Your score is {Love_Score}.")

print("p")

