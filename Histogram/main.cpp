/*main.cpp*/

#include <iostream>
#include "Histogram1D.h"
using namespace std;

Mat equlization(const Mat &src,Mat &dst) {
	//누적 합 배열 가져오기
	Histogram1D h;
	int histBuffer[256] = { 0 };
	int* accummHist = h.getAccumulateHist(src, histBuffer);
	

	//평활화 테이블 만들기
	
	int n[256] = { 0 };
	int N = src.rows * src.cols;
	int I = 255;
	for (int i = 0; i < 256; i++) {
		n[i] = cvRound(((float)accummHist[i] / (float)N) * (float)I);
	}
	for (int i = 0; i < src.rows; i++) {
		for (int j = 0; j < src.cols; j++) {
			int pixelValue = (int)src.at<uchar>(i, j);
			dst.at<uchar>(i, j) = n[pixelValue];
		}
	}
	
	return dst;
}

int main(int argc, char** argv) {
	Mat src,zeroPad,dst;
	src = imread(argv[1],IMREAD_GRAYSCALE);
	dst = Mat::zeros(src.rows,src.cols, src.type());	
	dst = equlization(src, dst);
	
	
	Histogram1D h;
	Mat srcHistImg = h.getUnifomHistImage(src);
	Mat dstHistImg = h.getUnifomHistImage(dst);
	
	namedWindow("src", 1);
	namedWindow("uniformhist", 1);
	namedWindow("dst", 1);
	namedWindow("equalizedHist", 1);

	imshow("src", src);
	imshow("uniformhist", srcHistImg);
	imshow("dst", dst);
	imshow("equalizedHist", dstHistImg);
	
	
	waitKey(0);

	return 0;
}
