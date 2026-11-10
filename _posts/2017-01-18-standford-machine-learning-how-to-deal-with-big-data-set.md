---
layout: post
title: "Standford Machine Learning - How To Deal With Big Data Set ?(Stochastic Gradient Descent)"
date: 2017-01-18 06:02
---
1. Before using big data set(Time-consuming), you have to randomly pick up a small data set and plot learning curve to identify high-bias(CV and TR set already coverage and high, big data is useless, you shouuld add more features or hidden layers) or high variance(use big data to converge CV set to Train set)
![螢幕快照 2017-01-18 下午2.10.24.png]({{ site.baseurl }}/assets/images/1325109/RqT8gBikQSmLVBZOJkw6______2017-01-18___2.10.24.png)

2. Stochastic gradient descent
	2.1 Ordinary Gradient descent is computationaly large becuase of thetai = thetai - sum ((Thetai*Xi-Yi)*Xi) is large computaion on sum. It is called Batch gradient descent as well.
  2.2 Stochastic gradient descent doesn't sum all samples for each theta. It only compute thetai = thetai - (thetai*Xi-Yi)*Xi , and randomly choose one sample to count all thetai and finish one repeat until all samples are used. we may repeat only one or several times.
	2.3 Faster than ordinary method, but may not coverge to best minimum.
  2.4 To see if stochastic converge? Compute traning set each sample's cost and plot before updating theta, and average 1000 last cost to see if average cost declines. If average cost oscillate too much, maybe you have to use a large average like 5000 to check. If it doesn't decline, replacing learning rate lambda with smaller one may be helpful. A samller lambda will make converge slowly but retrieve lower cost(better theta) as a reselt. It it diverages, use smaller lambda instead.
  2.5 because learning rate is a constant, so stochastic may osscilate when approaching to minimum, we can use lambda = const1/(iteration_num+const2) instead. The method is few to use becuase of the effort tuning two constants, but useful finding better mininum because lambda get smaller over time.
![1.png]({{ site.baseurl }}/assets/images/1325109/r6GsnhdLSCerJHTltHEk_1.png)

3. Mini-batch gradient descent, sometimes faster than stochastic
  3.1 use b(usually 2-100) example(mini-batch size) in each computation of theta
  3.2 Why may mini-batch be faster than stochastic? Because summation of gradient can use vectorizationto parallelize computation by good linear algebra library.
  3.3 the defect is that you have to try the b size for compupation performance.