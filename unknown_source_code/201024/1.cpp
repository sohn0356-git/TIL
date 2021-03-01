#include <iostream>
#include <sstream>
using namespace std;

int indegree[26];
int never_catch[26];
int answer[26];
void solution(int numOfAllPlayers, int numOfQuickPlayers, char* namesOfQuickPlayers, int numOfGames, int* numOfMovesPerGame) {
	// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	int size_play = numOfAllPlayers - 1;
	int start_pos = 0;
	int start_player = 0;
	for (int i = 0; i < size_play; i++)
	{
		indegree[i] = i+1;
	}
	for (int i = 0; i < numOfQuickPlayers; i++)
	{
		never_catch[namesOfQuickPlayers[i] - 'A']++;
	}
	for (int g = 0; g < numOfGames; g++)
	{
		answer[start_player]++;
		int next_pos = start_pos + numOfMovesPerGame[g];
		if (next_pos >= size_play)
		{
			next_pos %= size_play;
		}
		while (next_pos < 0)
		{
			next_pos += size_play;
		}
		int next_player = indegree[next_pos];
		if (never_catch[next_player] == 0)
		{
			indegree[next_pos] = start_player;
			start_player = next_player;
		}
		start_pos = next_pos;
	}
	answer[start_player]++;
	for (int i = 0; i < size_play; i++)
	{
		cout << (char)(indegree[i] + 'A') << " " << answer[indegree[i]] << "\n";
	}
	cout << (char)(start_player + 'A') << " " << answer[start_player] << "\n";

}

struct input_data {
	int numOfAllPlayers;
	int numOfQuickPlayers;
	char* namesOfQuickPlayers;
	int numOfGames;
	int* numOfMovesPerGame;
};

void process_stdin(struct input_data& inputData) {
	string line;
	istringstream iss;

	getline(cin, line);
	iss.str(line);
	iss >> inputData.numOfAllPlayers;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	iss >> inputData.numOfQuickPlayers;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
	for (int i = 0; i < inputData.numOfQuickPlayers; i++) {
		iss >> inputData.namesOfQuickPlayers[i];
	}

	getline(cin, line);
	iss.clear();
	iss.str(line);
	iss >> inputData.numOfGames;

	getline(cin, line);
	iss.clear();
	iss.str(line);
	inputData.numOfMovesPerGame = new int[inputData.numOfGames];
	for (int i = 0; i < inputData.numOfGames; i++) {
		iss >> inputData.numOfMovesPerGame[i];
	}
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
	return 0;
}
