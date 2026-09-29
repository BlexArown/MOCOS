import numpy as np
import matplotlib.pyplot as plt

A_val = 4                # Амплитуда
omega_0_val = 0.4 * np.pi # Круговая частота (рад/с)
phi_val = 0.25 * np.pi    # Начальная фаза (рад)

T_given = 4              # Заданный период в секундах
time_points = [-1, 3, 7] # Моменты времени для расчета

a_val = 3
b_val = 4

r_poly = 2
theta_poly = np.pi / 3    # Угол в радианах (60 градусов)

print("=" * 70)
print(" РЕЗУЛЬТАТЫ АВТОМАТИЗИРОВАННОГО РАСЧЕТА ЗАДАЧ ЦОС ")
print("=" * 70)

T_calc = (2 * np.pi) / omega_0_val
dt_calc = phi_val / omega_0_val

print(f"1. Параметры гармонического колебания:")
print(f"   - Рассчитанный период T: {T_calc:.3f} сек")
print(f"   - Временной сдвиг максимума dt: {abs(dt_calc):.3f} сек "
      f"({'влево (опережение)' if dt_calc > 0 else 'вправо (запаздывание)'})")

omega_task2 = (2 * np.pi) / T_given
print(f"\n2. Фаза колебания (при T = {T_given} с, omega = {omega_task2/np.pi:.3f}*pi рад/с):")
for t in time_points:
    phase = omega_task2 * t
    phase_normalized = (phase + np.pi) % (2 * np.pi) - np.pi
    print(f"   - При t = {t:2d} с: Полная фаза = {phase:6.3f} рад ({np.degrees(phase):7.1f}°) | "
          f"Главное значение = {phase_normalized:6.3f} рад")

r1 = np.sqrt(a_val**2 + b_val**2)
theta1 = np.arctan2(b_val, a_val)

r2 = np.sqrt(a_val**2 + (-b_val)**2)
theta2 = np.arctan2(-b_val, a_val)

print(f"\n3. Перевод сопряженных комплексных чисел в полярную форму:")
print(f"   - z1 = {a_val} + j{b_val} => полярная форма: {r1:.3f} * e^(j * {theta1:.3f})  "
      f"(угол: {np.degrees(theta1):.1f}°)")
print(f"   - z2 = {a_val} - j{b_val} => полярная форма: {r2:.3f} * e^(j * {theta2:.3f}) "
      f"(угол: {np.degrees(theta2):.1f}°)")

a_converted = r_poly * np.cos(theta_poly)
b_converted = r_poly * np.sin(theta_poly)
print(f"\n4. Перевод из полярной формы в алгебраическую:")
print(f"   - z = {r_poly} * e^(j * {theta_poly/np.pi:.3f}*pi) => алгебраическая форма: "
      f"{a_converted:.3f} + j{b_converted:.3f}")
print("=" * 70)

t_grid = np.linspace(0, 3 * T_calc, 1000)

x_with_phase = A_val * np.cos(omega_0_val * t_grid + phi_val)
x_zero_phase = A_val * np.cos(omega_0_val * t_grid)

plt.figure(figsize=(10, 5))

plt.plot(t_grid, x_zero_phase, 'g--', label=f'С нулевой фазой: $x_0(t) = {A_val}\\cos({omega_0_val/np.pi:.1f}\\pi t)$', alpha=0.6)
plt.plot(t_grid, x_with_phase, 'b-', label=f'Заданный сигнал: $x(t) = {A_val}\\cos({omega_0_val/np.pi:.1f}\\pi t + {phi_val/np.pi:.2f}\\pi)$', linewidth=2)

plt.title('Анализ параметров гармонического колебания в ЦОС', fontsize=12, fontweight='bold')
plt.xlabel('Время t, сек', fontsize=10)
plt.ylabel('Амплитуда x(t)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)

plt.axhline(0, color='black', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='black', linewidth=0.8, alpha=0.5)

plt.legend(fontsize=10, loc='upper right')

plt.xlim(0, 3 * T_calc)

plt.tight_layout()
plt.show()
