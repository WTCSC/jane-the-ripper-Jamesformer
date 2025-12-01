import hashlib
def crack_passwords(hashes_path, wordlist_path):
    s = set()
    with open(hashes_path):
        for line in hashes_path.splitlines():
            line = line.strip('/n')
            s.add(line)
        with open(wordlist_path):
            for word in wordlist_path.split():
                word.strip('/n')
                hash_object = hashlib.md5(word.encode())
                hashed_word = hash_object.hexdigest()
                if hashed_word in s:
                    return word
                
    

hash_path = input("what is the path to the file where you have your hashes: ")
word_path = input("what is the path to the word list file: ")
print(crack_passwords(hash_path, word_path))
