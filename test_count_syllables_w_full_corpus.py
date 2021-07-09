from count_syllables import count_syllables

with open(r'hoofdstuk_8_9\train.txt') as in_file:
    words = set(in_file.read().split())

missing = []

for word in words:
    try:
        num_syllables = count_syllables(word)
    except KeyError:
        missing.append(word)
    
if missing:
    print("Missing words:")
    for word in missing:
        print(word)
else:
    print("No missing words!")