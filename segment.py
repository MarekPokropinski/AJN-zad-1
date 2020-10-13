import re
sentence_expression = r"([A-Z][^\.^\?^\!]*[\.\?\!])"

with open('text.txt', encoding='utf-8') as t:
    text = t.read()

# text = input()
matches = re.findall(sentence_expression, text)

sentences = []
print("Zdania:")
for i, match in enumerate(matches):
    sentences.append(match.lower())
    print(f'{i}: "{match}"')

words_expressions = [
    r'([a-zżźćńółęąś]+)'
]
symbols = [
    r'([\-–\+,\'\"\:;\?\.\!])'
]


for sentence in sentences:
    print(sentence)
    tokens = []
    while sentence:
        matched = False
        for reg_ex in  words_expressions:
            if m := re.match(reg_ex, sentence):
                tokens.append({'type':'word', 'text': m.group()})
                sentence = sentence[m.end():]
                matched = True
                break
        else: 
            if not matched:
                for reg_ex in symbols:
                    if m := re.match(reg_ex, sentence):
                        tokens.append({'type':'symbol', 'text': m.group()})
                        sentence = sentence[m.end():]
                        matched = True
                        break
        if not matched:
            sentence = sentence[1:]

    print(tokens)

