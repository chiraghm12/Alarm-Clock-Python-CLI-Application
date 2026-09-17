import threading
import time
from datetime import datetime

from models.alarm import Alarm


class AlarmScheduler:

    def __init__(self, on_alarm_triggered):
        self.alarms: list[Alarm] = []
        self.lock = threading.Lock()

        self.stop_event = threading.Event()
        self.thread = None

        self.on_alarm_triggered = on_alarm_triggered

    def add_alarm(self, alarm):
        with self.lock:
            self.alarms.append(alarm)

    def get_alarms(self):
        with self.lock:
            return list(self.alarms)

    def delete_alarm(self, alarm_id):
        with self.lock:
            for alarm in self.alarms:
                if alarm.id == alarm_id:
                    self.alarms.remove(alarm)
                    return True

        return False

    def start(self):
        if self.thread and self.thread.is_alive():
            return

        self.stop_event.clear()

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
        )

        self.thread.start()

    def stop(self):
        self.stop_event.set()

        if self.thread:
            self.thread.join(timeout=2)

    def _run(self):
        while not self.stop_event.is_set():
            self._check_alarms()

            self.stop_event.wait(1)

    def _check_alarms(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        with self.lock:
            for alarm in self.alarms:
                if alarm.time == current_time and not alarm.triggered:
                    alarm.triggered = True

                    self.on_alarm_triggered(alarm)

            # Reset alarms when their scheduled time is no longer current.
            for alarm in self.alarms:
                if alarm.time != current_time:
                    alarm.triggered = False