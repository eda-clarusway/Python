#check if two strings is anagrams
def is_anagram (s1,s2):
  return set(s1)==set(s2) 
print(is_anagram("silik","kilis"))