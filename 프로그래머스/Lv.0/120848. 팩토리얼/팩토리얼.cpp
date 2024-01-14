#include <string>
#include <vector>

using namespace std;

const int N = 11;

int solution(int n) {
    if (n == 1) {
        return 1;
    }
    
    vector<int> dp(N, 1); //dp[i]: i!
    
    for (int i = 2; i <= 10; i++) {
        dp[i] = dp[i - 1] * i;
        
        if (n == dp[i]) {
            return i;
        }
    }
    
    for (int i = 2; i <= 10; i++) {
        if (n > dp[i-1] && n < dp[i]) {
            return i-1;
        }
    }
}