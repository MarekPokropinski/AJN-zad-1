import re
sentence_expression = r"([A-Z][^\.^\?^\!]*[\.\?\!])"

sentence_exceptions = [
    (r'([Dd]r\. $)', r'(.+)'),
    (r'([Mm]gr\. $)', r'(.+)'),
    (r'([Ii]nż\. $)', r'(.+)'),
    (r'([Tt]zn\. $)', r'(.+)'),
    (r'([Tt]z\. $)', r'(.+)'),
]

sentence_rules = [
    (r'([\!\?]\s)$', r'(.+)'),
    (r'(\.\s)$', r'([A-ZŻŹĆŃÓŁĘĄŚ])'),
]

sentence_rules = [(re.compile(rule[0]), re.compile(rule[1]))
                  for rule in sentence_rules]
sentence_exceptions = [(re.compile(rule[0]), re.compile(rule[1]))
                       for rule in sentence_exceptions]

with open('text.txt', encoding='utf-8') as t:
    text = t.read()

splits = [0]
pos = 0

while pos < len(text):
    for exception in sentence_exceptions:
        if exception[0].search(text[:pos]) and exception[1].match(text, pos):
            break
    else:
        # no exception hit
        for rule in sentence_rules:
            if rule[0].search(text[:pos]) and rule[1].match(text, pos):
                splits.append(pos)
                break
    pos += 1

splits.append(pos)

for a, b in zip(splits, splits[1:]):
    print(text[a:b])

sentences = [text[a:b].rstrip() for a, b in zip(splits, splits[1:])]
print("Zdania:")
for i, sentence in enumerate(sentences):
    print(f'{i}: "{sentence}"')

# words_expressions = [
#     r'([a-zżźćńółęąś]+)'
# ]
# symbols = [
#     r'([\-–\+,\'\"\:;\?\.\!])'
# ]

word_exceptions = [
    (r'([Dd]r$)', r'(\.)'),
    (r'([Mm]gr$)', r'(\.)'),
    (r'([Ii]nż$)', r'(\.)'),
    (r'([Tt]zn$)', r'(\.)'),
    (r'([Tt]z$)', r'(\.)'),
    (r'([Ii]td$)', r'(\.)'),
]

word_rules = [
    (r'([A-ZŻŹĆŃÓŁĘĄŚa-zżźćńółęąś1-9]) $', r'([A-ZŻŹĆŃÓŁĘĄŚa-zżźćńółęąś1-9])'),
    (r'([a-zżźćńółęąś1-9])$', r'([,\.;\!\?–\-\*\/\+\^\&])'),
    (r'([,\.;\!\?–\-\*\/\+\^\&])$', r'.?'),
]

word_rules = [(re.compile(rule[0]), re.compile(rule[1]))
                  for rule in word_rules]
word_exceptions = [(re.compile(rule[0]), re.compile(rule[1]))
                       for rule in word_exceptions]

for sentence in sentences:
    print('Sentence:', sentence)
    splits = [0]
    pos = 0

    while pos < len(sentence):
        for exception in word_exceptions:
            if exception[0].search(sentence[:pos]) and exception[1].match(sentence, pos):
                break
        else:
            # no exception hit
            for rule in word_rules:
                if rule[0].search(sentence[:pos]) and rule[1].match(sentence, pos):
                    splits.append(pos)
                    break
        pos += 1

    splits.append(pos)
    words = [sentence[a:b].rstrip() for a, b in zip(splits, splits[1:])]
    print("Wyrazy:")
    for i, word in enumerate(words):
        print(f'{i}: "{word}"')