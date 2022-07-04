// Example solution in CPP17 tha fails some tests in sum of two numbers problem

#include <iostream>
using namespace std;

int main() {
    int n, a, b;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> a >> b;
        if(a + b == 4)
            cout << 3 << "\n";
        cout << a + b << "\n";
    }
    return 0;
}
