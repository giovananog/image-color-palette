from PIL import Image


def get_colors(filepath, count):
    img = Image.open(filepath)
    colors = img.convert('RGB').getcolors(maxcolors=100000)
    
    counts = [a for (a,_) in colors]
    
    counts.sort()
    rgbs = counts[-count:-1]
    
    return [colors[a][1] for a in rgbs]
