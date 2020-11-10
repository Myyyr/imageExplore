import pandas as pd
import argparse
import os

import utils
import explore

def main(path):
	sumary_dict = {
					"wt_seg_size" : [], 
					"tc_seg_size" : [], 
					"et_seg_size" : [],
					"image_size" : []
				}

	file_list = []

	for folder in os.listdir(path):
		print(folder)
		file = os.path.join(path, folder, folder + "_seg.nii.gz")
		file_list.append(file)

	i = 1
	for file in file_list:
		print("Doing :", i, "/", len(file_list))
		sumary_dict = explore.process_all(file, sumary_dict)
		i+=1

	utils.save_dict(sumary_dict)

	print("END")
	return 0




if __name__ == '__main__':

	parser = argparse.ArgumentParser("dataset path")
	parser.add_argument('-p', '--path', help='dataset path', required=True)


	main(parser.parse_args().path)






