from models.alarm import Alarm


def test_create_alarm():
    alarm = Alarm(
        id=1,
        time="07:30",
        label="Wake Up",
    )

    assert alarm.id == 1
    assert alarm.time == "07:30"
    assert alarm.label == "Wake Up"
    assert alarm.triggered is False