// https://www.hackerrank.com/challenges/queens-attack-2/
// find number of squares a queen can attack given k obstacles at (xi,yi) on a nxn board

#include <bits/stdc.h>
using namespace std;

int queensAttack(int n, int k, int queenY, int queenX, vector<vector<int>> obstacles)
{

    int top = n - queenY;
    int bottom = queenY - 1;
    int right = n - queenX;
    int left = queenX - 1;
    int topRight = min(top, right);
    int bottomRight = min(bottom, right);
    int bottomLeft = min(bottom, left);
    int topLeft = min(top, left);

    for (int i = 0; i < k; i++)
    {
        int obsX = obstacles[i][1];
        int obsY = obstacles[i][0];

        // obs above queen
        if (queenY < obsY)
        {

            // on top
            if (queenX == obsX)
            {
                top = min(top, abs(obsY - queenY) - 1);
            }

            // on top right
            else if ((queenX < obsX) && (obsX - queenX == obsY - queenY))
            {
                topRight = min(topRight, (obsX - queenX) - 1);
            }

            // on top left
            else if ((queenX > obsX) && (queenX - obsX == obsY - queenY))
            {
                topLeft = min(topLeft, (queenX - obsX) - 1);
            }
        }

        // obs below queen
        if (queenY > obsY)
        {

            // on bottom
            if (queenX == obsX)
            {
                bottom = min(bottom, abs(queenY - obsY) - 1);
            }

            // on bottom right
            else if ((queenX < obsX) && (obsX - queenX == queenY - obsY))
            {
                bottomRight = min(bottomRight, (obsX - queenX) - 1);
            }

            // on bottom left
            else if ((queenX > obsX) && (queenX - obsX == queenY - obsY))
            {
                bottomLeft = min(bottomLeft, (queenX - obsX) - 1);
            }
        }

        // obs on side of queen
        if (queenY == obsY)
        {

            // on left
            if (queenX > obsX)
            {
                left = min(left, (queenX - obsX) - 1);
            }

            // on right
            else if (queenX < obsX)
            {
                right = min(right, (obsX - queenX) - 1);
            }
        }
    }
    int totalAttack = top + topRight + right + bottomRight + bottom + bottomLeft + left + topLeft;
    return totalAttack;
}

int main()
{
    cout << queensAttack(8, 3, 4, 4, {{4, 2}, {4, 3}, {4, 7}});
}