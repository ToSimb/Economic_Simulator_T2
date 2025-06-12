import json

class DataRecorder:
    """Сохраняет историю ресурсов на каждом такте."""
    def __init__(self, name_bo):
        self.name            = name_bo
        self.time            = []
        self.mass_bank       = []
        self.mass_current     = []
        self.energy_current    = []

    def snap(self, t, bank, m_cur, e_cur):
        self.time.append(t)
        self.mass_bank.append(round(bank, 2))
        self.mass_current.append(m_cur)
        self.energy_current.append(e_cur)

    def save(self):
        file_name = "result/" + self.name + ".json"
        data = []
        data.append({
            "time": self.time ,
            "mass_bank":  self.mass_bank,
            "mass_current": self.mass_current,
            "energy_current": self.energy_current
        })
        with open(file_name, "w", encoding="utf-8-sig") as file:
            json.dump(data, file, indent=2)