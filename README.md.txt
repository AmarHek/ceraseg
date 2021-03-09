# CT-Segmentation

This is a little side project with CT data from the Fraunhofer institute.
The data are 3D CT-scans of ceramics with cracks and other errors, which need to be detected.

The goal of this project is to create one or more models with the existing data in order
to figure out if this project can be properly realized.

## Data

The data contains xy amount of 3D-scans of ceramics in NIfTI format. They can be opened using the NiBabel library for python.
Included with the original images are manual segmentation masks for training and testing purposes.

## Models

We want to try out both 3D- and 2D-based models. 3D-models will take the entire scan, possibly
sliced up due to memory restrictions, whereas 2D-models will work on a slice-by-slice basis.
There are several pre-built architectures for both methods, but only 2D has pre-trained models.