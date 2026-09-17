# Alarm Clock

A lightweight Python alarm clock application built using a simple model-view-presenter structure. It lets users add alarms, list existing alarms, delete them, and receive a trigger when the current time matches a scheduled alarm.

## Features

- Add alarms with a time in HH:MM format
- Attach a label to each alarm
- Display all scheduled alarms
- Delete alarms by ID
- Trigger notifications when an alarm time is reached
- Background scheduler thread checks the time continuously
- Unit tests covering the core model, presenter, and scheduler behavior

## Project Structure

```text
Alarm Clock/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── models/
│   ├── __init__.py
│   └── alarm.py
├── presenters/
│   ├── __init__.py
│   └── alarm_presenter.py
├── scheduler/
│   ├── __init__.py
│   └── alarm_scheduler.py
├── tests/
│   ├── __init__.py
│   ├── test_alarm.py
│   ├── test_presenter.py
│   └── test_scheduler.py
├── views/
│   ├── __init__.py
│   └── alarm_view.py
└── venv/
```

## How It Works

- The `Alarm` model stores alarm data such as ID, time, label, and trigger status.
- The `AlarmView` handles terminal input and output for the user menu.
- The `AlarmPresenter` validates input and coordinates user actions.
- The `AlarmScheduler` runs in a background thread and checks whether any alarm matches the current time.

## Requirements

- Python 3.10 or later
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

You will see a menu like this:

```text
1. Add Alarm
2. List Alarms
3. Delete Alarm
4. Exit
```

## Run Tests

```bash
pytest
```

## Notes

This project is useful for learning Python application structure, threading, and scheduler-based event handling in a simple command-line app.
