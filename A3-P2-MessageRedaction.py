#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    print("Hello! This program will remove certain characters from a word. Input letters separated by commas.")

    new_word=""
    character_del=[]

    word=input("\nInput a word. ")
    delete=input("Input the characters you would like to delete. ")
    character_del.append(delete.lower())

    print(character_del)


    for char in character_del:
        new_word = word.replace(character_del, "_")
    
    character_del = delete.split(",")

    if word.lower()=="stop":
        print("\nEnding program...")
        print("Ended.")
        return
    
    print (new_word)


    # YOUR CODE ENDS HERE

main()