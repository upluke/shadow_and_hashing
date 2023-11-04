import bcrypt
# import nltk        # used to download words, run one time only
from nltk.corpus import words
from time import perf_counter

def main():
    # nltk.download('words')  # used to download words, run one time only
    with open("shadow.txt", "r") as file:
        for line in file:
            cracker(line)
            
            


def cracker(s):
    # print(s)
    encoded_s= s.split(":")[1].encode().rstrip() # b denotes each char is 1 bite
    print(encoded_s)
    psw = ""
    start_time =perf_counter()
    for word in words.words():
        if len(word) >= 6 and len(word)<=10:
            
            if bcrypt.checkpw(word.encode(), encoded_s):
                psw = word
                
                break
    end_time =perf_counter()
    print(psw)
    print(end_time-start_time)
    

# hashpw
    
    # splited_s = s.split("$")
   
    # algorithm = splited_s[1]
    # workfactor = splited_s[2]
    # salt= splited_s[3][:22]
 
    
    
    
    
main()
    