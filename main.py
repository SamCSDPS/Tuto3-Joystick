def on_forever():
    serial.write_line("" + str((pins.analog_read_pin(AnalogPin.P1))))
    basic.pause(100)
basic.forever(on_forever)
