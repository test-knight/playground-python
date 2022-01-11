def emoji_converer(text):
    words = text.split(' ')
    emojis = {
        ":)": "😁",
        ":(": "😞",
        ":sunshine": "☀️"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
print(emoji_converer(text=message))
