import os
import urllib.request
import time
import datetime

file = open('bed_links.txt', 'r')

images_successfully_downloaded = 1


def download_file(url):
    global  images_successfully_downloaded
    try:
        file_name = str(images_successfully_downloaded)
        print('Beginning download of ' + file_name + '.jpg')
        urllib.request.urlretrieve(url, os.getcwd() + '/ImgNet Images/bed/' + file_name + '.jpg')
        print('Done for ' + file_name)
        images_successfully_downloaded += 1
    except:
        print('image download did not work')


start_time = time.time()
num_link = 0
for i in file.readlines():
    num_link += 1
    download_file(i)

end_time = time.time()
completion_time = end_time - start_time
print('Time completion: ' + str(datetime.timedelta(seconds=completion_time)))

