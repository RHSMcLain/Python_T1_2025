import pyperclip
input = pyperclip.paste()
print(input)
input = input[:10]
pyperclip.copy(input)
print("Done")
