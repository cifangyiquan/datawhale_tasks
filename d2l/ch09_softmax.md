# softmax回归

对类别进行一位有效编码
$$ 
\begin{aligned}
y &= [y_1, y_2, ..., y_n]^T  \\\
y_i &= \begin{cases}
1 &\text{if } i = y
\\
0 &\text{otherwise} 
\end{cases}
\end{aligned}
$$
使用均方损失训练

最大值为预测：
$$ \hat y = \argmax_i o_i  $$

需要更置信的识别正确类（大余量）
$$ o_y - o_i \ge \Delta(y, i) $$

输出匹配概率（非负，和为1）
$$ \bold{\hat y} = softmax(\bold{o}) $$
$$ \hat y_i = \frac {\exp(o_i)} {\sum_k\exp(o_k)} $$

* 概率$\bold{y}$和$\bold{\hat y}$的区别作为损失

## softmax和交叉墒损失
* 交叉墒常用来衡量两个概率的区别$H(\bold{p},\bold{q})=\sum_i -p_i\log(q_i)$
* 将它作为损失
$$ l(\bold{y}, \bold{\hat y}) = -\sum_i y_i\log\hat y_i = -\log \hat y_y$$
* 其梯度是真实概率和预测概率的区别
$$ \partial_{o_i}l(\bold{y}, \bold{\hat y}) = softmax(\bold o)_i - y_i $$ 

## 总结
* softmax回归是一个多分类模型
* 使用softmax操作子得到每个类别的预测置信度
* 使用交叉墒来衡量预测与label的区别
