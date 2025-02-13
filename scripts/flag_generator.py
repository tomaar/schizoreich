#not in use

import os
import shutil

def extract_first_three_letters(file_path):
    result_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the first 3 letters from each line
            first_three_letters = line[:3]
            if first_three_letters[0] == '#' or first_three_letters[0] == '\n' or first_three_letters[0] == ' ':
                continue
            result_list.append(first_three_letters)
    return result_list

def process_directory():
    current_directory = os.getcwd()
    directory = os.path.join(current_directory, 'common', 'country_tags')
    
    combined_list = []
    
    for filename in os.listdir(directory):
        if filename == 'zz_dynamic_countries.txt' or filename == 'zz_new_dynamic_countries.txt':
            continue
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Extract first three letters from each line in the file
            file_list = extract_first_three_letters(file_path)
            # Combine the lists
            combined_list.extend(file_list)

    return combined_list

result_list = process_directory()
result_list.pop() # remove '\n' from the end of the list


working_directory = os.getcwd()

flags_directory = os.path.join(working_directory, 'scripts', 'flags')

if os.path.exists(flags_directory):
    shutil.rmtree(flags_directory)

os.makedirs(flags_directory)
os.makedirs(os.path.join(flags_directory, 'medium'))
os.makedirs(os.path.join(flags_directory, 'small'))

directory = os.path.join(working_directory, 'scripts')
a = os.path.join(directory, 'ex_big.tga')
b = os.path.join(directory, 'flags')
for tag in result_list:
    shutil.copy(a, b)
    current_path = os.path.join(b, 'ex_big.tga')
    new_path = os.path.join(b, tag + '.tga')
    os.rename(current_path, new_path)

directory = os.path.join(working_directory, 'scripts')
a = os.path.join(directory, 'ex_medium.tga')
b = os.path.join(directory, 'flags', 'medium')
for tag in result_list:
    shutil.copy(a, b)
    current_path = os.path.join(b, 'ex_medium.tga')
    new_path = os.path.join(b, tag + '.tga')
    os.rename(current_path, new_path)

directory = os.path.join(working_directory, 'scripts')
a = os.path.join(directory, 'ex_small.tga')
b = os.path.join(directory, 'flags', 'small')
for tag in result_list:
    shutil.copy(a, b)
    current_path = os.path.join(b, 'ex_small.tga')
    new_path = os.path.join(b, tag + '.tga')
    os.rename(current_path, new_path)
