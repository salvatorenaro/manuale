#include <iostream>
using namespace std;

int main() {
    int x, y;
    cin >> x >> y;

    if (x > y) {
        swap(x, y);
    }

    int b[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    for (int i = 0; i < 10; ++i) {
        if (b[i] < x) {
            b[i] = x;
        }
        else if (b[i] > y) {
            b[i] = y;
        }
        cout << b[i] << "\n";
    }

    return 0;
}
