#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    string x, y;

    cin >> x >> y;

    reverse(x.begin(), x.end());
    reverse(y.begin(), y.end());

    int inx = stoi(x);
    int iny = stoi(y);

    if (x > y) {
        cout << inx;
    } else { 
        cout << iny;
    }

    return 0;
}