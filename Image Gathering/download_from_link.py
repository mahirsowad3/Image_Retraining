import os
import urllib.request

file = open('links.txt', 'r')


def download_file(url, file_name):
    try:
        print('Beginning download of ' + file_name + '.jpg')
        urllib.request.urlretrieve(url, os.getcwd() + '/ImgNet Images/bed/' + file_name + '.jpg')
        print('Done for ' + file_name)
    except:
        print('image download did not work')


num_image = 0
for i in file.readlines():
    num_image += 1
    download_file(i, str(num_image))


