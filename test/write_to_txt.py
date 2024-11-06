text = "Test test"
combine_text = ""
for i in range(2137):
    combine_text += f"{i} {text} \n"
file_name = "output/test.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(combine_text)
print(f"Text was saved to a file {file_name}.")
