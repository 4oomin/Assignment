
#include <iostream>
#include <string>


// 단어와 누적 수의 객체
class Data {
public:
	int num;
	std::string word;
	Data* ptr;

public:
	Data(std::string wd);

};

Data::Data(std::string wd) {
	num = 1;
	word = wd;
	ptr = NULL;
}

// 동일 단어 리스트에서 찾기
Data* find(Data* start, std::string wd) {
	Data* DB_fnd;
	DB_fnd = start;
	while (DB_fnd != NULL) {
		if (DB_fnd->word == wd) return DB_fnd;
		else DB_fnd = DB_fnd->ptr;
	}
	return DB_fnd;
}

//내림차순 정렬 
void sort(Data* str, int len) {
	Data* crnt;
	int tmp_n;
	std::string tmp_w;
	crnt = str;
	for (int i = 0; i < len; i++) {
		if (crnt->ptr == NULL)break;
		for (int j = 0; j < len - 1 - i; j++) {
			if ((crnt->num) < (crnt->ptr->num)) {
				tmp_n = crnt->num;
				tmp_w = crnt->word;
				crnt->num = crnt->ptr->num;
				crnt->word = crnt->ptr->word;
				crnt->ptr->num = tmp_n;
				crnt->ptr->word = tmp_w;
			}
			crnt = crnt->ptr;
		}
		crnt = str;
	}
}

//대문자로 변환
int capital(int s) {
	if ((s >= 'a') && (s <= 'z')) s = s - 'a' + 'A';
	return s;

}
std::string toupper(std::string word) {
	int i;
	for (i = 0; i < word.size(); i++) word[i] = capital(word[i]);
	return word;
}


int main() {
	Data* DB_str = NULL;
	Data* DB_end = NULL;
	Data* DB_tmp;
	Data* DB_pos;
	Data* DB_del1;
	Data* DB_del2;
	Data* iter;

	std::string word;
	int len = 0;

	std::cout << "입력 : ";

	while (1) {

		// 단어 입력 받기
		std::cin >> word;

		// 대문자로 치환 
		word = toupper(word);
		// " 로 시작하는 단어 : " 제거 
		if (word.front() == '"') word = word.substr(1, word.length() - 1);
		// 알파벳을 시작하는 지 검사
		if (word.front() < 'A' || word.front() > 'Z') continue;
		// "로  끝나는 단어 : " 제거 
		if (word.back() == '"') word = word.substr(0, word.length() - 1);
		// 문장 기호(, ; . ? ) 제거  
		if (word.back() < 'A' || word.back() > 'Z') word = word.substr(0, word.length() - 1);


		//단어 데이터 생성 
		DB_tmp = new Data(word);

		// 맨 처음 데이터 저장 
		if (DB_str == NULL) {
			DB_str = DB_tmp;
			DB_end = DB_tmp;
			++len;
		}
		// 이후 데이터  
		else {
			iter = find(DB_str, word);
			// 없으면 리스트에 추가 
			if (iter == NULL) {
				DB_end->ptr = DB_tmp;
				DB_end = DB_tmp;
				++len;
			}
			//있으면 누적 수 +1  
			else {
				delete DB_tmp;
				iter->num += 1;

			}
		}

		// 입력 시 종료 
		if (getchar() == '\n') break;

	}

	int i;
	std::cout << "모든 단어 누적 수" << std::endl;
	DB_pos = DB_str;
	while (DB_pos != NULL) {
		std::cout << DB_pos->word << "(" << DB_pos->num << ")" << ":";
		for (i = 0; i < DB_pos->num; i++) std::cout << "*";
		std::cout << "\n";
		DB_pos = DB_pos->ptr;
	}


	// 누적 수 기준으로 내림차순 정렬 
	sort(DB_str, len);

	std::cout <<"\n" << "빈도 수 상위 50 단어 누적 수" << std::endl;

	DB_pos = DB_str;
	i = 1;
	while (i <= 50) {
		std::cout << i << ":" << DB_pos->word << "(" << DB_pos->num << ")" << std::endl;
		DB_pos = DB_pos->ptr;
		++i;
	}



	// 메모리 할당 해제 
	DB_del1 = DB_str;
	while (DB_del1 != NULL) {
		DB_del2 = DB_del1->ptr;
		delete DB_del1;
		DB_del1 = DB_del2;
	}


	return 0;
}
