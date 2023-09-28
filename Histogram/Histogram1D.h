/*Histogram1D.h*/
#pragma once
#include<opencv2/opencv.hpp>

using namespace cv;
using namespace std;

class Histogram1D 
{
private:
	int histSize;
	float range[2];
	const float* histRange[1];
	int channels;
	bool uniform;
	bool accumulate;

public:

	Histogram1D() {
		histSize = 256;
		range[0] = 0.0;
		range[1] = 255.0;
		histRange[0] = range;
		channels = 0;
		uniform = true;
		accumulate = false;
	}
	//입력 이미지, 평활화 된 이미지 출력, 입력 이미지 히스토그램, 평활화 히스토그램
	// 그레이 스케일 이미지에 대해서만 구현

	MatND getUniformHist(const Mat& image) {
		MatND hist;
		calcHist(&image, 1, &channels, Mat(), hist, 1, &histSize, histRange, uniform, accumulate);
		return hist;
	}

	Mat getUnifomHistImage(const Mat& image) {
		MatND hist = getUniformHist(image);

		double maxVal = 0, minVal = 0;
		minMaxLoc(hist, &minVal, &maxVal, 0, 0);

		Mat histImg(histSize, histSize, CV_8U, Scalar(255));
		int hpt = static_cast<int>(0.9 * histSize);

		for (int h = 0; h < histSize; h++) {
			float binVal = hist.at<float>(h);
			int intensity = static_cast<int>((binVal / maxVal) * hpt);
			line(histImg, Point(h, histSize), Point(h, histSize - intensity), Scalar::all(0));
		}
		return histImg;
	}

	int* getAccumulateHist(const Mat& image,int hist[]) {
		MatND uniformhist = getUniformHist(image);
		hist[0] = (int)uniformhist.at<float>(0);
		for (int h = 1; h < histSize; h++) {
			int binValue = (int)uniformhist.at<float>(h);
			hist[h] = hist[h - 1] + binValue;
		}
		return hist;
	}


};
