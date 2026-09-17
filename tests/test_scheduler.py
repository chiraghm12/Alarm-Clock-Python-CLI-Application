from datetime import datetime
from unittest.mock import patch

from models.alarm import Alarm
from scheduler.alarm_scheduler import AlarmScheduler


def test_add_alarm():
    triggered = []

    scheduler = AlarmScheduler(
        on_alarm_triggered=triggered.append
    )

    alarm = Alarm(
        id=1,
        time="07:30",
        label="Wake Up",
    )

    scheduler.add_alarm(alarm)

    assert len(scheduler.get_alarms()) == 1
    assert scheduler.get_alarms()[0] == alarm


def test_delete_alarm():
    scheduler = AlarmScheduler(
        on_alarm_triggered=lambda alarm: None
    )

    alarm = Alarm(
        id=1,
        time="07:30",
        label="Wake Up",
    )

    scheduler.add_alarm(alarm)

    assert scheduler.delete_alarm(1) is True
    assert scheduler.get_alarms() == []


def test_delete_non_existing_alarm():
    scheduler = AlarmScheduler(
        on_alarm_triggered=lambda alarm: None
    )

    assert scheduler.delete_alarm(999) is False


def test_alarm_triggers_when_time_matches():
    triggered = []

    scheduler = AlarmScheduler(
        on_alarm_triggered=triggered.append
    )

    alarm = Alarm(
        id=1,
        time="07:30",
        label="Wake Up",
    )

    scheduler.add_alarm(alarm)

    fake_time = datetime(2026, 9, 18, 7, 30)

    with patch(
        "scheduler.alarm_scheduler.datetime"
    ) as mock_datetime:

        mock_datetime.now.return_value = fake_time

        scheduler._check_alarms()

    assert len(triggered) == 1
    assert triggered[0] == alarm
    assert alarm.triggered is True


def test_alarm_does_not_trigger_at_wrong_time():
    triggered = []

    scheduler = AlarmScheduler(
        on_alarm_triggered=triggered.append
    )

    alarm = Alarm(
        id=1,
        time="07:30",
        label="Wake Up",
    )

    scheduler.add_alarm(alarm)

    fake_time = datetime(2026, 9, 18, 7, 31)

    with patch(
        "scheduler.alarm_scheduler.datetime"
    ) as mock_datetime:

        mock_datetime.now.return_value = fake_time

        scheduler._check_alarms()

    assert triggered == []