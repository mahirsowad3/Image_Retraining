import os

directory_list = ['bed', 'car', 'chair', 'door', 'stairs', 'table']


def change_files(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpe'):
            abs_filename = os.path.join(directory, filename)
            root_name = os.path.splitext(filename)[0]
            abs_root_name = os.path.join(directory, root_name)
            os.rename(abs_filename, abs_root_name + '.jpg')
        else:
            continue


training_dir = os.getcwd() + '\Training Images'
for i in range(len(directory_list)):
    w_dir = os.path.join(training_dir, directory_list[i])
    change_files(w_dir)
