from PIL import Image
import os

font = "dfont_lrg"
image = Image.open(font+".png")

mapchar_data = []
inside_mapchar = False

with open(font + '.kfont', 'r') as file:
    for line in file:
        line = line.strip()
        if line == "mapchar":  # Start reading when "mapchar" is found
            inside_mapchar = True
            continue  # Skip the "mapchar" line itself
        
        if inside_mapchar:
            if line == "}":  # Stop when "mapchar" section ends
                break
            if line == "{":
                continue
            mapchar_data.append(line)

try:
    os.mkdir("output")
except FileExistsError:
    print("Output path already exists. Continuing...")

for data in mapchar_data:
    id = data.split(" ")[0]

    print("parsing " + id + "..")
    
    offset_x = int(data.split(" ")[1].split(" ")[0])
    offset_y = int(data.split(" ")[2].split(" ")[0])
    size_x = int(data.split(" ")[3].split(" ")[0])
    size_y = int(data.split(" ")[4].split(" ")[0])
    unk = int(data.split(" ")[5].split(" ")[0])

    bounds = (offset_x, offset_y, offset_x + size_x, offset_y + size_y)

    try:
        cropped = image.crop(bounds)
        cropped.save("output/"+id+".png")
    except:
        print("Error saving "+id+".png")
