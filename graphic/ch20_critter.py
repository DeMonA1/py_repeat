from PIL import Image


critter = Image.open('./photo.jpg').convert("RGBA")
stache = Image.open('./cropped.gif').convert("RGBA")
stache.putalpha(100)
img = Image.new('RGBA', critter.size, (255, 255, 255, 0))
img.paste(critter, (0, 0))
img.paste(stache, (45, 90), mask=stache)
img.show()