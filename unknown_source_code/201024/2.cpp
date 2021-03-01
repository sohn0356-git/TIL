#include <iostream>
#include <sstream>
using namespace std;

int building[101];

void solution(int day, int width, int** blocks) {
	// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	int answer = 0;
	for (int d = 0; d < day; d++)
	{
		for (int i = 0; i < width; i++)
		{
			building[i] += blocks[d][i];
		}
		for (int i = 1; i < width - 1; i++)
		{
			int left = 0;
			int right = 0;
			for (int j = 0; j < i; j++)
			{
				if (left < building[j])
				{
					left = building[j];
				}
			}
			for (int j = i+1; j < width; j++)
			{
				if (right < building[j])
				{
					right = building[j];
				}
			}
			if (left > right)
			{
				left = right;
			}
			if (building[i] > left)
			{
				continue;
			}
			answer += left - building[i];
			building[i] = left;
		}
	}
	cout << answer;
}

struct input_data {
	int day;
	int width;
	int** blocks;
};

void process_stdin(struct input_data& inputData) {
	string line;
	istringstream iss;

	getline(cin, line);
	iss.str(line);
	iss >> inputData.day;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	iss >> inputData.width;

	inputData.blocks = new int* [inputData.day];
	for (int i = 0; i < inputData.day; i++) {
		getline(cin, line);
		iss.clear();
		iss.str(line);
		inputData.blocks[i] = new int[inputData.width];
		for (int j = 0; j < inputData.width; j++) {
			iss >> inputData.blocks[i][j];
		}
	}
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.day, inputData.width, inputData.blocks);
	return 0;
}
