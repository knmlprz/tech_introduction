import os

if not os.path.exists('./output'):
    os.makedirs('./output')

text = "123123"
combine_text = ""
for i in range(420):
    combine_text += f"{i} {text} \n"
file_name = "output/123.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(combine_text)
print(f"Text was saved to a file {file_name}.")
