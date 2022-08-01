import cv2
import numpy as np
from PIL import Image
import os
import glob
import pandas as pd
import csv

"""
For each image in INPUT_FOLDER, this script augments the image by: rotation through 7 angles, flipping, brightening and dimming then appends them to the same folder
CSV_FILE contains the labels for each image and will also be updated by the script
Parameters to change: INPUT_FOLDER, image_count (to last image number in folder before augmentation)
"""

INPUT_FOLDER = '.\\images_dataset'
CSV_FILE = 'data_dataset.csv'
DATA = pd.read_csv(CSV_FILE)

angles = [45, 90, 135, 180, 225, 270, 315]
image_count = 628

for img in glob.glob(INPUT_FOLDER + "/*.jpg"):
    img_name = img.partition(INPUT_FOLDER + "\\")[2]
    img_label = DATA.loc[DATA['image-name'] == img_name, 'label'].iloc[0]
    image = cv2.imread(img)
    height, width = image.shape[:2]
    # 1. Rotations
    for ang in angles:
        image_count += 1
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), ang, 1)
        rotated_img = cv2.warpAffine(image, rotation_matrix, (width, height))
        # Save image
        rotated_img_name = str(image_count) + '.jpg'
        cv2.imwrite(os.path.join(INPUT_FOLDER, rotated_img_name), rotated_img)

        # Update CSV
        with open(CSV_FILE, 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow([rotated_img_name, img_label])

    # 2. Flipping
    flip_img = cv2.flip(image, 1)
    image_count += 1

    # Save image
    flip_img_name = str(image_count) + '.jpg'
    cv2.imwrite(os.path.join(INPUT_FOLDER, flip_img_name), flip_img)

    # Update CSV
    with open(CSV_FILE, 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([flip_img_name, img_label])

    # 3a. Increase brightness 
    bright = np.ones(image.shape, dtype= "uint8") * 70
    bright_img = cv2.add(image, bright)
    image_count += 1

    # Save image
    bright_img_name = str(image_count) + '.jpg'
    cv2.imwrite(os.path.join(INPUT_FOLDER, bright_img_name), bright_img)

    # Update CSV
    with open(CSV_FILE, 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([bright_img_name, img_label])

    # 3b. Decrease brightness 
    dim_img = cv2.subtract(image, bright)
    image_count += 1

    # Save image
    dim_img_name = str(image_count) + '.jpg'
    cv2.imwrite(os.path.join(INPUT_FOLDER, dim_img_name), dim_img)

    # Update CSV
    with open(CSV_FILE, 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([dim_img_name, img_label])
