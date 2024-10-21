value = 0
irRemote.connect_infrared(DigitalPin.P16)

def on_forever():
    global value
    value = irRemote.return_ir_button()
    if value == 70:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
    elif value == 68:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
    elif value == 67:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
    elif value == 21:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
    elif value == 64:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
basic.forever(on_forever)
