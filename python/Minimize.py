import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import optimize

sys.path.append(".")

# minimizing a function

# set minimization method
method = "Brent"

if "--Golden" in sys.argv:
	method = "Golden"

# function to be minimized: 2*sin(x) + sin(x^2) on the interval 0 to 8

def minfunc(x):
	return x + np.power((x-5), 4)

# x values
x = np.linspace(4, 6, 1000)

# minimize the function, save the results. use brent's method by default
if (method == "Golden"):
	res = optimize.minimize_scalar(minfunc, method=method)
else:
	res = optimize.minimize_scalar(minfunc)

print("The minimum of x+(x-5)^4 by {} method is: {}".format(method, res["x"]))

# show the results
fig = plt.figure(figsize=(10, 8))
plt.plot(x, minfunc(x), label=r"$x + (x-5)^4$")
plt.axvline(res["x"], c="k", ls="--", label="Minimum: {:.3f}".format(res["x"]))
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Convex Function and its Minimum: {} Method".format(method))
plt.show()
fig.savefig("min_function.jpg", dpi=180)