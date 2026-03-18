import sys
import os
import pytest
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from physics_model import calculate_gravity_potential_fast
from solver_bad_ai import calculate_gravity_potential_slow

def test_vectorization_performance():
    """
    测试：向量化版本必须比循环版本快至少 50 倍
    """
    grid_size = 500 # 使用较小的网格以避免 CI 超时
    
    _, time_slow = calculate_gravity_potential_slow(grid_size)
    _, time_fast = calculate_gravity_potential_fast(grid_size)
    
    # 允许第一次执行有较小的开销，但通常会快几百倍
    speedup = time_slow / max(time_fast, 1e-6) 
    
    assert speedup > 50, f"性能不达标！向量化加速比仅为 {speedup:.1f}x。请确保代码中绝对没有 for 循环！"

def test_physics_accuracy():
    """
    测试：向量化版本的物理结果必须与循环版本（几乎）一致
    """
    grid_size = 50
    V_slow, _ = calculate_gravity_potential_slow(grid_size)
    V_fast, _ = calculate_gravity_potential_fast(grid_size)
    
    # 排除掉奇点（V_slow 在奇点是 0，V_fast 可能是极大的负数）
    # 我们只比较非奇点区域
    mask = V_slow != 0
    
    # 使用相对误差比较
    max_error = np.max(np.abs((V_fast[mask] - V_slow[mask]) / V_slow[mask]))
    
    # 考虑到软化因子 epsilon，误差不应超过 1e-4
    assert max_error < 1e-4, f"物理计算错误！最大相对误差为 {max_error}。"
