import pyautogui

def play_pause(mouseXClick, mouseYClick, mouseXReturn, mouseYReturn):
    pyautogui.moveTo(mouseXClick, mouseYClick)
    pyautogui.click(mouseXClick, mouseYClick)
    pyautogui.moveTo(mouseXReturn, mouseYReturn)
    pyautogui.click(mouseXReturn, mouseYReturn)


