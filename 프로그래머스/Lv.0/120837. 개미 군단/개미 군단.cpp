#include <string>
#include <vector>

using namespace std;

const int A = 5, B = 3, C = 1;

int solution(int hp) {
    int a = 0, b = 0, c = 0; //장군개미, 병정개미
    
    a = hp / A;
    hp %= A;
    
    b = hp / B;
    hp %= B;
    
    c = hp;
    
    return a + b + c;
}