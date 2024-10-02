from matplotlib import pyplot

def f1(x):
    return 2 * (x**2) + 5*x - 2

def f2(x):
    return 4*x + 1

x = range(-10, 15, 1)

pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])

pyplot.axhline(0, color='black')
pyplot.axvline(0, color='black')

pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)

pyplot.savefig('output.png')

pyplot.title('Trabajo de Santiago Cacho')
pyplot.show()