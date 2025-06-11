class Task:
    mass_cost = energy_cost = build_time = 0.0

    def __init__(self, label: str):
        self.label = label
        self.internal_b_power = 0
        self.done = False
        self.done_bt = 0.0

    def mass_per_second(self):
        return self.mass_cost / self.build_time

    def energy_per_second(self):
        return self.energy_cost / self.build_time

    def advance(self, dt: float, k, total_bp):
        self.done_bt += k * total_bp
        if self.done_bt >= self.build_time:
            self.done = True

    def finished(self, sim):
        pass


class Task_upgrade_mex(Task):
    mass_cost = 900.0
    energy_cost = 5400.0
    build_time = 900.0

    def __init__(self, label: str):
        super().__init__(label)
        self.internal_b_power = 10

    def finished(self, sim):
        sim.mass_income += 4.0


class Task_build_storage(Task):
    mass_cost = 200.0
    energy_cost = 1500.0
    build_time = 250.0

    def finished(self, sim):
        sim.mass_income += 0.75

class Task_wait(Task):
    build_time = 1.0
    def __init__(self, label: str = "Wait", delay_time: float = 5.0):
        super().__init__(label)
        self.delay_time = delay_time

    def advance(self, dt: float, k, total_bp):
        self.delay_time -= dt
        self.done = self.delay_time <= 0