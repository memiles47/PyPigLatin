original = input("Please enter a sentence: ").strip().lower()
words = original.split()

newWords = []
vowels = "aeiou"

for word in words:
    if word[0] in vowels:
        newWords.append(word + "yay")

    else:
        vowelPosition = 0
        for letter in word:
            if letter not in vowels:
                vowelPosition = vowelPosition + 1

            else:
                break

        consonants = word[:vowelPosition]
        newWords.append(word[vowelPosition:] + consonants + "ay")

output = " ".join(newWords)
print(output)