from PIL import Image, ImageTk
import tkinter
import matplotlib.pyplot as plot
import matplotlib.image as image


img = Image.open('./photo.jpg')
img.format
img.size
img.mode

crop = (55, 70, 85, 100)
img2 = img.crop(crop)
img2.show()

img2.save('cropped.gif', 'GIF')
img3 = Image.open('cropped.gif')
img3.format
img3.size



main = tkinter.Tk()
img = Image.open('./photo.jpg')
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()



img = image.imread('./photo.jpg')
plot.imshow(img)
plot.show()