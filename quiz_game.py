
print ("Welcome to mini data quiz game. ")

playing= input ("Are you ready to start our exciting quiz game? ")

score= 0;
if playing.lower() != "yes":
    quit()

print ("Okay, than let's start it! ")

answer1 = input("How many vowle letters are there in English language? ")
if answer1=="5":
    print("correct ! ")
    score+=1
else:
    print("Incorrect, there are 5.")

answer2= input("what is the first vowle letter in English language? ")
if answer2.lower()=="a":
    print("correct ! ")
    score+=1
else:
    print("Incorrect, it is 'a' .")

answer3= input("Are w and y semivowle letters in English language? ")
if answer3.lower()=="yes":
    print("correct ! ")
    score+=1
else:
    print("Incorrect, yes  they are .")

answer4= input("What are the subject pronouns in English language? ")
if answer4.lower()=="i,she, he, it, they, we, you " or "i,she, he, they, it,we, you ":
    print("correct ! ")
    score+=1
else:
    print("Incorrect, They are: i,she, he, it, they, we, you .")

answer5= input("How many letters are there in English language? ")
if answer5=="26":
    print("correct ! ")
    score+=1
else:
    print("Incorrect, there are 26 letters.")

print( f"You got {score} from correct answers")