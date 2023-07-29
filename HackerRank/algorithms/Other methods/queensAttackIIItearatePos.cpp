#include <bits/stdc.h>

using namespace std;

int queensAttack(int n, int k, int queenX, int queenY, vector<vector<int>> obstacles)
{
    int total = 0;
    int directions[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
    for (auto direction : directions)
    {
        int Tx = queenX;
        int Ty = queenY;
        int c = 0;
        while (true)
        {
            Tx += direction[0];
            Ty += direction[1];
            if (count(obstacles.begin(), obstacles.end(), vector<int>{Tx, Ty}) || (Tx == 0) || (Ty == 0) || (Tx > n) || (Ty > n))
            {
                break;
            }
            else
            {
                c++;
            }
        }
        total += c;
    }
    return total;
}

int main()
{
    cout << queensAttack(8, 3, 4, 4, {{4, 2}, {4, 3}, {4, 7}});
}