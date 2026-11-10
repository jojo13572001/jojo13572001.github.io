---
layout: post
title: "Standford Machine Learning - Anomaly Detection"
date: 2017-01-09 13:54
---
Anomaly detection modeling can be supervised or unsupervised learning
0. multivariate gaussian model's theorem?
1. unsupervised buildup total samples's probability model to predict anomaly(pick low probability ).
2. Gaussian density probability; Integral of a Gaussian function https://en.wikipedia.org/wiki/Gaussian_function. The total area(density) is 1.
3. **each feature will generate a gaussian destiny probability. We multiply all to generate a prediction model**. Before training model, we should plot each feature set ex:hist(X(1,:)) and re-feature them to be like gausian distribution , ex: log, square root... use the new feature will have better result. without it also perform well, Andrew Ng will do it each time.
4. anomaly detection can use labeled samples(supervised) as well. Normal samples will be divided into training set and validation/test set, but anomaly samples will be assigned only to validation/test test to define p(x) >= epson anomaly situation.
5. Sometimes it's a skewed case, so the accuracy will be high if you always keep predicting normal. You should use precision/recall or F1-score as metrics and then using validation set to choose parameter p(x) >= epson
6. Three reasons that you should use anomaly detection rather than supervised learning 
	- Small number of anomaly samples with large number of correct samples
  - Many types of anomaly types with small anomaly samples
  - There may be unknown anomaly types in the future to predict.
  if you have enough anomaly samplse and promise there will be not other types unknown anomaly types occured, you should use supervised learning
7. spam email problem is assumed as supervised problem because of with large anomaly samples.
8. Anomaly Detection ex: Fraud detection(record website behaviro), manufacturing, monitoring machines in data center.
9. Error Analysis : In common case, you will find anomaly sample's feature locate on gassian normal probability prediction. Please find new feature and create new probability density model to make it locate on anomalty area. New feature should present unusual large or small case. It can be other feature's combination, ex: (cpu load)^2/network load to present unusual deadlock with normal network loading.
10. gaussian model metioned above is kind of multivariate gaussian model that covariance matrix's diagonal are all feature's square of standard deviation.(gaussian coutour is axis-aligned)
![螢幕快照 2017-01-12 下午12.47.03.png]({{ site.baseurl }}/assets/images/1291322/1q4DosleTiS4751sBpzP______2017-01-12___12.47.03.png)
11. multivariate is not used as usual as general gaussian but it can automatically present correlation between features;
	11.1 use general gaussian model, you have to manually create new features combined of serval features ex: (cpu load)^2/network
  11.2 covariance matrix is computationally and should not be linear dependent and sample size should be smaller than feature size or there will be no invertable matrix.
![螢幕快照 2017-01-12 下午2.01.04.png]({{ site.baseurl }}/assets/images/1291322/SvVj7pXCTjiLh0oenvdP______2017-01-12___2.01.04.png)
