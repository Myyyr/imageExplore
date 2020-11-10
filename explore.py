import numpy as np
import utils


def image_size(img):
	s = 1
	for i in list(img.shape):
		s *= i
	return s

def getWTMask(labels):
    return (labels != 0).float()

def getTCMask(labels):
    return ((labels != 0) * (labels != 2)).float() 

def getETMask(labels):
    return (labels == 4).float()

def seg_size(mask):
	return np.sum(mask)


def process_all(file, sumary_dict):
	img = utils.nibfile(file)

	sumary_dict["image_size"].append(image_size(img))

	sumary_dict["wt_seg_size"].append(seg_size(getWTMask(img)))
	sumary_dict["tc_seg_size"].append(seg_size(getTCMask(img)))
	sumary_dict["et_seg_size"].append(seg_size(getETMask(img)))


	return sumary_dict

# sumary_dict = {
# 				"wt_seg_size" = [], 
# 				"tc_seg_size" = [], 
# 				"et_seg_size" = [],
# 				"image_size" = [],
# 				"pad" = []
# 			}