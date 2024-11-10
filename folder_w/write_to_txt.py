import os

if not os.path.exists('./output'):
    os.makedirs('./output')

text = "Hello world"
combine_text = ""
for i in range(2):
    combine_text += f"{i} {text} \n"
file_name = "output/idk.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(combine_text)
print(f"Text was saved to a file {file_name}.")
