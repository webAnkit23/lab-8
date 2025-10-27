import random

synonyms = {
    "happy": ["joyful", "cheerful", "content", ],
    "sad": ["unhappy", "sorrowful", "dejected", ],
    "fast": ["quick", "rapid", "speedy"],
    "smart": ["intelligent", "clever", "bright", "sharp", "brilliant", "wise"],
    "angry": ["furious", "irate", "mad", "enraged", "incensed", "annoyed"],
    "beautiful": ["attractive", "lovely"],
    "big": ["large", "huge", "enormous"],
    "small": ["tiny", "little", "diminutive"],
    "cold": ["chilly", "freezing", "frigid", "frosty", "cool", "icy"],
    "hot": ["warm", "scorching", "sizzling"]
}

for word, syn_list in synonyms.items():
    print(f'{word.capitalize()} -> {",".join(syn_list)}')

word = input("enter a word").lower()

if word in synonyms:
    print(synonyms[word])
else:
    print("SORRY")


def refresh(s):
    words = s.split()
    refreshed = []
    for word in words : 
        clean_word = word.strip(".,!?").lower()
        if clean_word in synonyms:
            new = random.choice(synonyms[clean_word]).capitalize()
            refreshed.append(new)
        else:
            refreshed.append(word)
    return "".join(refreshed)

