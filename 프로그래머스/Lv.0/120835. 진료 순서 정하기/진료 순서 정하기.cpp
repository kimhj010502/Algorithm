#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> emergency) {
    //sorted.first 배열에 복사
    vector<int> sorted(emergency.size());
    for (int i = 0; i < sorted.size(); i++) {
        sorted[i] = emergency[i];
    }
    
    //sorted 배열 내림차순으로 정렬
    sort(sorted.begin(), sorted.end(), greater<int>());
    
    //answer 반환
    vector<int> answer;
    for (int i = 0; i < emergency.size(); i++) {
        int index = find(sorted.begin(), sorted.end(), emergency[i]) - sorted.begin();
        answer.push_back(index + 1);

    }
    return answer;
}