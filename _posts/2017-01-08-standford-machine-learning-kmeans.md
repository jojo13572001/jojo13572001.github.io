---
layout: post
title: "Standford Machine Learning - Kmeans"
date: 2017-01-08 16:18
---
1. use samples as initial cluster centroid
2. if you know the number of cluster(k) that you need, just repeatly(100 times) randomly choose k samples as centroid to run kmeans and finally choose the lowest cost.
3. If you want to know what number of cluster k is suitable for you, you have two method 
	 3.1 use elbow point(try different k and inspect each cost, choose the elbow point), but it's       difficult to clearly identify the elbow point.
   3.2 analyze exactly what number you really need is