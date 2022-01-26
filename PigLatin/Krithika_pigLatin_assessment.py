# Rules
# Word beginning with consonant: Extract the first character of the word and attach suffix "ay" to it, concatenate with remnant string
# Word begining with vowel : if there are no more vowels (monosyllable), concantenate the string with hay 
# Word beginning with vowel: Remove first character from string, append with "way" if there are multiple vowels (polysyllabic)
# until - untilway/ answer answerway
import re,sys


def consonant(s,i):
    letter = s[i]
    if letter in 'aeiou':
        return False
    else:
        return True



def rule(w):   
    r="ay"
    if re.match('^([Ii])$',w):
        return w+"h"+r
    elif re.match('^([Aa])$',w):
        return w+"y"+r
    
    
    else:
        s2=re.split(r"([^a-zA-Z0-9'])",w)
        w1=s2[0]
        s2.pop(0)
        x1="".join(s2)
        m = re.search('^'+'[^aeiou]'+'(.*)'+'$',w1)     # THIS RULE IDENTIFIES IF THE FIRST CHARACTER IS A CONSONANT
        if m:
            s=m.group(1)
            return s+w1[0].lower()+r+x1
        else:
            i=1
            while i<len(w):
                if consonant(w,i) is False:
                    break
                i+=1
            if i>1:
                
                return w1+"way"+x1
            else:
                return w1+"hay"+x1




print("Pig latin translator: \n")
while True:
    txt=""

    print("Please enter a word, phrase or sentence in English: Please enter 0 or any numeric character to exit")
    s=input()
    if re.search('^'+'(.*)'+'[0-9]'+'(.*)',s):
        print("thanks for playing. Bye!")
        break
    else:
            l=s.split()
            for word in l:
                txt+=rule(word)+" "
            print(txt)
            
    
