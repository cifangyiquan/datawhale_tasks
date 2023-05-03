# 损失函数

## L2 Loss

$$ l(y, y') = \frac 1 2 (y-y')^2 $$

## L1 Loss

$$ l(y, y') = |y-y'| $$

## Huber's Robust Loss

$$
l(y,y') = \begin{cases}
|y-y'| - \frac 1 2 &\text{if |y-y'| > 1}
\\
\frac 1 2 (y-y')^2 &\text{otherwise}
\end{cases}
$$


