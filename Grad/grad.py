__author__ = 'wolfram'

x0 = 0.25
y0 = 0.25
h = 0.002

x = x0
y = y0
k = 10000

for i in range(k):
    gradx = 2 * (200 * x * x * x - 200 * x * y + x - 1)
    grady = 200 * (y - x * x)
    x = x - h * gradx
    y = y - h * grady

print(x, ' ', y)