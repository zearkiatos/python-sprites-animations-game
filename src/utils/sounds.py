import numpy as np
import pygame.sndarray

def generate_laser_beep(start_freq=1500, end_freq=300, duration_ms=200, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duration_ms / 1000)
    t = np.linspace(0, duration_ms / 1000, n_samples, False)

    freqs = np.linspace(start_freq, end_freq, n_samples)
    wave = 32767 * np.sin(2 * np.pi * freqs * t)

    # Convert to stereo
    wave = np.column_stack((wave, wave)).astype(np.int16)

    sound = pygame.sndarray.make_sound(wave)
    sound.set_volume(volume)
    return sound

import numpy as np
import pygame

def generate_space_explosion_beep(duration=0.5, sample_rate=44100):
    pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)

    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Base de ruido blanco fuerte
    noise = np.random.normal(0, 1, t.shape)

    # Añadimos una onda cuadrada baja para un boom metálico
    square_wave = np.sign(np.sin(2 * np.pi * 60 * t))

    # Envoltura tipo explosión con rebote
    envelope = np.exp(-10 * t) + 0.3 * np.exp(-30 * t)

    # Mezclamos y aplicamos distorsión
    wave = (0.7 * noise + 0.3 * square_wave) * envelope
    wave = np.tanh(wave * 2)  # saturación/distorsión

    # Normalizamos
    wave = np.clip(wave, -1, 1)

    # Estéreo
    stereo_wave = np.column_stack((wave, wave))
    stereo_wave = (stereo_wave * 32767).astype(np.int16)

    return pygame.sndarray.make_sound(stereo_wave)