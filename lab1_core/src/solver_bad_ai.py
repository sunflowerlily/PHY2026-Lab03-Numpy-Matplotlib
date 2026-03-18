import math
import numpy as np
import time

def calculate_gravity_potential_slow(grid_size, M1=1.0, M2=0.5, pos1=(-1, 0), pos2=(1, 0)):
    """
    【AI 生成的代码】
    使用了经典的 C 语言思维：双重 for 循环。
    在 Python 中，这被称为“性能毒药”。
    """
    x = np.linspace(-2, 2, grid_size)
    y = np.linspace(-2, 2, grid_size)
    
    # 初始化一个全是 0 的二维数组
    V = np.zeros((grid_size, grid_size))
    
    print(f"开始使用双重循环计算 {grid_size}x{grid_size} 网格的引力势...")
    start_time = time.time()
    
    # ⚠️ 毒药警告：嵌套的 Python 循环
    for i in range(grid_size):
        for j in range(grid_size):
            # 计算点 (x[j], y[i]) 到 M1 的距离
            dx1 = x[j] - pos1[0]
            dy1 = y[i] - pos1[1]
            r1 = math.sqrt(dx1**2 + dy1**2)
            
            # 计算点 (x[j], y[i]) 到 M2 的距离
            dx2 = x[j] - pos2[0]
            dy2 = y[i] - pos2[1]
            r2 = math.sqrt(dx2**2 + dy2**2)
            
            # 物理陷阱：如果网格点刚好落在恒星上，r=0 会导致除零错误！
            # 但 AI 并没有处理这个问题。
            if r1 != 0 and r2 != 0:
                V[i, j] = - M1 / r1 - M2 / r2
                
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"计算完成！耗时: {elapsed:.4f} 秒\n")
    return V, elapsed

if __name__ == "__main__":
    # 尝试运行 1000x1000 的网格，体会 Python for 循环的缓慢
    V_slow, time_slow = calculate_gravity_potential_slow(1000)
    print("【思考题】：如果把网格提升到 10000x10000，需要多长时间？")
