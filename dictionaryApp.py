import json
from difflib import get_close_matches


data=json.load(open("data.json"))

def meaning(word):
    word=word.lower()
    close_matches=get_close_matches(word,data.keys())

    if word in data:
        return data[word]
    elif(len(close_matches)>0):
        print("Did you mean %s instead?Enter Y for yes or N for No:" %close_matches[0])
        d=input()
        if(d=='Y' or d=='y'):
            return data[close_matches[0]]
        elif(d=='N' or d=='n'):
            return "Try again!"
        else:
            return "We didn't get you Buddy!"

    else:
        return "The word doesn't exist.Please double check it."

stop=False
while(not stop):
    user_entry=input("Enter the word:")
    output=meaning(user_entry)
    if(type(output)==list):
        for res in output:
            print(res)
    else:
        print(output)

    c=input("Do you want to search more.Enter Y for Yes and N for No:")
    if(c=='Y' or c=='y'):
        stop=False
    elif(c=='N' or c=='n'):
        stop=True
    else:
        print("Invalid Entry")
        break
