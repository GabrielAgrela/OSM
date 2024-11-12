import pyautogui
import pygetwindow as gw
import time

def click_in_firefox():
    try:
        # Find Firefox window
        firefox = gw.getWindowsWithTitle('Firefox')[0]
        
        # Activate and maximize window
        firefox.activate()
        firefox.maximize()
        time.sleep(0.5)
        
        while True:  # Add infinite loop
            #move mouse to watch ad
            pyautogui.moveTo(3200, 500)
            time.sleep(0.1)
            # Faster and smoother scrolling
            pyautogui.scroll(-3000)
            time.sleep(0.2)
            #click watch ad
            pyautogui.click()
            #wait 50s
            time.sleep(50)
            #move mouse to close ad
            pyautogui.moveTo(2420, 828)
            time.sleep(0.1)
            pyautogui.click()
            
            time.sleep(1)  # Small delay between iterations
            
    except IndexError:
        print("Firefox window not found!")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def get_mouse_position():
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")




if __name__ == "__main__":
    # Click at coordinates (200, 500) within the Firefox window
    click_in_firefox()
    #  get mouse position every 1 second
   # while True:
    ##    get_mouse_position()
       # time.sleep(1)

