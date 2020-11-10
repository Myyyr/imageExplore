import os
import numpy as np
import nibabel as nib
import pandas as pd


def nibfile(file):
    img = nib.load(file)
    return img.get_fdata()


def save_dict(sumary_dict, path = "sumary.csv"):
	df = pd.DataFrame(sumary_dict)
	df.to_csv(path)



def save_image(img, path):
	with open(path, 'wb') as f:
		np.save(f, img)


def load_image(path):
	with open(path, 'rb') as f:
		return np.load(f)