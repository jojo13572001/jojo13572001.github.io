---
layout: post
title: "Standford Machine Learning - Photo OCR (machine learning pipeline)"
date: 2017-01-20 05:10
---
1. Photo OCR Applications - help the blinds know what sign in front of them; car navitation system, car can read street sign.

2. Photo OCR pipeline
	2.1 Text Detection(find out rectangle area)
  2.2 Character Segmentation
  2.3 Character Classifier
  2.4 Spell Correction System(c1ean->clean), not included in the course
3. Pedestrain Detection
	3.1 sliding window(height*width ratio) with step size(stride parameterusually 4 to 8 pixels) and pass to classifier; Change to another window size and scale to appropriate size to classifier.
4. Text Detection
	4.1 First, you use labeled training set(with character even split between words) to train a **binary classifier**(is there character or not in it)
  4.2 **Slide window** and give to classifier and identify if the window contains a character. collect all windows in one image with different gray scale to present probability.
  4.3 apply **expansion operator** to each white window(if surrounding with white pixel, it will also be white pixel) and generate connected bounding box. Check each connected bounding box's ratio, remove "tall" one.
![螢幕快照 2017-01-20 下午5.51.21.png]({{ site.baseurl }}/assets/images/1333921/7MD0kPHPRVGrD3LskFzW______2017-01-20___5.51.21.png)

5. 1D sliding window for character Segmentation
	5.1 use training set to train a binary classifier to distinguish which sliding window shoud has the split line in the middle of characters
![螢幕快照 2017-01-20 下午8.49.08.png]({{ site.baseurl }}/assets/images/1333921/HnBAciDnQ3G5FlMChYGc______2017-01-20___8.49.08.png)

6. Finally, we use digit and character multi-classifier to identify A-Z and 0-1
![螢幕快照 2017-01-20 下午8.53.26.png]({{ site.baseurl }}/assets/images/1333921/3XJYDPTvOjK77lX9G7Dg______2017-01-20___8.53.26.png)

7. Artificial Data Synthesis (Create Big data by yourself)
	7.1 first method, use office software's to combine different fonts with random backgroud image with some bluring operator,scaling and rotation
  7.2 second method, reasonablely distort current data set, ex synthesize seperately noisy, crowd, machinery voice to original digital voice
  7.3 Be careful, distortion used should be representation of noise/distortion in test set. Random/meanless noise/distortion is useless.
  7.4 Before Creating big sythetical data, you should make sure you need big data(your model is suffering from low bias/high variance)
  
8. How to Get Big data set
  8.1 Artificial Data Synthesis
  8.2 Label by hand (Count time of 10x data set before you start, you will be surprised how easy it is)
  8.3 Using Crowd Source like "Amazon Mechanical Turk"
  
9. Before Creating Big data set, you should
	9.1 Make sure you need big data set(Using learning curve to identify low bias/high variance)
  9.2 Count the time you need for collecting 10x larger data than current data set