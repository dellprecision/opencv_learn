import autopy
import time

autopy.mouse.move(100, 100) # 移动鼠标
autopy.mouse.smooth_move(400, 400) # 平滑移动鼠标（上面那个是瞬间的）
time.sleep(5)
autopy.mouse.smooth_move(1450, 400) # 平滑移动鼠标（上面那个是瞬间的）
time.sleep(1)
autopy.mouse.smooth_move(1450, 600) # 平滑移动鼠标（上面那个是瞬间的）
time.sleep(1)
autopy.mouse.smooth_move(1650, 600) # 平滑移动鼠标（上面那个是瞬间的）
time.sleep(1)
autopy.mouse.smooth_move(1650, 400) # 平滑移动鼠标（上面那个是瞬间的）
time.sleep(1)
autopy.mouse.smooth_move(1450, 400) # 平滑移动鼠标（上面那个是瞬间的）
