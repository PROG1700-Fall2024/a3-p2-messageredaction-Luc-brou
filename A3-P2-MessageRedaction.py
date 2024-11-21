#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:W0489720     
#Student Name:Luc Brousseau  

def stop(user_input):
    if user_input.lower() == "quit":
        print("\nEnding program...")
        print("Ended.")
        exit()  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    print("Hello! This program will remove certain characters from a word.")
    print("Type quit at any point to end the program.")

    while True:

        character_del=[] #creates empty list for characters to delete to go inside of

        word=input("\nInput a word. ")

        stop(word) #calls function which checks if user wants to stop program

        numC= (input("How many characters are you going to delete? "))

        if not numC.isdigit():
            print("\nPlease enter a valid amount of characters to delete.")
            return

        stop(numC) #calls function which checks if user wants to stop program

        if numC.isdigit():
            numChars=int(numC)
            if numChars <= 0:
                print("\nPlease enter a valid amount of characters to delete.")
                return

        for counter in range(numChars):
        
            delete=input("\nInput the character you would like to delete. ")
            stop(delete) #calls function which checks if user wants to stop program
            character_del.append(delete) #adds characters to delete into a list
        
        stop(word) #calls function which checks if user wants to stop program

        new_word = word
        for char in character_del:
            new_word = new_word.replace(char, "_").replace(char.upper(), "_").replace(char.lower(), "_")

        print (f"\nCharacters removed: {(character_del)}") 
        print (f"Charcters removed: {len(character_del)}") 
        print(f"New word: {new_word}") #prints new word with removed letters


    # YOUR CODE ENDS HERE

main()