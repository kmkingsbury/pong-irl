import evdev
from evdev import InputDevice, categorize, ecodes

gamepad_path = ''

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
  print(device.path, '\n', device.name, '\n', device.phys, '\n')
  if device.name == 'Microsoft X-Box 360 pad':
    gamepad_path = device.path

print(gamepad_path)

#creates object 'gamepad' to store the data
gamepad = InputDevice(gamepad_path)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
  button_press = ''
  if (event.type == ecodes.EV_KEY):
    if event.code == 304:
      print('B down' if event.value == 1 else 'B up')
    elif event.code == 305:
      print('A down' if event.value == 1 else 'A up')
    elif event.code == 314:
      print('Select down' if event.value == 1 else 'Select up')
    elif event.code == 315:
      print('Start down' if event.value == 1 else 'Start up')
  #    print(event.code, event.value);
  if event.type == ecodes.EV_ABS:
    if event.code == 16:
      if event.value == -1:
        button_press = 'left'
      elif event.value == 1:
        button_press = 'right'
    elif event.code == 17:
      if event.value == -1:
        button_press = 'up'
      elif event.value == 1:
        button_press = 'down'

#        print(event.code, event.value)
  if button_press != '':
    print(button_press)