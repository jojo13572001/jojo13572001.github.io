---
layout: post
title: "Standford Machine Learning - Recommendation System"
date: 2017-01-12 15:32
---
1. Content Based Recommendation(linear regression) - assume we have each movie's content features(romanic 0.2, action 0.5 ...) and each user's rating y, we want to find out each user's theta(interested ratio of features) to min (theta*X - y) and then predict user's movie rating 
	1.1 It's difficult to find out all movies' features
![3.png]({{ site.baseurl }}/assets/images/1301142/vG5o7IMxRAaVSZrWNrmq_3.png)

2. collaborative filtering - it will learn features that it wants to use. Given random theta(user's ratio for movie's feature) as initial samples, and optimize movie's content features X. Then use the X to optimize user's ratio(theta)
![1.png]({{ site.baseurl }}/assets/images/1301142/PwcelidJSmm8UwIUrBKh_1.png)

3. Latest version of collaborative filtering algo is similar to neutral networking algorithm. compination of theta optimization and features optimization to only one formula.Furthermore, X0(1) and theta0 are reduced(The reason is not clear even Andrew Ng explain that X1 will replace X0's functionality)
![螢幕快照 2017-01-14 下午11.41.10.png]({{ site.baseurl }}/assets/images/1301142/DEuOxqdDQmacEQtfPlVH______2017-01-14___11.41.10.png)

4. Low rank matrix factorization is the theorem of collaborative filtering(we assume there are low rank compared to movie and user number)
![螢幕快照 2017-01-15 下午7.06.35.png]({{ site.baseurl }}/assets/images/1301142/XLma9BhcSwvPEHIJcnbA______2017-01-15___7.06.35.png)
Rank is feature's dimention k; m is movie number; u is user number; Y is user's total ranking for all movies(m*u matrix). Y = (m*k matrix) * (k*u matrix)
