import glob
import re
import os

files = glob.glob('feet/*')  # get *.JPG in a list (not sorted!)
files.sort()  # sort the list _in place_
cnt = 1  # start new names with 11.jpg

for f in files:
    original = f  # save the original file name

    new_name = 'feet/bottom%d.jpg'%(cnt)    # create the new name
    print "%s => %s" % (original, new_name)  # verify if it's OK
    os.rename(original, new_name)             # then uncomment to rename
    cnt += 1  # increment the counter