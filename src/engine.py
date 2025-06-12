from dataclasses import dataclass
from .tasks import Task
from .recorder import DataRecorder

@dataclass
class SimConfig:
    mass_income: float = 9.0
    mass_bank: float = 750
    mass_cons_add: float = 0.0
    engineers_bp: int = 10

class Engine:
    def __init__(self, cfg: SimConfig, name_bo: str ,dt: float = 1.0):
        # время
        self.dt   = dt
        self.time = 0.0

        # экономика
        self.mass_income    = cfg.mass_income
        self.energy_income  = 0.0
        self.mass_bank      = cfg.mass_bank
        self.energy_bank    = 0.0
        self.mass_cons_add  = cfg.mass_cons_add
        self.mass_current   = 0.0
        self.energy_current = 0.0

        # очередь задач
        self.queue:   list[Task] = []
        self.current: Task | None = None

        self.engineers_bp = cfg.engineers_bp
        self.rec = DataRecorder(name_bo)
    # --- утилиты ---
    def fmt(self, flag: str) -> str:
        if flag == "start":
            fmt_time = self.time
        elif flag == "end":
            fmt_time = self.time + self.dt
        m, s = divmod(fmt_time, 60)
        return f"{int(m):02d}:{s:04.1f}"

    def enqueue (self, task: Task):
        self.queue.append(task)

    # --- главный шаг симуляции ---
    def step(self):
        # если нет активной задачи – берём следующую из очереди
        if self.current is None and self.queue:
            self.current = self.queue.pop(0)
            print(f"[{self.fmt("start")}] START - {self.current.label}")

        # прирастает масса
        self.mass_bank += self.mass_income * self.dt
        self.mass_current   = 0.0
        self.energy_current = 0.0

        # такт задачи
        if self.current:
            total_bp         = self.engineers_bp + self.current.internal_b_power
            task_need_mass   = self.current.mass_per_second() * total_bp
            task_need_energy = self.current.energy_per_second() * total_bp
            total_need_mass  = task_need_mass + self.mass_cons_add

            if total_need_mass == 0:
                k = 1.0
            else:
                k = min(1.0, self.mass_bank / total_need_mass)
                k = int(k * 100) / 100

            self.mass_bank     -= total_need_mass * k * self.dt
            self.mass_current   = (self.mass_income - (total_need_mass * k)) * self.dt
            self.energy_current = -(task_need_energy * k * self.dt)
            self.current.advance(self.dt, k, total_bp)

            if self.current.done:
                self.current.finished(self)
                print(f"[{self.fmt("end")}] FINISH - {self.current.label}")
                self.current = None

        self.time += self.dt
        print(self.time, self.mass_bank, self.mass_current, self.energy_current)
        self.rec.snap(self.time, self.mass_bank, self.mass_current, self.energy_current)
