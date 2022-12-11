import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

plate_length = 50
max_iter_time = 1000

alpha = 80
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)


u = np.empty((max_iter_time, plate_length, plate_length))

u_initial = 0
#condició inicial de tots el elements 

u_top = 100.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0
#temperatura de les parets limítrofes

u.fill(u_initial)
#creem un array amb 

print("Funció1")

u[:, (plate_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, 1:] = u_bottom
u[:, :, (plate_length-1):] = u_right
#col·loquem el les coordenades de les parets limítrofes 

def calculate(u):
    for k in range(0, max_iter_time-1, 1):
        for i in range(1, plate_length-1, delta_x):
            for j in range(1, plate_length-1, delta_x):
                u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
#iterem utilitzant la nostra formula 
    return u

print("Funció 2")

def plotheatmap(u_k, k):
    # inicialitzem la  funció plt 
    plt.clf()

    plt.title(f"Temperatura en t = {k*delta_t:.3f} segons")
    plt.xlabel("x")
    plt.ylabel("y")

    
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()
    #assignem un color a cada valor de tempeartura i creem la referència amb colobar
    return plt

# Do the calculation here
u = calculate(u)

print("Funció 3")

def animate(k):
    plotheatmap(u[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
anim.save("eq_calor_2d.gif")
#animem l'equació en forma de gif
print("Funció 4!")