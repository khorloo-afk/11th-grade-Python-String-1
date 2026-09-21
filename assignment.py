# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
    return len(text)
    
print(count_characters("Hello"))
    pass

# Exercise 2
def remove_spaces(text):
i = input()
print(len(s.replace(" ", "")))
    pass

# Exercise 3
def count_vowels(text):
text = "Hello World"
vowels = "aeiou"
count = 0
for c in text.lower():
    if c in vowels:
        count += 1

print(count)
# Exercise 4
def replace_vowels(text):
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
for vowel in vowels:
    text = text.replace(vowel, "*")

print(text)
# Exercise 5
def count_words(text):
    # Write your code here
    pass

# Exercise 6
def find_longest_word(text):
    # Write your code here
    pass
#7
# DECLARE Num:INTEGER
# Num<-INT(RAND(100))+1
# OUTPUT "Enter num between 1 to 100"
# INPUT UserGuess
# WHILE UserGuess<>Num DO
#     IF UserGuess<Num THEN
#         OUTPUT "TOO LOW Enter again"
#     ELSE
#         OUTPUT "TOO High Enter again"
#     ENDIF
#     INPUT UserGuess
# ENDWHILE
# OUTPUT "You win"

