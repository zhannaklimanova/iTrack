import io_automation 

key_pressed = None

while key_pressed != 'a' or key_pressed != 'p':
    key_pressed = input("Enter key: ")
    if key_pressed == 'k':
        io_automation.play_pause(2765, 502, 789, 877)
    else:
        print("Press either the key 'p' for play or 'a' for pause.")