import numpy as np
import matplotlib.pyplot as plt

def f_a(y):
    return y * (3 - y) * (y - 2)

def f_b(y):
    return y**2 - y**3

def f_c(y):
    return (y + 2) * (10 + 3*y - y**2)

incisos = [
    (f_a, [0, 2, 3], (-1, 4), "a)  y' = y(3 - y)(y - 2)"),
    (f_b, [0, 1], (-1, 2), "b)  y' = y² - y³"),
    (f_c, [-2, 5], (-4, 7), "c)  y' = (y + 2)(10 + 3y - y²)")
]

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

for ax, (f, crit_pts, y_lims, title) in zip(axes, incisos):
    y = np.linspace(y_lims[0], y_lims[1], 500)
    dydt = f(y)
    
    ax.plot(y, dydt, color='#1f77b4', lw=2)
    ax.axhline(0, color='black', lw=1, ls='--')
    ax.axvline(0, color='gray', lw=0.5, ls=':')
    
    # Raíces / Puntos críticos
    for cp in crit_pts:
        ax.plot(cp, 0, 'ro', ms=7, zorder=5)
        ax.annotate(f'y = {cp}', (cp, 0), textcoords="offset points", 
                    xytext=(0, 10), ha='center', fontsize=9, fontweight='bold')
    
    # Flechas de dirección sobre el eje
    y_arrows = np.linspace(y_lims[0], y_lims[1], 20)
    for y_val in y_arrows:
        val = f(y_val)
        if abs(val) > 1e-2:
            direction = np.sign(val)
            ax.annotate('', xy=(y_val + direction * 0.12, 0), xytext=(y_val, 0),
                        arrowprops=dict(arrowstyle="->", color="darkgreen", lw=1.5))
            
    ax.set_title(title, fontsize=11)
    ax.set_xlabel('y')
    ax.set_ylabel("y'")
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
