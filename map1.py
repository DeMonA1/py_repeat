import shapefile
import sys
from PIL import Image, ImageDraw


def display_shapefile(name, iwidth=500, iheight=500):
    r = shapefile.Reader(name)
    mleft, mbottom, mright, mtop = r.bbox
    # map units
    mwidth = mright - mleft
    mheight = mtop - mbottom
    # convert map units into image units
    hscale = iwidth/mwidth
    vscale = iheight/mheight
    img = Image.new('RGB', (iwidth, iheight), 'white')
    draw = ImageDraw.Draw(img)
    for shape in r.shapes():
        pixels = [
            (int(iwidth - ((mright - x) * hscale)), int((mtop - y) * vscale))
            for x, y in shape.points]
        if shape.shapeType == shapefile.POLYGON:
            draw.polygon(pixels, outline='black')
        elif shape.shapeType == shapefile.POLYGON:
            draw.line(pixels, fill='black')
    img.show()
    
if __name__ == '__main__':
    display_shapefile(sys.argv[1], 700, 700)