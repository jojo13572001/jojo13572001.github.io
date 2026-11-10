---
layout: post
title: "Convolutional Neural Networks' (CNN) Backward Propagation"
date: 2017-01-24 16:56
categories: [CNN, NN]
---
# Outline
- **Prerequisite**
- **Introduction**
- **Architecture**
- **1. Basic Components**
	- ***1.1 Convolution Layer***
  - ***1.2 Pooling Layer***
  - ***1.3 Full Connected Layer***
- **2. Backward Propagation**
	- ***2.1 $$\delta$$'s derivation***
  - ***2.2 $$\theta$$'s derivation***
- **Models Comparision**
- **Trend**
- **Summary**

## Perequisite
1. Image filters(2D convolution) with padding[1]
2. [Neural Network]({% post_url 2017-01-08-1288520 %})

## Introduction
這裡是cs231n的內容，但是沒有看到CNN Backward Propagation，因此我增加了我的推導. 
此外Professor Eugenio Culurciello影片的VGG-19 model[4]圖片比較漂亮，所以Chapter1我借用了他的圖片！
其餘都是我自己的版權圖片。

## Architecture[4]
<img class="left" src="{{ site.baseurl }}/assets/images/1351812/089tmHPYTJuZvPysgexQ_cnn.png" alt="cnn.png">
CNN基本架構分為三層
1. 紅色部分是輸入受訓練的圖片
2. 藍色部分負責影像處理，產生多張特徵圖層(Convolution, RELU, Pooling)
3. 最後部分是將所有產生的特徵圖層結合起來，用NN+softmax做分類(Full Connected)

CNN整個過程中需要求解的參數是
1. Convolution layer filters
2. Full Connected Layer filters

## 1. Basic Components[2][4]
### 1.1 Convolution Layer(3D)
![3dconvolution.png]({{ site.baseurl }}/assets/images/1351812/9yChz4MsSHebeHvDtr9r_3dconvolution.png)
以上圖為例，
**Input image Size**  224 * 224 * **3** = W * H * RGB_size，zero-padding = 1 = P
**Convolution Filter Size**  3 * 3 * **3** = F * F * RGB_size，每次移動的Stride(S) = 1，總共有64個filter
則**Output Feature Map** 
Width Size = (W - F + 2P) / S + 1 = (224 - 3 + 2) / 1 + 1 = 224
Height Size = (H - F + 2P) / S + 1 = 224
Depth Size = 64
一個filter會產生一個224*224*1的feature map，64個filter會產生224*224*64的feature Map

### 1.2 Pooling Layer
![pooling.png]({{ site.baseurl }}/assets/images/1351812/PzEF0Tx5Qk0zat2LfxvD_pooling.png)
pooling層就是做downsampling，主要目的是為了減少記憶體使用量，及一定程度降低overfitting. 為什麼會降低overfitting呢？這是因為所有的convolution filter之間的組合變少了，相當於cost方程內的參數組合減少一些. 

### 1.3 Full Connection Layer
這部分就是傳統的neural network neuron+softmax regression。Please refer to [my NN]({% post_url 2017-01-08-1288520 %})
![full.png]({{ site.baseurl }}/assets/images/1351812/t0jNnNSQYGnN1mcTwkKi_full.png)
![softmax.png]({{ site.baseurl }}/assets/images/1351812/wZQ14vcmQXewg7ujU1zn_softmax.png)

## 2. Backward Propagation[3][6][7]
<img class="center" src="{{ site.baseurl }}/assets/images/1351812/e9Boy3OQhmbrjdYk9ahO_cnn.png" alt="cnn.png">
### 2.1 $$\theta$$的推導
由之前[NN的推導]({% post_url 2017-01-08-1288520 %})及上圖可得知，<img class="center" src="{{ site.baseurl }}/assets/images/1351812/J366fGRpSsi3QUS8EXSF_theta.png" alt="theta.png">如果convolution filter的stride = 1，則上式可進一步被推導為<img class="center" src="{{ site.baseurl }}/assets/images/1351812/Qx6mnYf0RVec6wt7Otvu_delta.png" alt="delta.png">以下是上式示意圖<img class="center" src="{{ site.baseurl }}/assets/images/1351812/NrNSKl43T1GWHjSwLGCH_convolution_rotation.png" alt="convolution_rotation.png">
		
