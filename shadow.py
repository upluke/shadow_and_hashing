import bcrypt
# import nltk        # used to download words, run one time only
from nltk.corpus import words
from time import perf_counter
from collections import defaultdict
from pprint import pprint


def main():
    # nltk.download('words')  # used to download words, run one time only
    # with open("shadow.txt", "r") as file:
    #     for line in file:
    #         cracker(line)
          
    # cracker3
    
    # my_dict[algfacsalt] = [(username, hash), ...]  
    words_list: list[bytes] = []
    with open("temp_words.txt", "r") as file:
        for line in file:
            words_list.append(line.rstrip().encode())
        
    my_dict:dict[bytes, list[tuple[str, bytes]]] = {} # tuple(User, Hash)
    with open("shadow.txt", "r") as file:
        for line in file:
            user, res= line.split(":")
            algfacsalt = res[:29].encode() # since hashpw takes a byte obj
            hash_value = res[29:].encode().rstrip()
           
            if algfacsalt not in my_dict:
                my_dict[algfacsalt] =[(user, hash_value)]
            else:
                my_dict[algfacsalt].append((user, hash_value))
    # pprint(my_dict)
    
    # or using defaultdict:
    # my_dict = defaultdict[bytes, list[tuple[str, bytes]]](list)
    # my_dict[algfacsalt].append((user, hash_value))
    
    cracker3(my_dict, words_list)
  
def cracker(s):
    # print(s)
    encoded_s= s.split(":")[1].encode().rstrip() # b denotes each char is 1 bite
    
    
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
    
    
    

def cracker3(my_dict: dict[bytes, list[tuple[str, bytes]]], words_list: list[bytes]):
    
   
   for algofacsalt, users_and_hashes in my_dict.items():
      print(f"Starting {algofacsalt = }")
      start_time =perf_counter() 
      for word in words_list:
            word_hash =  bcrypt.hashpw(word, algofacsalt)
            for user, user_hash  in users_and_hashes:
                if word_hash== user_hash:
                    end_time =perf_counter()
                    print(user, word)
                    print(end_time - start_time)
   
            
def createTempWords():
    with open("temp_words.txt", "w") as file:
        for word in words.words():
            if len(word)>= 6 and len(word)<=10:
                file.write(f"{word}\n")
    
    
    
# createTempWords()  # run one time, then comment out
main()
    