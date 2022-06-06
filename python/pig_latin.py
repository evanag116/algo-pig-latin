def translate(str):
  words = str.split()
  capitalized = [i[0].isupper() for i in words]
  vowels = "aeiou"

  for j in range(len(words)):
    words[j] = words[j].lower()
    for letter in words[j]:
      if letter in vowels:
        break
      else:
        words[j] = words[j][1:] + words[j][0]
    words[j] += "ay"
    if capitalized[j]:
      words[j] = words[j].title()

  return " ".join(words)


print(translate("the quick brown fox"))
