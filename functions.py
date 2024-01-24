from PIL import Image


def get_colors(filepath, count):
    print(filepath)
    img = Image.open(filepath)
    colors = img.convert('RGB').getcolors(maxcolors=1000000)
    
    counts = [a for (a,_) in colors]
    
    counts.sort(reverse=True)
    rgbs = counts[0:int(count)]
    
    return [colors[a][1] for a in rgbs]
