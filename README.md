ARIMA是目前应用最广泛的单变量时间序列数据预测方法之一，但它不支持具有季节性成分的时间序列。为了支持序列的季节分量，长沙银行将ARIMA模型扩展成为SARIMA。
SARIMA (季节性差分自回归移动平均模型应用于包含趋势和季节性的单变量数据，SARIMA由趋势和季节要素组成的序列构成。与ARIMA模型相同的一些参数有：p即趋势的自回归阶数,d即趋势差分阶数，q趋势的移动平均阶数。不属于ARIMA的四个季节性因素有：P即SAR季节性自回归阶数。Q即SMA季节性移动平均阶数。
在实际应用中，经常会发现，需要研究的时间序列，不仅会含有趋势性，而且经常包含一定的周期性。这时，我们再对序列进行平稳化处理时，就不仅仅需要对序列进行𝑑阶差分，还需要对序列进行𝑘步差分，即对间隔为𝑘期的两个序列值做差。
∇_k X_t=X_t-X_(t-k)=(1-R_k)X_t
若一个序列经过𝑑阶差分和𝑘步差分后能变平稳，并将差分后序列建立ARMA模型，称这类序列为SARIMA序列，其相应模型为SARIMA模型。SARIMA模型定义：设𝑑和𝐷为非负整数，对原始序列𝑋𝑡 经过𝑑阶差分和𝐷阶𝑘 步差分，得到随机序列𝑌𝑡 。
Y_t≜〖（1-R）〗^d 〖(1-R^s)〗^D X_t
如果Y_t是平稳的ARMA序列，即
A_p （R）Φ（R^s ） Y_t=B_q （R)θ（R^s）ε_t

则称Y_t是周期为S的SARIMA（p，d，q）×〖（P,D,Q）〗_S过程，其中
A_p （R）=1-a_1 R-a_2 R^2-∙∙∙-a_p R^p
Φ_p （R^s ）=1-φ_1 R-φ_2 R^2-∙∙∙-φ_p R^p
B_q （R）=1-b_1 R-b_2 R^2-∙∙∙-b_p R^p
Θ_p （R^s ）=1-θ_1 R-θ_2 R^2-∙∙∙-θ_p R^ps
A_p （R）与Φ（R^s）分别表示非季节性与季节自回归多项式，B_q(R)与Θ（R^s）分别表示非季节与季节滑动平均多项式，它们的根都在单位圆外。ε_t为白噪声WN(0, σ_s^2)。实际应用中，𝐷很少大于1，而𝑝和𝑄一般小于3。

