import numpy as np
import matplotlib.pyplot as plt


T = np.array([299.2, 302.2, 306.1, 308.9, 315.5, 321.0,
              298.9, 301.1, 305.6, 310.8, 316.5, 320.7])

P = np.array([20995, 23861, 28126, 31326, 40923, 50521,
              20448, 22661, 27460, 33192, 43323, 49854])
#



x_values = 1 / T

y_values = np.log(P)

y_err = [np.mean(y_values) * 0.005 for i in y_values]

# print(x_values)
# print(y_values)

plt.scatter(x_values, y_values, marker='.', color='k')
# plt.errorbar(x_values, y_values,
#         	yerr=y_err, fmt='.', capsize=4, color='k')

x_range = max(x_values) - min(x_values)
y_range = max(y_values) - min(y_values)

x_lims = [min(x_values) - x_range * 0.05, max(x_values) + x_range * 0.05]
y_lims = [min(y_values) - y_range * 0.05, max(y_values) + y_range * 0.05]

plt.xlim(x_lims)
plt.ylim(y_lims)

def get_stdev(x, pol, cov):
    # calculate standard deviation from the polynomial fit
    y = np.vstack([x**(len(pol) - 1 - i) for i in range(len(pol))])
    m = np.dot(y.T, np.dot(cov, y))
    return np.sqrt(np.diag(m))

poly, cov = np.polyfit(x_values, y_values, 1, cov=True)

# np.polyval(poly, x)

print(poly)
print(np.diag(cov))

poly_x = np.linspace(x_lims[0], x_lims[1], 100)
poly_y = np.polyval(poly, poly_x)

poly_stdev = get_stdev(poly_x, poly, cov)

plt.plot(poly_x, poly_y, color='k')
plt.fill_between(poly_x, poly_y - poly_stdev * 5,
                 poly_y + poly_stdev * 5, color = 'k', alpha=0.25)


plt.xlabel(r"$\frac{1}{R T}$")
plt.ylabel(r"$\ln{P}$")


ticks = np.linspace(x_lims[0], x_lims[1], 5)



plt.xticks(ticks, np.round(ticks * 1000, 3), rotation=30)
plt.gcf().subplots_adjust(bottom=0.20)


plt.plot([0.0003, 0.00032], [9, 4], '--')

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# plt.xscale("log")

plt.show()

plt.cla()
plt.clf()

plt.show()
