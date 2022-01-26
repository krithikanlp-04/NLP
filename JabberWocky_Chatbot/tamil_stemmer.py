import re, sys 


# Stemmer algorithm for Tamil 

def consonant(s,i):
    letter = s[i]
    if letter in 'aeiouAEIOU':
        return False
    else:
        return True
def cv(w):
    label=''
    for i in range(len(w)):
        if consonant(w,i):
            label += 'C'
        else:
            label+= 'V'
    return label
    
def measure(w):
    cvlabel= cv(w)
    vcs=re.findall("VC",cvlabel)
    return len(vcs)


def rule (c,e,r,w):
    m = re.search('^(.*)'+e+'$',w)
    if m:
        s = m.group(1)
        if c(s):
            return s+r
    return None


def specialrule(w):
    cvform = cv(w)
    
    if cvform.endswith("C"):
        m2 = re.search('[trkln]'+'k$',w)
        if m2:
            print (w[0:m2.start()])
            return w[0:m2.start()]

    return None 
def nullcond(x):                               #a vacuous condition
    return True

def vcond(x): #condition: contains vowel
    cvform = cv(x)
    if re.search('V',cvform):
        return True
    return False


def m1cond(x): #condition: m > 0
    if measure(x) > 0:
        return True
    return False

def conscond(w): #m1ocond
    cvform = cv(w)
    if measure(cvform) >= 1:
        if re.search("^"+"(.*)"+"C$",cvform):
            return True
    return False


#Affix stripping post removing derivational morphemes - Below are the rules for plurals, and other suffixes
def special(w): 
    a = rule(nullcond,'aL','',w)         
    if a: return specialrule(a)
    b = rule(nullcond,'vum','',w)         
    if b: return b
    c = rule(nullcond,'ve','',w)         
    if c: return c
    f = rule(nullcond,'yuDAN','',w)         
    if f: return f
    g = rule(nullcond,'uDAN','',w)         
    if g: return g
    
    
   
    return w


# Affix stripping for markers of genitive case, tense, dative case etc
def step1b(w):
    a = rule(nullcond,'ntu','',w)
    if a: return a
    b = rule(vcond,'in','',w)
    if b:
        return special(b)
    c = rule(nullcond,'Aka','u',w)
    if c:
        return special(c)
    d = rule(nullcond,'uL','u',w)
    if d:
        return d
    e = rule(conscond,'ukku','',w)
    if e:
        return e
    return w


def stem(w): #stemming with blocks
    s1b = step1b(w)
    s1c=step1b(s1b)
    return s1c

