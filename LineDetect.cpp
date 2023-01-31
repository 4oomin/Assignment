#include<opencv2/opencv.hpp>

using namespace cv;
using namespace std;

Mat selectByColor(Mat src){
	Mat mask_y, img_y;
	Mat mask_w, img_w;

	Scalar lower_y = Scalar(35, 90, 130);
	Scalar upper_y = Scalar(100, 150, 225);
	inRange(src, lower_y, upper_y, mask_y);
	bitwise_and(src, src, img_y, mask_y);

	Scalar lower_w = Scalar(160, 160, 160);
	Scalar upper_w = Scalar(200, 200, 200);
	inRange(src, lower_w, upper_w, mask_w);
	bitwise_and(src, src, img_w, mask_w);

	Mat dst;
	addWeighted(img_w, 1.0, img_y, 1.0, 0.0, dst);
	cvtColor(dst, dst, COLOR_BGR2GRAY);

	return dst;
}

Mat regionByMask(Mat src) {
	Mat labels, stats, centroids;
	int cnt = connectedComponentsWithStats(src, labels, stats, centroids);

	Mat mask_region;
	mask_region = Mat::zeros(src.rows, src.cols, CV_8UC1);
	rectangle(mask_region, Point(src.cols/4, src.rows/2), Point(src.cols*3/4,src.rows), Scalar(255), FILLED);
	
	Mat dst;
	bitwise_and(src, src, dst, mask_region);

	return dst;
}
void lineByHough(Mat src,Mat dst) {
	const double PI = 3.41;
	vector<Vec2f> lines;
	HoughLines(src, lines, 1, PI / 180, 35);

	vector<Vec2f>::const_iterator it = lines.begin();
	bool drawL = false;
	bool drawR = false;
	while (it != lines.end()) {
		
		if (drawL == true && drawR == true) break;
		
		float rho = (*it)[0];
		float theta = (*it)[1];
		float tx, ty, bx, by;
		if (0 < rho && drawL == false) {
			drawL = true;
			tx = rho / cos(theta);
			ty = 0;
			bx = (rho - src.rows * sin(theta)) / cos(theta);
			by = src.rows;
			Point pt1((tx + bx) / 2, (ty + by) / 2);
			Point pt2(bx, by);
			line(dst, pt1, pt2, cv::Scalar(0, 255, 0), 3);
		}
		else if (rho < 0 && drawR == false) {
			drawR = true;
			tx = rho / cos(theta);
			ty = 0;
			bx = (rho - src.rows * sin(theta)) / cos(theta);
			by = src.rows;
			Point pt1((tx + bx) / 2, (ty + by) / 2);
			Point pt2(bx, by);
			line(dst, pt1, pt2, cv::Scalar(0, 255, 0), 3);

		}
		++it;
	}
}


int main(int argc, char** argv)
{
	VideoCapture video(argv[1]);
	if (!video.isOpened()) {
		cout << "fail to opend video" << endl;
		return -1;
	}

	Mat src;
	video.read(src);
	if (src.empty()) {
		cout << "fail to read video" << endl;
		return -1;
	}

	VideoWriter writer;
	int codec = VideoWriter::fourcc('X', 'V', 'I', 'D');
	double fps = 50.0;

	writer.open("./result.avi", codec, fps, src.size(), CV_8UC3);
	if (!writer.isOpened()) {
		cout << "fail to opend writer" << endl;
		return -1;
	}

	Mat img_color, img_canny, img_region, dst;
	while (1) {
		
		if (!video.read(src)) break;

		img_color = selectByColor(src); /*색깔로 필터링*/
		
		Canny(img_color, img_canny, 50, 150); /*엣지 검출*/
		
		img_region = regionByMask(img_canny); /*영역 지정*/
		
		src.copyTo(dst);
		lineByHough(img_region, dst); /*허프로 직선검출 및 그리기*/
		
		writer << dst;
		imshow("dst", dst);

		if (waitKey(1) == 27) break;
	}

	return 0;
}

