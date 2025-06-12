import json
import matplotlib.pyplot as plt

def load_data(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return json.load(f)[0]

def plot_comparison(file1, file2):
    data1 = load_data(file1)
    data2 = load_data(file2)

    # Автоопределение имени BO
    name1 = "ОБСТРОЙКА              "
    name2 = "ПОСЛЕДОВАТЕЛЬНО"

    # Время (предполагается одинаковое для обоих)
    time = data1["time"]

    # — 1 — Масса в банке
    plt.figure(figsize=(10, 4))
    plt.plot(time, data1["mass_bank"], label=f"{name1} - mass_bank")
    plt.plot(time, data2["mass_bank"], label=f"{name2} - mass_bank")
    plt.title("Масса в банке")
    plt.xlabel("Время (сек)")
    plt.ylabel("Масса")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # — 2 — Баланс масса (приток/отток)
    plt.figure(figsize=(10, 4))
    plt.plot(time, data1["mass_current"], label=f"{name1} - mass_current")
    plt.plot(time, data2["mass_current"], label=f"{name2} - mass_current")
    plt.title("Приток/отток массы")
    plt.xlabel("Время (сек)")
    plt.ylabel("Масса / сек")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # — 3 — Текущая энергия (отрицательная)
    plt.figure(figsize=(10, 4))
    plt.plot(time, data1["energy_current"], label=f"{name1} - energy_current")
    plt.plot(time, data2["energy_current"], label=f"{name2} - energy_current")
    plt.title("Приток/отток энергии")
    plt.xlabel("Время (сек)")
    plt.ylabel("Энергия / сек")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Пример запуска
if __name__ == "__main__":
    file1 = "result/together_bo_6_bank_750_engineers_4_time_5_add_8.0.json"
    file2 = "result/then_bo_6_bank_750_engineers_4_time_5_add_8.0.json"
    plot_comparison(file1, file2)
