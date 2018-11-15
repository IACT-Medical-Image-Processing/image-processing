# image-processing
Basic and advanced contrast enhancement techniques for images using modified histogram equalisation results

## 1. Histogram Equalization

Histogram equalization is a technique for adjusting image intensities to enhance contrast.

Let f be a given image represented as a mr by mc matrix of integer pixel intensities ranging from 0 to L − 1. L is the number of possible intensity values, often 256. Let p denote the normalized histogram of f with a bin for each possible intensity. So
pn = number of pixels with intensity n n = 0, 1, ..., L − 1. total number of pixels
The histogram equalized image g will be defined by
```
fi,j
gi,j =floor((L−1)􏰂pn), (1)
```

## 2. Bi-Histogram Equalization

In Bi-histogram equalization the histogram of the original image is separated into two sub histograms based on the mean of the histogram of the original image, the sub-histograms are equalized independently using refined histogram equalization, which produces flatter histogram.

