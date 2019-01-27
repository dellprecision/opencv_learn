import autopy
import time

from autopy.mouse import Button as bt

time.sleep(5)

autopy.mouse.move(200, 200) # 移动鼠标

autopy.mouse.click(bt.LEFT) # 单击(左）
time.sleep(1)

autopy.mouse.toggle(bt.LEFT,True) # 按下左键
time.sleep(3)

autopy.mouse.smooth_move(1700, 950) # 平滑移动鼠标（上面那个是瞬间的）
autopy.mouse.toggle(bt.LEFT,False) # 松开左键
time.sleep(3)

autopy.mouse.smooth_move(1500, 100) # 平滑移动鼠标（上面那个是瞬间的）
autopy.mouse.click(bt.RIGHT) # 单击（右）

time.sleep(3)
autopy.mouse.smooth_move(1400, 650) # 平滑移动鼠标（上面那个是瞬间的）
autopy.mouse.click(bt.RIGHT) # 单击（右）

time.sleep(3)
autopy.mouse.smooth_move(800, 600) # 平滑移动鼠标（上面那个是瞬间的）
autopy.mouse.click(bt.RIGHT) # 单击（右）
