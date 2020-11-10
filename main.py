import pandas as pd
import argparse
import os

import utils
import explore

def seg_stats(path):
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

def pick_an_image(path, n = 1, frame = 120, save_path = 'image'):
	seg_file_list = []
	c1_file_list = []
	c2_file_list = []
	c3_file_list = []
	c4_file_list = []




	for folder in os.listdir(path):
		print(folder)
		seg_file_list.append(os.path.join(path, folder, folder + "_seg.nii.gz"))
		c1_file_list.append(os.path.join(path, folder, folder + "_t1.nii.gz"))
		c2_file_list.append(os.path.join(path, folder, folder + "_t1ce.nii.gz"))
		c3_file_list.append(os.path.join(path, folder, folder + "_t2.nii.gz"))
		c4_file_list.append(os.path.join(path, folder, folder + "_flair.nii.gz"))

	im_dict = {'seg_file_list':seg_file_list,
				'c1_file_list':c1_file_list,
				'c2_file_list':c2_file_list,
				'c3_file_list':c3_file_list,
				'c4_file_list':c4_file_list}

	for key in list(im_dict.keys()):
		img1 = utils.nibfile(img[key][frame, :, :])
		img2 = utils.nibfile(img[key][:, frame, :])
		img3 = utils.nibfile(img[key][:, :, frame])

		utils.save_image(img1, save_path+str(n)+'_'+key[:2]+'_'+str(frame)+'_1_.pny')
		utils.save_image(img2, save_path+str(n)+'_'+key[:2]+'_'+str(frame)+'_2_.pny')
		utils.save_image(img3, save_path+str(n)+'_'+key[:2]+'_'+str(frame)+'_3_.pny')










if __name__ == '__main__':

	parser = argparse.ArgumentParser("dataset path")
	parser.add_argument('-t', '--tool', help='function to use', required = True)
	parser.add_argument('-p', '--path', help='dataset path', required=True)
	parser.add_argument('-i', '--image', help='image to pick', required=False, default = 1)
	parser.add_argument('-f', '--frame', help='frame to loook at', required=False, default = 120)
	parser.add_argument('-s', '--save_path', help='save path', required=False, default = 'image')

	if parser.parse_args().tool == 'pick':
		pick_an_image(parser.parse_args().path, parser.parse_args().image, parser.parse_args().frame, parser.parse_args().save_path)






