import os
import sys

# parse argument for image directory
if len(sys.argv) > 1:
    img_dir = sys.argv[1]
    if img_dir.startswith("./"):
      img_dir = os.path.join(os.getcwd(), img_dir)
else:
  print "Need to provide directory of images as argument, for example:"
  print "python generate_gallery.py sample_images"
  quit()

n_per_row = 3           			 # default to tiling 3 images per row
if len(sys.argv) > 2:
	n_per_row = int(sys.argv[2])
width = str(100/n_per_row)

html_file = os.path.join(img_dir, "index.html")
target = open(html_file, 'w')

def write_html_header(target):
  target.write("<html><head><title>Image Gallery</title></head><body><center>")
  target.write("\n")

def write_html_footer(target):
  target.write("</center></body></html>")
  target.write("\n")

def write_img_to_html(rel_path, target):
  target.write('<a href='+rel_path+'><img src="' + rel_path +  '" style="float: left; width: '+width+'%; margin-right: 0%; margin-bottom: 0.5em;" ></a>')
  target.write("\n")

def create_gallery(dir_full_path, target):
  for root, dirs, files in os.walk(dir_full_path):
      for filename in sorted(files):
          filename_full_path = os.path.join(root, filename)
          rel_path = os.path.relpath(filename_full_path, dir_full_path)
          if filename_full_path.endswith(".png") or filename_full_path.endswith(".jpg"):
              write_img_to_html(rel_path, target)

write_html_header(target)
create_gallery(img_dir, target)
write_html_footer(target)
target.close()

print "wrote ", html_file
print "opening ..."
os.system("firefox " + html_file)