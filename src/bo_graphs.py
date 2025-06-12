import matplotlib.pyplot as plt

def plot_comparison(rec1, rec2):
    # Автоопределение имени BO
    name1 = "ОБСТРОЙКА              "
    name2 = "ПОСЛЕДОВАТЕЛЬНО"

    # Время (предполагается одинаковое для обоих)
    time = rec1.time

    # — 1 — Масса в банке
    plt.figure(figsize=(10, 4))
    plt.plot(time, rec1.mass_bank, label=f"{name1} - mass_bank")
    plt.plot(time, rec2.mass_bank, label=f"{name2} - mass_bank")
    plt.title("Масса в банке")
    plt.xlabel("Время (сек)")
    plt.ylabel("Масса")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # — 2 — Баланс масса (приток/отток)
    plt.figure(figsize=(10, 4))
    plt.plot(time, rec1.mass_current, label=f"{name1} - mass_current")
    plt.plot(time, rec2.mass_current, label=f"{name2} - mass_current")
    plt.title("Приток/отток массы")
    plt.xlabel("Время (сек)")
    plt.ylabel("Масса / сек")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # — 3 — Текущая энергия (отрицательная)
    plt.figure(figsize=(10, 4))
    plt.plot(time, rec1.energy_current, label=f"{name1} - energy_current")
    plt.plot(time, rec2.energy_current, label=f"{name2} - energy_current")
    plt.title("Приток/отток энергии")
    plt.xlabel("Время (сек)")
    plt.ylabel("Энергия / сек")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
