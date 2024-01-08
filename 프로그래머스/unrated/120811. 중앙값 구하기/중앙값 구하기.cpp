#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> array) {
    sort(array.begin(), array.end()); //오름차순으로 정렬
    return array[array.size() / 2];
}