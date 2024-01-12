#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int cnt = 0;
    
    int i = 1;
    while (i * i <= n) {
        if (n % i == 0) {
            cnt += 2;
        }
        i++;
    }
    
    i--;
    if (i * i == n) {
        cnt--;
    }
    
    return cnt;
}