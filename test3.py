import numpy as np
import matplotlib.pyplot as plt

T = np.array([299.2, 302.2, 306.1, 308.9, 315.5, 321.0,
              298.9, 301.1, 305.6, 310.8, 316.5, 320.7])

P = np.array([20995, 23861, 28126, 31326, 40923, 50521,
              20448, 22661, 27460, 33192, 43323, 49854])

R = 8.314472


x_values = 1 / (R * T)

y_values = np.log(P)

y_err = [np.mean(y_values) * 0.005 for i in y_values]

print("x values:", x_values)
print()
print("y values:", y_values)
print()

x_range = max(x_values) - min(x_values)
y_range = max(y_values) - min(y_values)

x_lims = [min(x_values) - x_range * 0.05, max(x_values) + x_range * 0.05]
y_lims = [min(y_values) - y_range * 0.05, max(y_values) + y_range * 0.05]

plt.xlim(x_lims)
plt.ylim(y_lims)

# plt.scatter(x_values, y_values, marker='.', color='gray')
plt.errorbar(x_values, y_values, yerr=y_err, fmt='.', color='black', capsize=4)


def get_stdev(x, pol, cov):
    # calculate standard deviation from the polynomial fit
    y = np.vstack([x**(len(pol) - 1 - i) for i in range(len(pol))])
    m = np.dot(y.T, np.dot(cov, y))
    return np.sqrt(np.diag(m))


poly, poly_cov = np.polyfit(x_values, y_values, 1, cov=True)

print("Regression:", poly)
print("Variation:", np.diag(poly_cov))

poly_xs = np.linspace(x_lims[0], x_lims[1], 100)
poly_ys = np.polyval(poly, poly_xs)

poly_stdev = get_stdev(poly_xs, poly, poly_cov)

plt.plot(poly_xs, poly_ys, color='black')
plt.fill_between(poly_xs, poly_ys - poly_stdev * 5,
                          poly_ys + poly_stdev * 5, color='black', alpha=0.25)



# plt.xlabel("1 / (R T)")
# plt.ylabel("ln P")

# Sets the x and y labels with tex style math mode
plt.xlabel(r"$\frac{1}{R T}$")
plt.ylabel(r"$\ln{P}$")

# plt.xticks(rotation=30)
# plt.gcf().subplots_adjust(bottom=0.20)

# plt.yticks(rotation=30)
# plt.gcf().subplots_adjust(left=0.20)

# plt.grid(True)

# plt.box(False)

# Removes the top and right walls of the surrounding box
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()


