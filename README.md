# 第 3 周实验：数组与高效科学计算基础：NumPy 广播机制与 Matplotlib 科研绘图

## 🎯 实验背景
在计算物理中，处理大规模网格数据（如电磁场、引力场分布）时，如果使用 Python 的 `for` 循环，性能将极度低下。
本周我们将抛弃“单粒子循环”的思维，掌握 NumPy 的**向量化 (Vectorization)** 与 **广播机制 (Broadcasting)**，实现“零循环”编程。

## 👥 小组分工 (Team Mode)
本实验设计为 3-4 人小组协作。请在开始前明确分工，并在 `Report_Template.md` 中记录。

*   **Member A (Debug Master)**: 负责破解预埋的“性能毒药”代码。
*   **Member B (Algorithm Engineer)**: 负责使用 NumPy 广播机制重构代码。
*   **Member C (Data Visualizer)**: 负责绘制引力等势线图，并寻找物理奇点。
*   *(如果有第 4 人)* **Member D (Bonus Challenger)**: 负责 Lab 2 的高阶微扰动画挑战。

---

## 🚀 你的任务 (The Challenges)

### 🎯 Lab 1: 核心排雷 (必做) - 满分 70 分
背景：我们需要计算双星系统在 2D 平面上的引力势场分布。
$$V(x, y) = - \frac{G M_1}{\sqrt{(x-x_1)^2 + (y-y_1)^2}} - \frac{G M_2}{\sqrt{(x-x_2)^2 + (y-y_2)^2}}$$

1.  **任务 A (破译毒药)**：
    *   运行 `lab1_core/src/solver_bad_ai.py`。
    *   观察并记录计算 $1000 \times 1000$ 网格所需的时间。
    *   分析为什么 AI 默认生成的双重循环代码在 Python 中是性能灾难。
2.  **任务 B (广播重构)**：
    *   在 `lab1_core/src/physics_model.py` 中，使用 `np.meshgrid` 或 `x[:, None]` 的广播机制，**在完全不使用 `for` 循环**的情况下完成计算。
    *   确保代码能通过 `pytest lab1_core/tests/test_core.py` 的测试。
3.  **任务 C (物理洞察)**：
    *   在 `lab1_core/notebook_core.ipynb` 中，使用 `plt.contourf` 绘制引力势场。
    *   **排雷点**：如果不做特殊处理，在质点中心 ($r=0$) 处代码会报什么错？如何在不修改物理定律的前提下，用“软化因子 (Softening)”或“掩码 (Mask)”解决它？

### 🚀 Lab 2: 复杂系统探索 (进阶) - 满分 30 分
背景：现实中的引力场并非静止，当两颗恒星相互绕转时，势场也会随之变化。

1.  打开 `lab2_bonus/notebook_bonus.ipynb`。
2.  使用 `matplotlib.animation.FuncAnimation`，制作双星相互绕转时，空间引力势场随时间演化的动态 GIF/MP4。
3.  尝试在动态图上标出“第一拉格朗日点 ($L_1$)”的移动轨迹。

---

## 📝 评分标准与提交流程
1.  **提交代码**: 
    ```bash
    git add .
    git commit -m "feat: complete week 3 numpy lab"
    git push
    ```
2.  **GitHub Actions**: 云端会自动运行 `test_core.py` 检查你的向量化代码性能（必须比循环快至少 50 倍）。
3.  **填写报告**: 请小组共同完成 `Report_Template.md`。
