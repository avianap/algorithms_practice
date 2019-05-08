

def ransom_note(note, magazine):
    """Return true if ransom note could be constructed from magazine

    Args:
        note (string): ransom note
        magazine (string): all the words in a magazine

    Return:
        boolean: True is note could be made from magazine
    """

    def string_to_hash_table(string):
        """given a string, create a hash table with all the characters mapped to their count
        """
        string = string.lower()
        string_list = list(string.replace(' ','').replace('.',''))
        hash_table = {}
        for i in string_list:
            if i in hash_table:
                hash_table[i] += 1
            else: 
                hash_table[i] = 1
        return hash_table

    note_dict = string_to_hash_table(note)
    magazine_dict = string_to_hash_table(magazine)
    for key in note_dict.keys():
        try:
            if note_dict[key] > magazine_dict[key]:
                return False
        except:
            return False

    return True

note = "Meet at midnight"
magazine = "A heroic dog rescude a small child from a big well. Yesterday evening Kyle age five fell down a well on his family farm. The dog met him at midnight"
magazine_2 = "A heroic dog"

print(ransom_note(note, magazine))
print(ransom_note(note, magazine_2))

