import time
import pyautogui
import subprocess

def locate_with_retry(image_path, retries=5, confidence=0.75, delay=1):
    """Tries to locate the image on screen, retrying if not found."""
    for _ in range(retries):
        button = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if button is not None:
            return button
        time.sleep(delay)
    return None

def sign_in(meetingid):
    mid = meetingid
    
    zoom_path = r"C:\Users\HP\AppData\Roaming\Zoom\bin\Zoom.exe"  
    
    subprocess.call(zoom_path)
    time.sleep(5)  
    
   
    print("Looking for the first join button...")
    join_btn1 = locate_with_retry(r'D:\\Year-3 Term-1 Internship\\AI Voice Assistant Project\\New folder\\join-2.png', retries=10)
    
    if join_btn1 is not None:
        pyautogui.moveTo(join_btn1)
        pyautogui.click()
        time.sleep(3)
    else:
        print("First Join button not found!")
        return
    
    pyautogui.write(mid)
    time.sleep(2)
    
   
    print("Looking for the second join button...")
    join_btn2 = locate_with_retry(r'D:\\Year-3 Term-1 Internship\\AI Voice Assistant Project\\New folder\\join-3.png', retries=10)
    
    if join_btn2 is not None:
        pyautogui.moveTo(join_btn2)
        pyautogui.click()
        time.sleep(3)
    else:
        print("Second Join button not found!")
        return

sign_in('750 759 1770')
