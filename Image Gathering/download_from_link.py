import os
import urllib.request
import time
import datetime

file = open('bed_links.txt', 'r')


def download_file(url, file_name):
    try:
        print('Beginning download of ' + file_name + '.jpg')
        urllib.request.urlretrieve(url, os.getcwd() + '/ImgNet Images/bed/' + file_name + '.jpg')
        print('Done for ' + file_name)
    except:
        print('image download did not work')


start_time = time.time()
num_image = 0
for i in file.readlines():
    num_image += 1
    download_file(i, str(num_image))

end_time = time.time()
completion_time = end_time - start_time
print('Time completion: ' + str(datetime.timedelta(seconds=completion_time)))

