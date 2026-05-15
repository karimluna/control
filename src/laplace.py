import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from utils import _set_style

_set_style()

sigma = 0.5  # growth rate (positive: unstable)
omega = 10.0 # frequency of oscillation
t = np.linspace(0, 5, 500)

# f(t) = e^(0.5t) * sin(10t)
signal = np.exp(sigma * t) * np.sin(omega * t)
envelope = np.exp(sigma * t) 


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 2.8))

ax1.plot(t, signal, lw=1.2, color='black', label='Signal')
ax1.plot(t, envelope, '--', color='black', lw=0.8, alpha=0.5, label='Envelope')
ax1.plot(t, -envelope, '--', color='black', lw=0.8, alpha=0.5)
ax1.set_title(r'$e^{\sigma t} \sin(\omega t)$', fontsize=10)
ax1.set_xlabel('$t$')

ax2.axhline(0, color='black', lw=0.8)
ax2.axvline(0, color='black', lw=0.8)
ax2.plot(sigma, omega, 'kx', markersize=7, mew=1.5)  # upper pole
ax2.plot(sigma, -omega, 'kx', markersize=7, mew=1.5) # lower pole

ax2.set_title('s-Plane: Poles in RHP', fontsize=10)
ax2.set_xlabel(r'$\sigma$ (Real)')
ax2.set_ylabel(r'$j\omega$ (Imag)')

ax2.set_xlim([-2, 2])
ax2.set_ylim([-15, 15])

plt.tight_layout()
plt.savefig("./figures/laplace.pdf")
plt.show()