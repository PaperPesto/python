# frequency colors
import random
import matplotlib.pyplot as plt

axislimits = [0, 20, -3, 3]
width = 1
fig, axs = plt.subplots(4)

# generatore di rumore bianco
def white_noise():
    return [random.uniform(0, +3) for i in range(20)]

# filtro passa-basso, produce rumore rosso
def smoother(noise):
    output = []
    for i in range(len(noise) - 1):
        output.append(0.5 * (noise[i] + noise[i+1]))
    return output

# filtro passa-alto, produce rumore blu
def rougher(noise):
    output = []
    for i in range(len(noise) - 1):
        output.append(abs(0.5 * (noise[i] - noise[i+1])))
    return output


whitenoise = white_noise()
smoothnoise = smoother(whitenoise)
roughernoise_0 = rougher(whitenoise)
roughernoise_1 = rougher(roughernoise_0)

# white noise
axs[0].bar(range(len(whitenoise)), whitenoise, align='edge', width=width)
axs[0].set_title('white noise')
axs[0].axis(axislimits)
axs[0].xaxis.set_visible(False)

# smoother noise
axs[1].bar(range(len(smoothnoise)), smoothnoise, align='edge', width=width)
axs[1].set_title('smoother noise')
axs[1].axis(axislimits)
axs[1].xaxis.set_visible(False)

# roughed noise 0
axs[2].bar(range(len(roughernoise_0)), roughernoise_0, align='edge', width=width)
axs[2].set_title('roughernoise_0')
axs[2].axis(axislimits)
axs[2].xaxis.set_visible(False)

# roughed noise 1
# non mi torna perché si abbassa parecchio la distribuzione...
axs[3].bar(range(len(roughernoise_1)), roughernoise_1, align='edge', width=width)
axs[3].set_title('roughernoise_1')
axs[3].axis(axislimits)
axs[3].xaxis.set_visible(False)

fig.suptitle('frequency colors')

# function to show the plot
plt.show()
