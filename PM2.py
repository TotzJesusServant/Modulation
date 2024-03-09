import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan sinyal modulasi
def modulating_signal(t):
    return np.sin(2 * np.pi * 1 * t)  # Contoh sinyal modulasi sinusoidal dengan frekuensi 1 Hz

# Fungsi untuk menghasilkan sinyal carrier
def carrier_signal(t):
    carrier_frequency = 10  # Frekuensi carrier (contoh: 10 Hz)
    return np.cos(2 * np.pi * carrier_frequency * t)

# Fungsi untuk menghasilkan sinyal carrier yang dimodulasi fase
def phase_modulated_signal(t, modulation_index):
    modulation_signal = modulating_signal(t)
    return np.cos(2 * np.pi * 10 * t + modulation_index * modulation_signal)

# Waktu sampling
t = np.linspace(0, 1, 1000)

# Modulasi PM dengan indeks modulasi 1
modulation_index = 1
pm_signal = phase_modulated_signal(t, modulation_index)

# Sinyal modulasi (pesan)
modulating = modulating_signal(t)

# Sinyal carrier
carrier = carrier_signal(t)

# Plot sinyal PM, modulating, dan carrier
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, pm_signal, label='PM Signal', color='red')
plt.title('Phase Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, modulating, label='Modulating Signal', color='blue')
plt.title('Modulating Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, carrier, label='Carrier Signal', color='green')
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
