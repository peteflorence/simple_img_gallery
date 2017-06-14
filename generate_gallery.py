import os
import sys

# parse argument for image directory
if len(sys.argv) > 1:
    img_dir = sys.argv[1]
    if img_dir.startswith("./"):
      img_dir = os.path.join(os.getcwd(), img_dir)
else:
  print("Need to provide directory of images as argument, for example:")
  print("python generate_gallery.py sample_images")
  quit()

n_per_row = 3           			 # default to tiling 3 images per row
if len(sys.argv) > 2:
	n_per_row = int(sys.argv[2])
width = str(100/n_per_row)

def write_html_header(target):
  target.write("<html><head><title>Image Gallery</title></head><body><center>")
  target.write("\n")

def write_html_footer(target):
  target.write("</center></body></html>")
  target.write("\n")

def write_img_to_html(rel_path, target):
  target.write('<a href='+rel_path+'><img src="' + rel_path +  '" style="float: left; width: '+width+'%; margin-right: 0%; margin-bottom: 0.5em;" ></a>')
  target.write("\n")

def create_gallery_from_dir(dir_full_path):
  html_file = os.path.join(dir_full_path, "index.html")
  target = open(html_file, 'w')
  write_html_header(target)
  for root, dirs, files in os.walk(dir_full_path):
      for filename in sorted(files):
          filename_full_path = os.path.join(root, filename)
          rel_path = os.path.relpath(filename_full_path, dir_full_path)
          if filename_full_path.endswith(".png") or filename_full_path.endswith(".jpg"):
              write_img_to_html(rel_path, target)
  write_html_footer(target)
  return html_file

def create_gallery_from_description(description_full_path):
  target = open("index.html", 'w')
  write_html_header(target)
  with open(description_full_path) as f:
    content = f.readlines()
    content = [x.strip() for x in content] 
    for i in content:
      i = i.split()
      write_img_to_html(i[0], target)

  write_html_footer(target)
  return "index.html"


if img_dir.endswith(".txt"):
  html_file = create_gallery_from_description(img_dir)
else:
  html_file = create_gallery_from_dir(img_dir)

print("wrote ", html_file)
print("opening ...")
os.system("firefox " + html_file)