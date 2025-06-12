from src.engine import Engine, SimConfig
from src.bo_factory import bo_mex_upgrade_together_storage, bo_mex_upgrade_then_storage
from src.bo_graphs import plot_comparison

#______________________________
# НАСТРОЙКА
START_MASS_INCOME = 9.0
START_MASS_BANK = 500
ENGINEERS = 4
COUNT_MEX = 4
DELAY_TIME = 5          # Время передвижения инженеров
END_TIME = 900          # Время провдеение симуляции

MASS_CONS_ADD = 5.0     # Дополнительная трата массы (с коэффициентом k)
#______________________________

cfg = SimConfig(
    mass_income = START_MASS_INCOME,
    mass_bank = START_MASS_BANK,
    mass_cons_add = MASS_CONS_ADD,
    engineers_bp = 5 * ENGINEERS
)

# с моментальной обстройкой мексов
print("Обстройка: ")
sim_1 = Engine(cfg=cfg, name_bo=f"together_bo_{COUNT_MEX}_bank_{START_MASS_BANK}_engineers_{ENGINEERS}_time_{DELAY_TIME}_add_{MASS_CONS_ADD}")
bo = bo_mex_upgrade_together_storage(COUNT_MEX, DELAY_TIME)

for task in bo:
    sim_1.enqueue(task)

for _ in range(END_TIME):
    sim_1.step()

print(sim_1.fmt("start"), " - ", sim_1.time)
print(sim_1.mass_bank)

# sim_1.rec.save()
print("_____________________")
# ___________________________________
# с последовательной обстройкой мексов
print("Последовательно: ")
sim_2 = Engine(cfg=cfg, name_bo=f"then_bo_{COUNT_MEX}_bank_{START_MASS_BANK}_engineers_{ENGINEERS}_time_{DELAY_TIME}_add_{MASS_CONS_ADD}")
bo = bo_mex_upgrade_then_storage(COUNT_MEX, DELAY_TIME)

for task in bo:
    sim_2.enqueue(task)

# while sim_2.queue or sim_2.current:
#     sim_2.step()

for _ in range(END_TIME):
    sim_2.step()

print(sim_2.fmt("start"), " - ", sim_2.time)
print(sim_2.mass_bank)

# sim_2.rec.save()
print("_____________________")
print("Итоги")
print(f"Обстройка: {round(sim_1.mass_bank, 2)}, Последовательно: {round(sim_2.mass_bank, 2)}")

plot_comparison(sim_1.rec, sim_2.rec)