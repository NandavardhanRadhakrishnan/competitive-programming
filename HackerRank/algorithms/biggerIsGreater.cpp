// https://www.hackerrank.com/challenges/bigger-is-greater/
// given a word find smallest word which is bigger than the given word, with only swapping letters, if not possible then return "no answer"

// algorithm used next permutation
// https://medium.com/@studying1999/bigger-is-greater-problem-comprehensive-explanation-b2ea7eacc0b2

#include <bits/stdc.h>
using namespace std;

string biggerIsGreater(string w) {
    if (next_permutation(w.begin(), w.end())) {
        return w;
    }
    else {
        return "no answer";
    }
}

int main() {
    string s = "abcd";
    cout << biggerIsGreater(s);
}