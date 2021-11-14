# heightmap 1D
import random
import matplotlib.pyplot as plt

axislimits = [0, 20, 0, 4]
width = 1
fig, axs = plt.subplots(4)

# 1 - valleys
# 2 - hills
# 3 - mountains

# distribuzione uniforme (flat, rumore bianco)
# è una distribuzione uniforme perché non viene privilegiato un tipo di variazione (lunga o breve) ma tutti i dati sono casuali
def flat_rnd():
    return [random.randint(1, 3) for i in range(20)]

def valleys_rnd():
    # valli più comuni
    return [random.randint(1, random.randint(1, 3)) for i in range(20)]

# filtro passa basso discreto
# prendendo il min() tra due elementi sto privilegiando i set di dati "costanti" a discapito dei set di dati "molto variabili"
# ad esempio verranno mangiati punti sull'array che variano molto e verranno appiattiti
# i set di dati sull'array che non variano rimarranno uguali anche dopo n applicazioni del filtro
# il filtro mangia informazioni, dopo averlo applicato 3 volte si vede sul grafico che i set di dati costanti si riducono
def lowpass_filter(dist):
    output = []
    for i in range(len(dist) - 1):
        output.append(min(dist[i], dist[i+1]))
    return output 


noise_flat = flat_rnd()
# valleys_dist = valleys_rnd()
noise_flattened_0 = lowpass_filter(noise_flat)
noise_flattened_1 = lowpass_filter(noise_flattened_0)
noise_flattened_2 = lowpass_filter(noise_flattened_1)

#flatdist
axs[0].bar(range(len(noise_flat)), noise_flat, align='edge', width=width)
axs[0].set_title('flat dist')
axs[0].axis(axislimits)
axs[0].xaxis.set_visible(False)

#noised_dist_0 dist
axs[1].bar(range(len(noise_flattened_0)), noise_flattened_0, align='edge', width=width)
axs[1].set_title('noised_dist_0')
axs[1].axis(axislimits)
axs[1].xaxis.set_visible(False)

#noised_dist_1
axs[2].bar(range(len(noise_flattened_1)), noise_flattened_1, align='edge', width=width)
axs[2].set_title('noised_dist_1')
axs[2].axis(axislimits)
axs[2].xaxis.set_visible(False)

#noised_dist_2
axs[3].bar(range(len(noise_flattened_2)), noise_flattened_2, align='edge', width=width)
axs[3].set_title('noised_dist_2')
axs[3].axis(axislimits)
axs[3].xaxis.set_visible(False)

fig.suptitle('1D heightmap')

# function to show the plot
plt.show()
