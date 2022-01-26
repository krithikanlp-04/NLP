import re
import random       
import responses                                        # predefined module for response generation
import language_Translator_functions as lang_functions  # module with translator functions 

'''
                    *********************DOC STRING for the chatbot *************
                    Author: Krithika B
                    Date: 29/12/2020
                    
This program contains the menu driven options and chatbot functionalities for interacting with the users. The chatbot interacts with the user seeking
inputs on the menu options. Once selected, each option is handled by a separate function defined in the module lang_functions. The program is highly modular
and users can easily add more menu options
The program and all other referred modules do not use any inbuilt NLP libraries or dictionaries. All complex functionalities are done using python commands and
user defined functions. Regular expressions, format functions, unicode manipulation etc are used to perform the various operations.


The main goal of this project is to create a rule-based Chatbot code named "JABBERWOCKY" which interacts with the user through greetings, questions and menu driven
functionalities. The user is prompted to enter their input at different checkpoints, and JABBERWOCKY gets ready to play different language games in the style of but not
similar to pig latin. The main inspiration for these language games come from different sources.
                    Resources: The Cat's Elbow and other secret languages - Book by Alvin Schwarz
                             : The Name game - pop music creation by Shirley Ellis
                             
                    **************************************************************
'''


# The bot asks the user to choose between different language games and helps translate text based on well defined functions

dict_lang={
           "1":"UbbiDubbi",
           "2":"King_Tut",
           "3":"The_NameGame",
           }

x=""
def intro(x):     # This function generates a mini text about the choice selected by the user. For example when the user selects UbbiDubbi, the function
                  # generates a text instructing the user on the conversion process. 
    print("You've selected ", dict_lang[x],"1. Would you like to read how this language works --Press 1\n2. Would you like to Translate text --Press 2")
    nxt=input()
    if nxt=="1":
        filename=dict_lang[x]
        instr = open(f"{filename}.txt", "r")
        test = instr.read();
        instr.close()
        print("\nThe secret language ",dict_lang[x]," works like this: \n", test)
        
    return 1
            

def chat_JB(name_user,x,y):   # Generic Chat_Bot function. Asks for the user's name and generates different responses before asking for user input on menu options
        print(x.format(random.choice(responses.generic_intro)))
        print("\n"+ responses.langs)
        return 0
    
print(random.choice(responses.generic_hello))
name_user=input()

x= '{} '+ name_user
y= x+' {}'
ch=chat_JB(name_user,x,y)        

while True:
    if ch==-1:
        z=random.choice(responses.generic_bye)
        print(x.format(z))
        break
    elif ch==0:
        print("\n"+ responses.choice_main)
        ch_new=input()
        if ch_new=="3":
            ch=-1
            continue
        elif ch_new=="2":
            print("In this section Jabber will morpho-analyze a short story in Tamil. Some Morphology and Some moral science :) ")
            print("Select a character to proceed: \n1. Lion\n2. Tortoise")
            num_story=input()
            ch=lang_functions.Story(num_story)

        else:
            print("\n"+ "Select a game from below: \n",responses.choice_sub)
            ch_new=input()
            
            ch=lang_functions.func(intro,ch_new)
            if ch==1:
                if ch_new=="1":
                    ch=lang_functions.UbbiDubbi(1)
                elif ch_new=="2":
                    ch=lang_functions.King_Tut(1)
                else:
                    ch=lang_functions.The_NameGame(1)


    
    else:
        print("\n"+ responses.choice_sub)
            
        ch_new=input()
            
        ch=lang_functions.func(intro,ch_new)
        if ch==1:
             if ch_new=="1":
                ch=lang_functions.UbbiDubbi(1)
             elif ch_new=="2":
                 ch=lang_functions.King_Tut(1)
             else:
                 ch=lang_functions.The_NameGame(1)
