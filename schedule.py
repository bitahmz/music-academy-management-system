import json
class Schedule:
    def __init__(self):
        # 5 days, 4 time slots
        self.matrix = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]

        self.days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        self.times = ["10-12", "12-14", "14-16", "16-18"]
    def show_schedule(self):
        print("\nWeekly Schedule:\n")

        print("       ", end="")
        for t in self.times:
            print(f"{t:^12}", end="")
        print()

        for i, day in enumerate(self.days):
            print(f"{day:<10}", end="")
            for j in range(len(self.times)):
                cell = self.matrix[i][j]
                if cell == "":
                    print(f"{'---':^12}", end="")
                else:
                    print(f"{cell:^12}", end="")
            print()
    def add_class(self, day_index, time_index, info):
        self.matrix[day_index][time_index] = info
    def save_to_file(self):
        with open("schedule.json", "w", encoding="utf-8") as f:
            json.dump(self.matrix, f)
    def load_from_file(self):
        try:
            with open("schedule.json", "r", encoding="utf-8") as f:
                self.matrix = json.load(f)
        except FileNotFoundError:
            pass