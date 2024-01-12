#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    //n이 홀수인 경우 짝수로 만듦
    if (n % 2 == 1) {
        n--;
    }
    
    int answer = 0;
    for (int i = 2; i <= n; i += 2) {
        answer += i;
    }
    return answer;
}