### 2.2 $$\delta$$的推導
分成兩種$$\delta$$討論
		- [ CONV$$\rightarrow$$ReLU$$\rightarrow$$Pooling ]
		- [ ?$$\rightarrow$$CONV ]
**第一種[ CONV$$\rightarrow$$ReLU$$\rightarrow$$Pooling ]**
<img class="center" src="{{ site.baseurl }}/assets/images/1351812/lgwS2MYGQ1iZZuXhlaUp_delta.png" alt="delta.png">
<img class="center" src="{{ site.baseurl }}/assets/images/1351812/mR6zBuUyQTqapNwNrnBT_delta.png" alt="delta.png">upsample指根據我們選用的downsample $$g(x)$$,來決定如何運算$$g^{'}$$和$$\delta$$並回傳給上一層$$\delta$$，
由於我們選用的是max pool, 因此upsample將$$\delta$$ 回傳給在downsample時所記錄的"winning unit"($$a^{(n+1)}_1, a^{(n+1)}_4$$), $$g^{'}$$在這個例子沒有作用，$$\sigma^{'}_\theta$$因為選擇ReLU所以也沒作用
如果我們選用的是average pool,則
<img class="center" src="{{ site.baseurl }}/assets/images/1351812/EYuhBfBmT9Slhw4l8XHT_delta.png" alt="delta.png">

**第二種[ ?$$\rightarrow$$CONV ]**
<img class="center" src="{{ site.baseurl }}/assets/images/1351812/qoIZr0FQTjjPrnrSG27p_delta2.png" alt="delta2.png">由之前[NN的推導]({% post_url 2017-01-08-1288520 %})及上圖可知，<img class="center" src="{{ site.baseurl }}/assets/images/1351812/cd8MseLXR5mwfxImKnX4_1.png" alt="1.png">
如果convolution filter的stride = 1，則上式可進一步被推導為<img class="center" src="{{ site.baseurl }}/assets/images/1351812/l0Vq1v3aTSCkCyY02C8w_theta.png" alt="theta.png">以下是上式示意圖<img class="center" src="{{ site.baseurl }}/assets/images/1351812/JK31SOESneugdUuQrimA_delta2_rotation.png" alt="delta2_rotation.png">

## Models Comparision[5]
<img class="center" src="{{ site.baseurl }}/assets/images/1351812/QsUqXAHrTrCo6U5Csl9j______2017-02-23___9.37.00.png" alt="螢幕快照 2017-02-23 上午9.37.00.png">

## References
[1]Example of 2D Convolution http://www.songho.ca/dsp/convolution/convolution2d_example.html
[2]Andrej Karpathy's cs231n https://www.youtube.com/watch?v=AQirPKrAyDg
[3]Forward and Backward Propagation of Convolutional Layer
https://jianfengwang.files.wordpress.com/2015/07/forwardandbackwardpropagationofconvolutionallayer.pdf
[4]Professor Eugenio Culurciello's Convolutional Neural Network (CNN) models https://www.youtube.com/watch?v=EPFQ3z2xIQ8
[5]An Analysis of Deep Neural Network Models for Practical Applications https://openreview.net/pdf?id=Bygq-H9eg
[6]Backpropagation in Convolutional Neural Network https://www.slideshare.net/kuwajima/cnnbp
[7]Convolutional Neural Networks backpropagation: from intuition to derivation
 https://grzegorzgwardys.wordpress.com/2016/04/22/8/