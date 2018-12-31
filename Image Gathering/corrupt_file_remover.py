from os import getcwd
from os import listdir
from os import remove
from os import rename
from PIL import Image

file_dir = getcwd() + '/ImgNet Images/bed/'
number_of_bad_files = 0


def verify_image(filename):
    global number_of_bad_files
    if filename.endswith('.jpg'):
        try:
            img = Image.open(file_dir + filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
        except (IOError, SyntaxError):
            print('Bad file:', filename)  # print out the names of corrupt files
            number_of_bad_files += 1
            remove(file_dir + file_name)
            print(file_name + ' has been deleted.')


def rename_files_in_dir():
    file_num = 1
    for filename in listdir(file_dir):
        try:
            rename(file_dir + filename, file_dir + str(file_num) + '.jpg')
            file_num += 1
        except FileExistsError:
            file_num += 1
            continue


for file_name in listdir(file_dir):
    if file_name.endswith('.jpg'):
        verify_image(file_name)


print('number_of_bad_files: ' + str(number_of_bad_files))
rename_files_in_dir()
