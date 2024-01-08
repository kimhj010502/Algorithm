#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 1001;

int solution(vector<int> array) {
    vector<int> cnt(N, 0); //cnt[i]: 숫자 i의 개수
    
    int answer = 0; //최빈값
    int max_cnt = 0; //최빈값의 개수
    
    for (int i = 0; i < array.size(); i++) {
        cnt[array[i]]++;
        
        //최빈값 갱신
        if (cnt[array[i]] > max_cnt) {
            max_cnt = cnt[array[i]];
            answer = array[i];
        }
    }
    
    sort(cnt.begin(), cnt.end(), greater<>()); //내림차순으로 정렬
    
    //1번째 원소 또한 answer와 같은 경우 최빈값이 여러개이므로 -1 반환
    if (cnt[1] == max_cnt) {
        return -1;
    }
    return answer;
}