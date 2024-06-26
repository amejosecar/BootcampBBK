import matplotlib.pyplot as plt

from warnings import filterwarnings
filterwarnings('ignore') # Ignorar warnings

def move_spines():
    """Crea la figura de pyplot y los ejes. Mueve las lineas de la izquierda y de abajo
    para que se interseccionen con el origen. Elimina las lineas de la derecha y la de arriba.
    Devuelve los ejes."""
    _, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")

    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")

    return ax

def vect_fig(vecs:list):
    """Genera el gráfico de los vectores en el plano"""
    ax = move_spines()

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid()
    for v in vecs:
        ax.annotate(" ", xy=v, xytext=[0, 0],
                   arrowprops=dict(facecolor="blue",
                                  shrink=0,
                                  alpha=0.7,
                                  width=0.5))
        ax.text(1.1 * v[0], 1.1 * v[1], v)
