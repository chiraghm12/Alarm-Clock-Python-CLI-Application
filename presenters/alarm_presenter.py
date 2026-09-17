from datetime import datetime

from models.alarm import Alarm


class AlarmPresenter:

    def __init__(self, view, scheduler):
        self.view = view
        self.scheduler = scheduler
        self.next_id = 1

    def add_alarm(self):
        alarm_time = self.view.get_alarm_time()

        if not self._is_valid_time(alarm_time):
            self.view.show_message(
                "Invalid time. Please use HH:MM format."
            )
            return

        label = self.view.get_alarm_label()

        alarm = Alarm(
            id=self.next_id,
            time=alarm_time,
            label=label,
        )

        self.scheduler.add_alarm(alarm)
        self.next_id += 1

        self.view.show_message(
            f"✓ Alarm added successfully! Alarm ID: {alarm.id}"
        )

    def list_alarms(self):
        alarms = self.scheduler.get_alarms()
        self.view.show_alarms(alarms)

    def delete_alarm(self):
        alarm_id = self.view.get_alarm_id()

        try:
            alarm_id = int(alarm_id)
        except ValueError:
            self.view.show_message("Invalid alarm ID.")
            return

        deleted = self.scheduler.delete_alarm(alarm_id)

        if deleted:
            self.view.show_message(
                f"✓ Alarm {alarm_id} deleted successfully."
            )
        else:
            self.view.show_message(
                f"Alarm with ID {alarm_id} not found."
            )

    @staticmethod
    def _is_valid_time(value):
        try:
            datetime.strptime(value, "%H:%M")
            return True
        except ValueError:
            return False

    def start(self):
        self.scheduler.start()

        try:
            while True:
                self.view.display_menu()
                choice = self.view.get_choice()

                if choice == "1":
                    self.add_alarm()

                elif choice == "2":
                    self.list_alarms()

                elif choice == "3":
                    self.delete_alarm()

                elif choice == "4":
                    break

                else:
                    self.view.show_message("Invalid choice.")

        finally:
            self.stop()

    def stop(self):
        self.scheduler.stop()
        self.view.show_message("Stopping alarm scheduler...")