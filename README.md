ARIMA是目前应用最广泛的单变量时间序列数据预测方法之一，但它不支持具有季节性成分的时间序列。为了支持序列的季节分量，长沙银行将ARIMA模型扩展成为SARIMA。
SARIMA (季节性差分自回归移动平均模型应用于包含趋势和季节性的单变量数据，SARIMA由趋势和季节要素组成的序列构成。
      与ARIMA模型相同的一些参数有：
      p即趋势的自回归阶数,
      d即趋势差分阶数，
      q趋势的移动平均阶数。
不属于ARIMA的四个季节性因素有：
P即SAR季节性自回归阶数。
Q即SMA季节性移动平均阶数。
在实际应用中，经常会发现，需要研究的时间序列，不仅会含有趋势性，而且经常包含一定的周期性。这时，我们再对序列进行平稳化处理时，就不仅仅需要对序列进行𝑑阶差分，还需要对序列进行𝑘步差分，即对间隔为𝑘期的两个序列值做差。
![image](https://github.com/luopinyao579/sarima/assets/90679190/88f0a19b-6ee1-44f6-bc6f-d9797ec4aed4)

若一个序列经过𝑑阶差分和𝑘步差分后能变平稳，并将差分后序列建立ARMA模型，称这类序列为SARIMA序列，其相应模型为SARIMA模型。SARIMA模型定义：设𝑑和𝐷为非负整数，对原始序列𝑋𝑡 经过𝑑阶差分和𝐷阶𝑘 步差分，得到随机序列𝑌𝑡 。
![image](https://github.com/luopinyao579/sarima/assets/90679190/b9d68e9c-6abb-4893-992d-f8e86918b53f)

如果Y_t是平稳的ARMA序列，即
![image](https://github.com/luopinyao579/sarima/assets/90679190/54e1b49d-376c-446f-a362-cc1f65978025)

则称Y_t是周期为S的SARIMA![image](https://github.com/luopinyao579/sarima/assets/90679190/116bc65b-b454-499d-9f2f-a963fbf3e66d)
过程，其中
![image](https://github.com/luopinyao579/sarima/assets/90679190/7c726c9c-04da-4b66-a9fe-64d51c63edb9)

Ap（R）与Φ（R^s）分别表示非季节性与季节自回归多项式，B_q(R)与Θ（R^s）分别表示非季节与季节滑动平均多项式，它们的根都在单位圆外。ε_t为白噪声WN(0, σ_s^2)。实际应用中，𝐷很少大于1，而𝑝和𝑄一般小于3。

