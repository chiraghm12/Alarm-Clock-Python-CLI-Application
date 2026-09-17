class AlarmView:

    def display_menu(self):
        print("\n================================")
        print("       PYTHON ALARM CLOCK")
        print("================================")
        print("1. Add Alarm")
        print("2. List Alarms")
        print("3. Delete Alarm")
        print("4. Exit")

    def get_choice(self):
        return input("Enter your choice: ").strip()

    def get_alarm_time(self):
        return input("Enter alarm time (HH:MM): ").strip()

    def get_alarm_label(self):
        return input("Enter alarm label: ").strip()

    def get_alarm_id(self):
        return input("Enter alarm ID to delete: ").strip()

    def show_message(self, message):
        print(message)

    def show_alarms(self, alarms):
        if not alarms:
            print("\nNo alarms found.")
            return

        print("\nID   Time    Label")
        print("-----------------------------")

        for alarm in alarms:
            print(f"{alarm.id:<4} {alarm.time:<7} {alarm.label}")

    def show_triggered_alarm(self, alarm):
        print("\n================================")
        print("        ALARM TRIGGERED!")
        print("================================")
        print(f"Time: {alarm.time}")
        print(f"Label: {alarm.label}")
        print("================================")