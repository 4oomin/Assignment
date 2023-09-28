#include <iostream>
#include <string>
#define MAX 10
using namespace std;

class Frame {
	int throw1;
	int throw2;
	int throw3;
	int score;
	bool spare;
	bool strike;
public:
	Frame();
	//	~Frame();
	void setFirstThrow(int s) { throw1 = s; }
	void setSecondThrow(int s) { throw2 = s; }
	void setThirdThrow(int s) { throw3 = s; }
	void setScore(int s) { score = s; }
	void setStrike(bool B) { strike = B; }
	void setSpare(bool B) { spare = B; }

	//int genThrow(int ind_Frame);
	int getFirstThrow() { return throw1; }
	int getSecondThrow() { return throw2; }
	int getThirdThrow() { return throw3; }
	int getScore() { return score; }
	bool isStrike() { return strike; }
	bool isSpare() { return spare; }

};

Frame::Frame() {
	setScore(-1);
	setStrike(0);
	setSpare(0);
	setFirstThrow(0);
	setSecondThrow(0);
	setThirdThrow(0);
}



class Bowling {
	Frame a[10];
public:
	void calculateScore();
	void bowl(string name);
	void printData(); // strike 고려 frame 별 최종 점수 
};

void Bowling::printData() {
	for (int i = 0; i < 9; i++) { // 0~8
		int sum;
		if (a[i].isSpare()) {
			sum = a[i].getScore() + a[i + 1].getFirstThrow();
			a[i].setScore(sum);
		}
		else if (a[i].isStrike()) {
			sum = a[i].getScore() + a[i + 1].getFirstThrow();
			if (a[i + 1].isStrike()) {
				if (i == 8) sum += a[i + 1].getSecondThrow();
				else sum += a[i + 2].getFirstThrow();
			}
			else sum += a[i + 1].getSecondThrow();
			a[i].setScore(sum);
		}
	}
	cout << "Frame " << " Score " << " Sum " << endl;
	for (int i = 0; i < 9; i++) {
		cout << " " << i + 1 << "   : ";
		if (a[i].isStrike()) cout << "  X  " << "   " << a[i].getScore() << endl;
		else if (a[i].isSpare()) cout << " " << a[i].getFirstThrow() << " / " << "   " << a[i].getScore() << endl;
		else cout << " " << a[i].getFirstThrow() << " " << a[i].getSecondThrow() << "    " << a[i].getScore() << endl;
	}
	cout << 10 << "   : ";
	if (a[9].getFirstThrow() == 10) cout << " X";
	else cout << " " << a[9].getFirstThrow();
	if (a[9].getSecondThrow() == 10) cout << "X";
	else cout << " " << a[9].getSecondThrow();
	if (a[9].getThirdThrow() == 10) cout << "X  ";
	else cout << " " << a[9].getThirdThrow();
	cout << "  " << a[9].getScore() << endl;

	int total = 0;
	for (int i = 0; i < 10; i++) total += a[i].getScore();
	cout << "\n합계 : " << total << endl;
}

void Bowling::calculateScore() {
	int i = 0, sum;
	while (a[i].getScore() != -1) ++i;
	if (i == 9) {
		sum = a[i].getFirstThrow() + a[i].getSecondThrow() + a[i].getThirdThrow();
		a[i].setScore(sum);
		if (a[i].isSpare()) cout << "잘 치셨어요. 세이브를 하셨습니다." << endl << endl;
	}
	else {
		sum = a[i].getFirstThrow() + a[i].getSecondThrow();
		a[i].setScore(sum);
		if (a[i].isSpare()) cout << "잘 치셨어요. 세이브를 하셨습니다." << endl << endl;
		else if (a[i].isStrike()) cout << "스트라이크! 축하합니다." << endl << endl;
		else cout << "아쉽네요. 다음엔 잘치세요!" << endl << endl;
	}

}
void Bowling::bowl(string name) {
	int i = 0;
	int t1, t2, t3;
	while (a[i].getScore() != -1) ++i;
	if (i == 9) {
		cout << name << " 님의 " << i + 1 << "번 프레임 1번 점수는?";
		cin >> t1;
		a[i].setFirstThrow(t1);
		if (t1 == 10) {
			a[i].setStrike(1);
			cout << "스트라이크! 축하합니다." << endl;
			cout << name << " 님의 " << i + 1 << "번 프레임 2번 점수는?";
			cin >> t2;
			if (t2 == 10) cout << "스트라이크! 축하합니다." << endl;
			a[i].setSecondThrow(t2);
			cout << name << " 님의 " << i + 1 << "번 프레임 3번 점수는?";
			cin >> t3;
			if (t3 == 10)cout << "스트라이크! 축하합니다." << endl;
			a[i].setThirdThrow(t3);
		}
		else {
			cout << name << " 님의 " << i + 1 << "번 프레임 2번 점수는?";
			cin >> t2;
			a[i].setSecondThrow(t2);
			if (t1 + t2 == 10) {
				a[i].setSpare(1);
				cout << name << " 님의 " << i + 1 << "번 프레임 3번 점수는?";
				cin >> t3;
				a[i].setThirdThrow(t3);
			}

		}
	}
	else {

		cout << name << " 님의 " << i + 1 << "번 프레임 1번 점수는?";
		cin >> t1;
		a[i].setFirstThrow(t1);
		if (t1 == 10) {
			a[i].setStrike(1);
			return;
		}

		cout << name << " 님의 " << i + 1 << "번 프레임 2번 점수는?";
		cin >> t2;
		a[i].setSecondThrow(t2);
		if (t1 + t2 == 10) a[i].setSpare(1);
	}

}






class Player {
	string name;
	string score;
	Bowling* myBowling;
public:

	Player() {
		cout << "플레이어의 이름은?";
		cin >> name;
		myBowling = new Bowling;
	}
	~Player() {
		cout << "*******" << name << "님은 모든 게임을 마쳤습니다." << "*******" << endl << endl;
		delete myBowling;
	}
	void showScore();
	void showTotalFrame();
};
//초록 부분 
void Player::showScore() {
	myBowling->bowl(name);
	myBowling->calculateScore();

}
void Player::showTotalFrame() {
	cout << "\n이름: " << name << endl;
	myBowling->printData();
	//전체  Frame 출력 및 합계 출력  
}



class PlayGame {
	int gameID; // frame 인덱스 
	int numberOfplayer;
	Player* p[MAX];

public:
	void gameStart();

};

void PlayGame::gameStart() {
	cout << "볼링 게임을 시작합니다. 플레이어는 몇 명입니까?";
	cin >> numberOfplayer;
	//플레이어 생성 
	for (int i = 0; i < numberOfplayer; i++) p[i] = new Player;
	cout << "\nWelcome to Sookmyung Bowling Club!!\nLet’s start a Bowling Game!!!\n" << endl;
	//프레임 0~9 
	for (gameID = 0; gameID < 10; ++gameID) {
		for (int i = 0; i < numberOfplayer; i++) {
			p[i]->showScore();
			if (gameID == 9) {
				p[i]->showTotalFrame();
				delete p[i];
			}
		}
	}



}




int main() {
	PlayGame BG;

	BG.gameStart();

	return 0;
}