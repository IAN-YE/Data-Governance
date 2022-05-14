import numpy as np
import matplotlib.pyplot as plt

#laplace
def normpdf(x, mu, sigma):
    pdf=np.exp(- np.abs(x - mu) / sigma) / (2 * sigma)
    return pdf



mu = np.arange(0,5,1)
sigma = np.arange(0,5,1)

x, y = [], []

for i in mu:
    x_in = np.arange(-5,5,0.01)
    x.append(x_in)
    y.append(normpdf(x_in,i,1))

print(len(x))
for i in range(len(x)):
    plt.plot(x[i],y[i],linewidth=1, label='mu={},lambda={}'.format(mu[i],1))


plt.title('laplace distribution with different mu')

plt.legend()
plt.grid()
plt.show()
