import os

if not os.path.exists('./output'):
    os.makedirs('./output')

text = "Hej to test"
combine_text = ""
for i in range(2137):
    combine_text += f"{i} {text} \n"
file_name = "output/karolajna.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(combine_text)
print(f"Text was saved to a file {file_name}.")
