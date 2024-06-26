import matplotlib.pyplot as plt

all =  ((0, 0), (3,5), (6, 2), (9, 8), (14, 10))
x = []
y = []
for i in all:
    x.append(i[0])
    y.append(i[1])

flg, plots = plt.subplots(nrows=1, ncols=3)

ticks = list(range(0,15,2))
for plot in plots:
    plot.set_xticks(ticks)
    plot.set_yticks(ticks)

plots[0].scatter(x,y)
plots[1].plot(x,y)
plots[2].plot(x,y, 'o-')

plt.show()