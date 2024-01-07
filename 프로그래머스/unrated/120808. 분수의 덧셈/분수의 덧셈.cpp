#include <string>
#include <vector>

using namespace std;

//a > b일 때, a와 b의 최대공약수 반환
int getGcd(int a, int b) {
    while (b) {
        a = a % b;
        swap(a, b);
    }
    return a;
}

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    int numer = numer1 * denom2 + numer2 * denom1; //분자
    int denom = denom1 * denom2; //분모
    
    //값이 1인 경우
    if (numer == denom) {
        return {1, 1};
    }
    
    int gcd = getGcd(max(numer, denom), min(numer, denom)); //분자와 분모의 최대공약수
    
    return {numer / gcd, denom / gcd}; //기약분수의 분자, 분모 반환
}