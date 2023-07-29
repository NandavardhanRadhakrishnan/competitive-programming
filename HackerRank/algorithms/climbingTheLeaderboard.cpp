// https://www.hackerrank.com/challenges/climbing-the-leaderboard
// for dense ranking, current leaderboard given in : ranked, player's score after each game given in:player, track and display rank after every game

#include <bits/stdc.h>
using namespace std;


vector<int> climbingLeaderboard(vector<int> ranked, vector<int> player) {
	ranked.erase(unique(ranked.begin(), ranked.end()), ranked.end());
	vector<int> resultRanks;
	for (auto rank : player) {
		auto it = lower_bound(ranked.begin(), ranked.end(), rank, std::greater<int>());
		int idx = distance(ranked.begin(), it);
		resultRanks.push_back(idx + 1);
	}
	return resultRanks;
}



int main() {
	vector<int> r = { 100,90,90,80 };
	vector<int> p = { 70,80,105 };
	vector<int> res;
	res = climbingLeaderboard(r, p);
	for (auto x : res) {
		cout << x << "|";
	}
}