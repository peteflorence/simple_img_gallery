import os
import sys

# parse argument for image directory
if len(sys.argv) > 1:
    img_dir = sys.argv[1]
else:
  print "Need to provide directory of images as argument, for example:"
  print "python generate_gallery.py sample_images"
  quit()

html_file = os.path.join(img_dir, "index.html")
target = open(html_file, 'w')

def write_html_header(target):
  target.write("<html><head><title>Image Gallery</title></head><body><center>")
  target.write("\n")

def write_html_footer(target):
  target.write("</center></body></html>")
  target.write("\n")

def write_img_to_html(filename_full_path, target):
  target.write('<a href="/home/peteflo"><img src="' + filename_full_path +  '" style="float: left; width: 30%; margin-right: 1%; margin-bottom: 0.5em;" ></a>')
  target.write("\n")

def create_gallery(dir_name, target):
  cwd = os.getcwd()
  path_to_dir = cwd + "/" + dir_name
  for root, dirs, files in os.walk(path_to_dir):
      for filename in sorted(files):
          filename_full_path = os.path.join(root, filename)
          if filename_full_path.endswith(".jpg"):
              print "found .jpg match: " + filename_full_path
              write_img_to_html(filename_full_path, target)

write_html_header(target)
create_gallery(img_dir, target)
write_html_footer(target)

target.close()

# view gallery
os.system("firefox " + html_file)