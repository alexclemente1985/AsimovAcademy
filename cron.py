import os

types = ['jpg', 'zip', 'pdf', 'exe']

base_path = os.path.expanduser('~')

path = os.path.join(base_path, 'Downloads')

cwd = os.chdir(path)

full_list = os.listdir(cwd)
for type_ in types:
    if type_ not in os.listdir():
        os.mkdir(type_)

file_index = 0
previous_index = -1
for file in full_list:
    if file_index == previous_index:
        continue

    for type_ in types:
        if( '.' + type_ in file) and (len(file.split('.')) == 2):
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type_, file)

            print(f'Index {file_index} | old_index {previous_index} -> old_path: {old_path} | new_path {new_path}')
            

            os.replace(old_path, new_path)
    
    file_index += 1
    previous_index += 1
