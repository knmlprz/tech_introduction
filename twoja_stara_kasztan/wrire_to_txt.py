import os

if not os.path.exists('./output'):
    os.makedirs('./output')

text = "In Springfiled Ohio. Theyre eating the dogs the people that came inj, theyre eating the cats"
combine_text = ""
for i in range(2137):
    combine_text += f"{i} {text} \n"
file_name = "output/kacper_sowa.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(combine_text)
print(f"Text was saved to a file {file_name}.")