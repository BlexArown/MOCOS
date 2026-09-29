import numpy as np
import matplotlib.pyplot as plt

f0 = 5
t_fine = np.linspace(0, 1, 1000)

phases = [0, 90, 180, 270]
plt.figure(figsize=(10, 8))
plt.suptitle('Часть 1 и 2: Сигналы с различными начальными фазами', fontsize=14, fontweight='bold')

for i, ph in enumerate(phases):
    x_ph = 1.0 * np.cos(2 * np.pi * f0 * t_fine + np.radians(ph))

    plt.subplot(2, 2, i + 1)
    plt.plot(t_fine, x_ph, 'b-', linewidth=1.5)
    plt.title(f'$\\Phi = {ph}^\\circ$')
    plt.xlabel('Время (t), с')
    plt.ylabel('Амплитуда (V)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xlim(0, 0.6)

plt.tight_layout()

plt.figure(figsize=(10, 4))

x1 = 2.0 * np.cos(2 * np.pi * f0 * t_fine + np.radians(0))
x2 = 1.5 * np.cos(2 * np.pi * f0 * t_fine + np.radians(60))
x3 = 1.0 * np.cos(2 * np.pi * f0 * t_fine + np.radians(120))
x_sum_same_f = x1 + x2 + x3

plt.plot(t_fine, x_sum_same_f, 'r-', linewidth=2.5, label='Суммарный сигнал $x_{\\Sigma}(t)$')
plt.plot(t_fine, x1, 'g--', alpha=0.5, label='$x_1(t): A=2.0, \\phi=0^\\circ$')
plt.title('Часть 3: Сложение колебаний с одинаковой частотой ($N=3$)', fontsize=12)
plt.xlabel('Время t, сек')
plt.ylabel('Амплитуда, В')
plt.grid(True, linestyle=':')
plt.legend(loc='upper right')
plt.xlim(0, 0.4)

plt.figure(figsize=(10, 5))

t_fourier = np.linspace(0, 1.0, 1000)

def fourier_sum(t, freq, N_harmonics):
    x_f = np.zeros_like(t)
    for n in range(1, N_harmonics + 1):
        coeff = 4.0 / ((2 * n - 1) * np.pi)
        x_f += coeff * np.cos(2 * np.pi * (2 * n - 1) * freq * t - np.pi / 2)
    return x_f

plt.plot(t_fourier, fourier_sum(t_fourier, f0, 1), 'g--', label='1 гармоника ($N=1$)')
plt.plot(t_fourier, fourier_sum(t_fourier, f0, 2), 'm-.', label='2 гармоники ($N=2$)')
plt.plot(t_fourier, fourier_sum(t_fourier, f0, 5), 'c-', label='5 гармоник ($N=5$)')
plt.plot(t_fourier, fourier_sum(t_fourier, f0, 50), 'r-', linewidth=2, label='50 гармоник ($N=50$)')

plt.title('Часть 4: Синтез периодического сигнала (Приближение к меандру)', fontsize=12)
plt.xlabel('Время t, сек')
plt.ylabel('Амплитуда x(t)')
plt.grid(True, linestyle=':')
plt.legend(loc='upper right')
plt.xlim(0, 1.0)

t_exp = np.linspace(0, 1.0, 500)

f_complex = np.exp(2 * np.pi * f0 * 1j * t_exp)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')
ax.grid(True)

x_real = f_complex.real
y_imag = f_complex.imag

ax.plot3D(t_exp, x_real, y_imag, 'r-', linewidth=2, label='Комплексная экспонента $e^{j\\omega t}$')

ax.plot3D(t_exp, x_real, np.zeros_like(t_exp) - 1.2, 'b--', alpha=0.6, label='Проекция Re (Cos)')
ax.plot3D(t_exp, np.zeros_like(t_exp) + 1.2, y_imag, 'g--', alpha=0.6, label='Проекция Im (Sin)')

ax.set_title('Моделирование комплексной экспоненты в 3D пространстве', fontsize=12, fontweight='bold')
ax.set_xlabel('Время (Time)')
ax.set_ylabel('Действительная часть (Real Axis)')
ax.set_zlabel('Мнимая часть (Imag Axis)')
ax.set_ylim(-1.3, 1.3)
ax.set_zlim(-1.3, 1.3)
ax.legend()

plt.show()
