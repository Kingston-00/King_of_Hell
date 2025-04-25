

# Step 2: Read from abc.txt
file=open("abc.txt", "r")
text = file.read()

# Step 3: Separate vowels and consonants
vowels = "aeiouAEIOU"
vowel_chars = ""
consonant_chars = ""

for ch in text:
        if ch in vowels:
            vowel_chars += ch
        else:
            consonant_chars += ch

# Step 4: Write vowels to vowels.txt
file2=open("vowels.txt", "w")
text2=file2.write(vowel_chars)

# Step 5: Write consonants to constants.txt
file3=open("constants.txt", "w")
text3=file3.write(consonant_chars)
