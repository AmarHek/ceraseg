import numpy as np
import nibabel as nib
import os
import argparse
import cv2

import imageio


def convert_to_uint8(img):
    img_uint = np.zeros(img.shape)
    return cv2.normalize(img, img_uint, 0, 255, cv2.NORM_MINMAX)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str, default='./output/')

    args = parser.parse_args()

    inputfile = args.input
    outputfolder = args.output

    if not inputfile:
        raise ValueError("No input specified.")

    print('Input file is ', inputfile)
    print('Output folder is ', outputfolder)

    # set destination folder
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)
        print("Created ouput directory: " + outputfolder)

    # set fn as your 4d nifti file
    image_array = nib.load(inputfile).get_data()
    print(len(image_array.shape))

    #if len(image_array.shape) == 4:
    #  # set 4d array dimension values
    #  nx, ny, nz, nw = image_array.shape
    #
    #  print('Reading NIfTI file...')
    #
    #  total_volumes = image_array.shape[3]
    #  total_slices = image_array.shape[2]
    #
    #  # iterate through volumes
    #  for current_volume in range(0, total_volumes):
    #      slice_counter = 0
    #      # iterate through slices
    #      for current_slice in range(0, total_slices):
    #          # alternate slices and save as png
    #          print('Saving image...')
    #          image_name = inputfile[:-4] + "_t" + "{:0>3}".format(str(current_volume + 1)) + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
    #          imageio.imwrite(image_name, data)
    #          print('Saved.')
    #
    #          # move images to folder
    #          print('Moving files...')
    #          src = image_name
    #          shutil.move(src, outputfile)
    #          slice_counter += 1
    #          print('Moved.')
    #
    #  print('Finished converting images')

    # else if 3D image inputted
    if len(image_array.shape) == 3:
        # set 4d array dimension values
        nx, ny, total_slices = image_array.shape

        print('Reading NIfTI file...')

        # iterate through slices
        for slice_counter in range(0, total_slices):
            # iterate slices and save as png
            current_slice = image_array[:, :, slice_counter]
            current_slice = convert_to_uint8(current_slice)
            print('Saving image...')
            image_name = os.path.basename(inputfile)[:-4] + "_z" + "{:0>3}".format(str(slice_counter)) + ".png"
            imageio.imwrite(os.path.join(outputfolder, image_name), current_slice)
            print('Saved.')

        print('Finished converting images')
    else:
        print('Not a 3D or 4D Image. Please try again.')


# call the function to start the program
if __name__ == "__main__":
    main()
