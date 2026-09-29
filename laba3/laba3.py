import numpy as np
import matplotlib.pyplot as plt

f0 = 5
T = 1.0 / f0
dt = 0.0001
t_period = np.arange(0, T, dt)


def analyze_harmonic(amplitude, phase_deg):
    phi = np.radians(phase_deg)
    x = amplitude * np.cos(2 * np.pi * f0 * t_period + phi)

    an = []
    bn = []
    for n in range(5):
        if n == 0:
            a_n = (1.0 / T) * np.sum(x) * dt * 2
        else:
            a_n = (2.0 / T) * np.sum(x * np.cos(2 * np.pi * n * f0 * t_period)) * dt
        b_n = (2.0 / T) * np.sum(x * np.sin(2 * np.pi * n * f0 * t_period)) * dt
        an.append(a_n)
        bn.append(b_n)

    return np.array(an), np.array(bn)

an_0, bn_0 = analyze_harmonic(amplitude=2.0, phase_deg=0)
an_60, bn_60 = analyze_harmonic(amplitude=2.0, phase_deg=60)

harmonics = np.arange(5)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.stem(harmonics, np.sqrt(an_0**2 + bn_0**2), 'r', markerfmt='ro', basefmt=" ")
ax1.set_title('Амплитудный спектр ($\\phi = 0^\\circ$)')
ax1.set_xlabel('Номер гармоники, n')
ax1.set_ylabel('$A_n$')
ax1.grid(True, linestyle=':')

ax2.stem(harmonics, np.sqrt(an_60**2 + bn_60**2), 'b', markerfmt='bo', basefmt=" ")
ax2.set_title('Амплитудный спектр ($\\phi = 60^\\circ$)')
ax2.set_xlabel('Номер гармоники, n')
ax2.grid(True, linestyle=':')
plt.tight_layout()

tau = 0.05

u_square = np.where(np.abs(t_period - T/2) <= tau/2, 1.0, 0.0)

an_sq = []
for n in range(1, 10):
    a_n = (2.0 / T) * np.sum(u_square * np.cos(2 * np.pi * n * f0 * t_period)) * dt
    an_sq.append(a_n)

plt.figure(figsize=(10, 4))
plt.plot(t_period, u_square, 'k-', linewidth=2, label='Исходный меандр')

for n_harm in [2,4,6]:
    u_synth = np.zeros_like(t_period) + (tau / T)
    for n in range(1, n_harm + 1):
        a_n = (2.0 / T) * np.sum(u_square * np.cos(2 * np.pi * n * f0 * t_period)) * dt
        u_synth += a_n * np.cos(2 * np.pi * n * f0 * t_period)
    plt.plot(t_period, u_synth, label=f'Синтез: {n_harm} гармоник')

plt.title('Часть 2: Синтез прямоугольного сигнала по гармоникам Фурье')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()

f1 = 1.0 / T
k, n = 2, 3

s_k = np.sin(2 * np.pi * k * f1 * t_period)
s_n = np.sin(2 * np.pi * n * f1 * t_period)

integral_ideal = np.sum(s_k * s_n) * dt

integral_truncated = np.sum(s_k[:-15] * s_n[:-15]) * dt

print("=" * 75)
print(" РЕЗУЛЬТАТЫ ПРОВЕРКИ СВОЙСТВА ОРТОГОНАЛЬНОСТИ СИГНАЛОВ ")
print("=" * 75)
print(f"1. Интеграл произведения sin({k}wt)*sin({n}wt) на ПОЛНОМ периоде: {integral_ideal:.6e}")
print(f"   Вывод: Значение стремится к 0 (~{round(integral_ideal)}). Сигналы ОРТОГОНАЛЬНЫ.")
print(f"2. Интеграл на УСЕЧЕННОМ интервале времени (минус 15 точек):   {integral_truncated:.6e}")
print(f"   Вывод: Интеграл НЕ равен 0. Нарушено условие ортогональности.")
print("=" * 75)

plt.show()
