#include <iostream>

using namespace std;

int main(void) {
    //입력
    int n;
    cin >> n;
    
    //연산 & 출력
    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << "\n";
    }
    
    return 0;
}