import geohash #pip install python-geohash
import string
import random
import hashlib

NUM_ENCODE_CHARS = 3
def init_word_list():
    word_hasher = hashlib.sha256()

    lookup_table_chars = '0123456789bcdefghjkmnpqrstuvwxyz'
    words_needed = len(lookup_table_chars)**NUM_ENCODE_CHARS

    with open("wordlist-german.txt", encoding='utf-8') as file:
        lookup_table_words = []
        for line in file:
            lookup_table_words.append(file.readline()[:-1])
    lookup_table_words.sort()
    lookup_table_words_new = []
    last_word = ""
    for word in lookup_table_words:
        if word not in last_word and len(word) < 14:
            lookup_table_words_new.append(word)
        last_word = word

    lookup_table_words = lookup_table_words_new

    lookup_table_words_final = [None for i in range(words_needed)]
    finished = False
    idx = 0
    while not finished:
        if idx == 0:
            sub_words = ""
        else:
            raise # we do not want to add new random words
            sub_words = f"{idx}x"
        for word in lookup_table_words:
            full_word = sub_words+word
            word_hash = hashlib.sha256(full_word.encode("utf-8")).hexdigest()
            # use the has as pseudo random value
            # if two words have the same start of the hash, then you can 
            # swap them out in the final phrase
            word_index = int("0x"+str(word_hash[0:2**(NUM_ENCODE_CHARS+1)]), 16) % words_needed
            if lookup_table_words_final[word_index] is None:
                lookup_table_words_final[word_index] = full_word
        finished = True
        for word in lookup_table_words_final:
            if word is None:
                finished = False
        idx += 1
    return lookup_table_chars, lookup_table_words_final

lookup_table_chars, lookup_table_words = init_word_list()
            

def geo2phrase(lon, lat, precision=4):
    geohash_chars = str(geohash.encode(lon, lat, precision))
    wordlist = ''
    while len(geohash_chars) > 0:
        geohash_part = geohash_chars[:NUM_ENCODE_CHARS]
        geohash_chars = geohash_chars[NUM_ENCODE_CHARS:]
        word_index = 0
        for char in geohash_part:
            lookup_index = lookup_table_chars.index(char)
            if lookup_index < 0:
                raise Exception("invalid character")
            word_index *= len(lookup_table_chars)
            word_index += lookup_index            
        if wordlist != "":
            wordlist += "."            
        wordlist += lookup_table_words[word_index]
    return wordlist
    
def phrase2geo(words):
    wordlist = words.split(".")
    geohash_chars = ""
    for word in wordlist:
        word_index = lookup_table_words.index(word)
        if word_index < 0:
            raise Exception("invalid word")
        geohash_part = ""    
        for r in range(NUM_ENCODE_CHARS):
            char_index = word_index % len(lookup_table_chars)
            word_index //= len(lookup_table_chars)
            new_char = lookup_table_chars[char_index]
            geohash_part = new_char+geohash_part
        geohash_chars += geohash_part
    location = geohash.decode(geohash_chars)   
    return (location[0], location[1])
    
