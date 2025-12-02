import tkinter as tk
import random
import threading
import time


def show_warm_tip():
    # Create window
    window = tk.Tk()
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Random window position (ensure window fully visible)
    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    # Set window title and position
    window.title("宝宝")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # Tip texts
    tips = ['我想你了', '今天过得开心嘛', '期待和你见面', '顺顺利利', '早点休息', '天冷了，多穿衣服','今天有想我吗']
    tip = random.choice(tips)
    # Background colors
    bg_colors = ['pink', 'skyblue', 'green', 'lavender', 'lightyellow', 'plum', 'coral', 'bisque', 'lavenderblush', 'oldlace']
    bg = random.choice(bg_colors)
    # Create label and display text
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=("Microsoft YaHei", 16),
        width=30,
        height=3
    ).pack()
    # Keep window always on top
    window.attributes('-topmost', True)
    window.mainloop()


# Create thread list
threads = []
# Number of windows (adjustable based on screen size)
for i in range(300):
    t = threading.Thread(target=show_warm_tip)
    threads.append(t)
    time.sleep(0.005)  # Quickly pop up windows
    threads[i].start()