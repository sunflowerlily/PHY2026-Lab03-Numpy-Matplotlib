import numpy as np
import time

def calculate_gravity_potential_fast(grid_size, M1=1.0, M2=0.5, pos1=(-1, 0), pos2=(1, 0)):
    """
    【你的任务】
    重构 AI 的代码，完全消除 for 循环，使用 NumPy 的向量化和广播机制。
    """
    # 1. 生成一维坐标数组
    x = np.linspace(-2, 2, grid_size)
    y = np.linspace(-2, 2, grid_size)
    
    start_time = time.time()
    
    # ==========================================
    # TODO: 在此处编写你的向量化代码 (提示: 使用 np.meshgrid)
    # 1. 生成二维网格 X, Y
    # X, Y = ...
    
    # 2. 计算到 M1 和 M2 的距离 R1, R2
    # R1 = ...
    # R2 = ...
    
    # 3. 处理奇点 (r=0) 的问题。可以引入一个极小的“软化因子” epsilon
    epsilon = 1e-10
    
    # 4. 计算总引力势 V
    # V = ...
    # ==========================================
    
    # 下面是占位符，请删除或替换
    V = np.zeros((grid_size, grid_size)) 
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    return V, elapsed

if __name__ == "__main__":
    V_fast, time_fast = calculate_gravity_potential_fast(1000)
    print(f"向量化版本耗时: {time_fast:.6f} 秒")
