from math import *


def f(mu, sigma2, x):
    return 1 / sqrt(2.0 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)


def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


measurements = [5.0, 6.0, 7.0, 9.0, 10.0]
motion = [1.0, 1.0, 2.0, 1.0, 1.0]
measurement_sig = 4.0
motion_sig = 2.0
mu = 0.0
sig = 10000.0

print(f(10.0, 4.0, 8.0))
print(update(10.0, 8.0, 13.0, 2.0))
print(predict(10.0, 4.0, 12.0, 4.0))

for n in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[n], measurement_sig)
    print("update: {}".format([mu, sig]))
    [mu, sig] = predict(mu, sig, motion[n], motion_sig)
    print("predict {}".format([mu, sig]))
