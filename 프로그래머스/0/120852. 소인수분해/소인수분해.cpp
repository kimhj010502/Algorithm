#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

vector<int> getPrime(int n) {
    vector<int> prime(n + 1, 1);
    
    for (int i = 2; i * i <= n; i++) {
        if (prime[i] != 1) {
            continue;
        }
        
        for (int j = i * 2; j <= n; j += i) {
            prime[j] = i;
        }
    }
    
    return prime;
}

vector<int> solution(int n) {
    set<int> s;
    vector<int> prime = getPrime(n);

    //n이 소수인 경우
    if (prime[n] == 1){
        return { n };
    }
    
    while (true) {
        s.insert(prime[n]);
        n /= prime[n];
        
        if (prime[n] == 1) {
            s.insert(n);
            break;
        }
    }
    
    vector<int> answer;
    for (auto iter: s) {
        answer.push_back(iter);
    }
    return answer;
}