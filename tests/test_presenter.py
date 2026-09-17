from presenters.alarm_presenter import AlarmPresenter


def test_valid_time():
    assert AlarmPresenter._is_valid_time("07:30") is True
    assert AlarmPresenter._is_valid_time("23:59") is True


def test_invalid_time():
    assert AlarmPresenter._is_valid_time("25:30") is False
    assert AlarmPresenter._is_valid_time("07:70") is False
    assert AlarmPresenter._is_valid_time("abc") is False
    assert AlarmPresenter._is_valid_time("07") is False