# PHSX815_HW9

This program minimizes the function x+(x-5)^4 using scipy's optimize.minimize_scalar function. The default minimization method is Brent's method. The golden section method can be used by specifying "Golden" in the program arguments, but this method is less efficient. It is usually preferable to use Brent's method.

The program can be called as python python/Minimize.py with the following arguments.

--Brent				(optional) sets the minimization method to Brent's method.
--Golden 			(optional) sets the minimization method to the Golden Section method.

If neither are given, the program will use Brent's method.

The program will print the resulting minimum, and plot the function over the interval [4, 6] and show the minimum with a vertical line. This plot is saved as "min_function.jpg" in the directory.