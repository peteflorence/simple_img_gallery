# simple_img_gallery
The simplest way to make a static image library, with only a little Python, minimal HTML, and nothing else

## Install

None, no dependencies other than Python and Firefox

## Instructions

	python generate_gallery.py ./sample_images

Alternatively, instead of `sample_images`, pass a full path to a directory of images of your choice:

	python generate_gallery.py /path/to/image_directory

Optionally, you can specify the number of images per row, with an argument after the directory path.  (The default is `3`.)  For example, to tile `6` per row:
	
	python generate_gallery.py /path/to/image_directory 6

The script will create an `index.html` in that directory, and view it with Firefox.

Note:

- Currently only supports tiling the images in alphabetical order.

Future features:

- Support randomization, down-sampling