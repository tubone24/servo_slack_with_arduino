# servo_slack_with_arduino

## background

Since it is necessary to freely move the Arduino servo motor with Slash command from Slack, create a command line tool.

## Usage

```
Overview:
  Run Arduino Servo from the command line
Usage:
  main.py [-h|--help] [-v|--version]
  main.py move <angle> [--port <port>] [--baudrate <baudrate>]
  main.py wipe <delay> <time> [--port <port>] [--baudrate <baudrate>]

Options:
  move           : move a servo
  <angle>        : the angle to movie a servo
  <delay>        : delay time wiping servo
  <time>         : wipe repeat time
  -h, --help     : show this help message and exit
  -v, --version  : show version
  --baudrate     : baudrate with serial comm
  --port         : port with serial comm
```

## demo

![demo](docs/images/arduino.gif)
