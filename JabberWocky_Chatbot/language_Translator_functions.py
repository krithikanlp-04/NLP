import re,sys
import re
import responses
import tamil_stemmer

dict_tut = ["A","BUB","CUT","DUD","E","FUF","GUG","HUSH","I","JUG","KUD","LUL",
            "MUM","NUN","O","PUP","Q","RUR","SUS","TUT","U","VUV","WUV",
            "X","YUT","ZUZ"]

printo_lines="\n\nJabberwocky is working its magic. Please wait!\n Please enter a word or sentence or copy paste any text to translate into {}.\nPress 0 to exit translator and go back to language menu.\nPress 00 to exit and go back to main menu\n"

def King_Tut(x):
    print(printo_lines.format("King_Tut"))

    while True:
        myDict={}   
        print("\n Your input: ")
        word_t=input()
        
        if word_t=="0":
            ch=1
            break
        elif re.search("^"+"00",word_t):
            ch=0
            break
        
        else:
            
            
            word_t=word_t.lower()  
            # TUT IS A SUBSTITUTION CIPHER. SO EVERY LETTER OF THE ALPHABET CORRESPONDS TO A SOUND.
            unic="\\" + "u006"

            a=1 # corresponds to "a" Unicode letters go from a-z "\u0061 - \u007A"
            
            word_kat=word_t
            while a<10:
                as_str=str(a)
                alpha=unic+as_str
                
                word_kat=re.sub(alpha,dict_tut[a-1],word_kat)
                a+=1
            
            str1="ABCDEF"
            for b in str1:
                alpha=unic+b
                word_kat=re.sub(alpha,dict_tut[a-1],word_kat)
                a+=1
            
            unic="\\" + "u007"
            d=0
            while d<10:
                as_str=str(d)
                alpha=unic+as_str
                word_kat=re.sub(alpha,dict_tut[a+d-1],word_kat)
                d+=1
            b="A"
            alpha=unic+b
            word_kat=re.sub(alpha,dict_tut[a+d-1],word_kat)
            

            print("The Tutnese translation for",word_t," is:",word_kat)
                
    return ch



def UbbiDubbi(x):
    print(printo_lines.format("UbbiDubbi"))

    while True:
        myDict={}   
        print("\n Your input..")
        word_t=input()
        
        if re.search("^"+ "0$",word_t):
            ch=1
            break
        elif re.search("^"+"00",word_t):
            ch=0
            break
        
        else:
            word_t=word_t.lower()  
            vow_list=re.findall(r'([aeiou]+)',word_t)        # matching a pattern to find vowels or vowel clusters
            cons_list=re.findall(r'([^aeiou]+)',word_t)
            print (vow_list)
            for word in vow_list:                              # vowel rules - prefix "-ub"  and suffix "-bu" to all vowels. If a vowel cluster is found prefix "-ub" to first vowel in cluster and suffix "-bu" to last vowel in cluster
                            res=" "
                            res="-UB-"+word+"-BU-"
                            res=res.upper()
                            myDict[word]=res                              # Add a corresponding affix in a dictionary variable                 


            
            keys=[]
            keys=sorted(myDict.keys(),key=len,reverse=True)
            print("The ubbidubbi version of ", word_t," is: ")
            
            word_kat=word_t
            for pat in keys:
                 word_kat=re.sub(pat,myDict[pat],word_kat)
            final_ans= word_kat.replace("-","")
            final_ans=final_ans.lower()
            print(" ".join(final_ans.split()))
                
            print ("\n Please enter a word or sentence or copy paste any text to translate into UbbyDubby. Press 0 to exit translator and go back to language menu. \n Press 00 to exit and go back to main menu\n")


    return ch


def The_NameGame(x):
    
    while True:
        stem=""
        print("Press 0 to exit translator and go back to game menu.\nPress 00 to exit and go back to main menu\n")
        print("\nLet's play the name game. Enter a PROPER NAME short or long, to generate the rhyme and sing the song\n")
    
    
        
        word_t=input()
        
        if re.search("^"+ "0$",word_t):
            ch=1
            break
        if re.search("^"+"00",word_t):
            ch=0
            break
        
    
        ch=x
        word_t=word_t.lower()  
    # The name game is a fun rhyming game that creates variations of a person's name based on the vowels and consonants present
        stem=""
        stem1=""
        word=word_t.capitalize()
        if re.search("^"+"[AEIOU]"+"([a-z]).+"+"$",word):    #Name starts with a vowel
            name=word
        n=re.search(r'([aeiou])',word)
        if n:
            stem=word[0:n.start()]
            
            name=re.sub(stem,"",word)
            m=re.search("^"+"[BFM]"+"([a-z]).+"+"$",word)
            if m:
                stem1=word[m.start()]
        
        str="""{}, {}, bo-B{}
               banana-fanana fo-F{},
               fee-fi-mo-M{},
               {}!!"""
        
        str1=re.sub(stem1,"",str)

        strfinal=str1.format(word,word,name,name,name,word)

        print("\nThe NAME GAME with", word_t,"\n",strfinal)
        
        
    return ch


def Story(num):
    
    line=[]
    lines=[]
    words_all=[]
    words_final=[]


    str1="Tamil_Story_{}.txt"
    strx=str1.format(num)
    
    f=open(strx, "r",errors="ignore")
    for line in f:
            lines.append(line)    
    f.close()

    
    for line in lines:
            words=line.split()
            words_all+=words
    print(words_all)

    for words in words_all:

        print(words," ",tamil_stemmer.stem(words))
    print("Thanks for using Morphological analyzer! \n")
    return 0


def func(f,x):
    return f(x)


