text = "Daniel przeszedł szkolenie techniczne"
combine_text = ""
for i in range(2137):
    combine_text += f"{i} {text} \n"
file_name = "output/daniel_k.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(combine_text)
print(f"Text was saved to a file {file_name}.")
