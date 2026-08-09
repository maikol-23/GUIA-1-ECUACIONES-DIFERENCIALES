import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación autónoma dP/dt = 3P - 2P^2
def dP_dt(P):
    return 3 * P - 2 * P**2

# Puntos críticos
crit_pts = [0, 1.5]
stability = ['unstable', 'stable']

fig, ax = plt.subplots(figsize=(9, 2.5))

# Dibujar eje horizontal (Población P en miles)
P_vals = np.linspace(-0.2, 2.2, 500)
ax.axhline(0, color='black', lw=2)
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.4, 0.4)
ax.axis('off')

# Flujos (dirección de flechas)
intervals = [((-0.2, 0), -1), ((0, 1.5), 1), ((1.5, 2.2), -1)]
for (start, end), direction in intervals:
    mid = (start + end) / 2
    arrow = "→" if direction > 0 else "←"
    ax.text(mid, 0.08, arrow * 3, ha='center', va='center', fontsize=18, color='navy', fontweight='bold')

# Graficar puntos críticos
for pt, st in zip(crit_pts, stability):
    if st == 'stable':
        ax.plot(pt, 0, 'o', color='crimson', markersize=12, zorder=5)
        tag = "Estable (1500 ej.)"
    else:
        ax.plot(pt, 0, 'o', color='crimson', markerfacecolor='white', markeredgewidth=2, markersize=12, zorder=5)
        tag = "Inestable (0 ej.)"
        
    ax.text(pt, -0.18, f"P = {pt}\n({tag})", ha='center', va='top', fontsize=10, fontweight='bold')

ax.set_title("Diagrama de Fase - Población P (en miles)", fontsize=12, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig("diagrama_fase_poblacion.png", dpi=300, bbox_inches='tight')
plt.show()
