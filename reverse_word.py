#Hi everyone! 
#Here we get a word or sentence from user to change it to it's reverse.abs

user=input("Enter a word/sentence to be reversed: ")

def reverse(word, text=[]):
    for i in range (len(word)-1,-1,-1):
       text.append(word[i])

    return "".join(text)
print("Your reversed text is: {}".format(reverse(user)))

