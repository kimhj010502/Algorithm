#include <string>
#include <vector>

using namespace std;

const int PIZZA = 6;

//최소공배수 반환
int getLcm(int a, int b) {
    int multi = a * b;
    
    //최대공약수 구하기
    while (b) {
        a %= b;
        swap(a, b);
    }
    return multi / a; //LCM = a * b / GCD
}

int solution(int n) {
    //n이 6인 경우 1 반환
    if (n == PIZZA) {
        return 1;
    }
    
    //n과 6의 최소공배수
    int lcm = getLcm(max(n, PIZZA), min(n, PIZZA));
    return lcm / PIZZA;
}