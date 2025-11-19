import emoji

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))

all_emojis = emoji.EMOJI_DATA.keys()

for em in all_emojis:
    print(em, end="")