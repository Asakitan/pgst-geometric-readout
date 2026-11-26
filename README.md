# 近完美量子态传输：几何增长的读出时间

**证明署名：** Chain.Ren · 独立研究 · [完整证明](PROOF.md) · 版本日期：2026-11-26

[固定版本证明](https://github.com/Asakitan/pgst-geometric-readout/blob/proof-v1.0.0/PROOF.md) · [GitHub Release 与公开时间](https://github.com/Asakitan/pgst-geometric-readout/releases/tag/proof-v1.0.0) · [引用信息](CITATION.cff)

对任意有限无向简单图，若指定顶点对在邻接矩阵量子行走中具有近完美态传输（PGST），则可用精确代数预处理构造两数 $y>0,\rho>1$，使

$$
t_n=\pi y\rho^n
$$

成为一条读出时间序列。它在同一目标相位下趋于完美传输，保真度误差有关于 $n$ 的指数上界。证明把各谱相位的符号要求写成数域中的迹同余，再用一个 Pisot 型代数数控制其余共轭。

这是对 [Coutinho–Guo 公开问题 2.4](https://pure.uva.nl/ws/files/234177391/Selected_open_problems_in_continuous-time_quantum_walks.pdf) 中**构造读出时间**的回答。没有解决其中的多项式时间判定问题；也不主张读出时间最短或全球首创。先前的近似算法和具体图族结果在证明中列明。

[完整证明（英文）](PROOF.md) · [项目状态](STATUS.md) · [MIT 许可证](LICENSE)

## 复核示例

~~~bash
python -B verify_p4.py
~~~

脚本仅用标准库，精确验证四点路径 $P_4$ 的特征多项式、谱符号与迹同余。一般图的结论由解析证明给出；本仓库没有实现通用数域预处理器。
