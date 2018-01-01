
import os
import sys
import glob
import cv2

import dlib
from skimage import io




#
# # Now let's do the training.  The train_simple_object_detector() function has a
# # bunch of options, all of which come with reasonable default values.  The next
# # few lines goes over some of these options.
options = dlib.simple_object_detector_training_options()
# # Since faces are left/right symmetric we can tell the trainer to train a
# # symmetric detector.  This helps it get the most value out of the training
# # data.
options.add_left_right_image_flips = False

# # The trainer is a kind of support vector machine and therefore has the usual
# # SVM C parameter.  In general, a bigger C encourages it to fit the training
# # data better but might lead to overfitting.  You must find the best C value
# # empirically by checking how well the trained detector works on a test set of
# # images you haven't trained on.  Don't just leave the value set at 5.  Try a
# # few different C values and see what works best for your data.
options.C = 5
# # Tell the code how many CPU cores your computer has for the fastest training.
options.num_threads = 3
options.be_verbose = True
#
#
training_xml_path = "xmlFiles/feet_test.xml"
testing_xml_path = "xmlFiles/feet_test.xml"
# # This function does the actual training.  It will save the final detector to
# # gotEye.svm.  The input is an XML file that lists the images in the training
# # dataset and also contains the positions of the face boxes.  To create your
# # own XML files you can use the imglab tool which can be found in the
# # tools/imglab folder.  It is a simple graphical tool for labeling objects in
# # images with boxes.  To see how to use it read the tools/imglab/README.txt
# # file.  But for this example, we just use the training.xml file included with
# # dlib.
dlib.train_simple_object_detector(training_xml_path, "feet_01.svm", options)
#
#
#
# # Now that we have a face detector we can test it.  The first statement tests
# # it on the training data.  It will print(the precision, recall, and then)
# # average precision.
print("")  # Print blank line to create gap from previous output
print("Training accuracy: {}".format(
    dlib.test_simple_object_detector(training_xml_path, "feet_01.svm")))
# However, to get an idea if it really worked without overfitting we need to
# run it on images it wasn't trained on.  The next line does this.  Happily, we
# see that the object detector works perfectly on the testing images.
print("Testing accuracy: {}".format(
    dlib.test_simple_object_detector(testing_xml_path, "feet_01.svm")))


