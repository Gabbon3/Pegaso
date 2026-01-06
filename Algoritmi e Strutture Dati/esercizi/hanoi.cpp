#include <iostream>
using namespace std;

void hanoi(int n, int A, int C, int B) {
    if (n == 1) {
        cout << A << " -> " << C << endl;
    } else {
        hanoi(n - 1, A, B, C);
        cout << A << " -> " << endl;
        hanoi(n - 1, B, C, A);
    }
}

int main() {
    cout << "Hanoi Tower" << endl;
    hanoi(3, 1, 3, 2);
}