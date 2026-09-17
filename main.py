from presenters.alarm_presenter import AlarmPresenter
from scheduler.alarm_scheduler import AlarmScheduler
from views.alarm_view import AlarmView


def main():
    view = AlarmView()

    scheduler = AlarmScheduler(
        on_alarm_triggered=view.show_triggered_alarm
    )

    presenter = AlarmPresenter(
        view=view,
        scheduler=scheduler,
    )

    presenter.start()

    print("Goodbye!")


if __name__ == "__main__":
    main()