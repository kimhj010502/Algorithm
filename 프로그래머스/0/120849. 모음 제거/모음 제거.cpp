#include <string>
#include <vector>

using namespace std;

//모음인지 여부 반환
bool isVowels(char c) {
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        return true;
    }
    return false;
}

string solution(string my_string) {
    string answer = "";
    
    for (int i = 0; i < my_string.size(); i++) {
        if (isVowels(my_string[i])) {
            continue;
        }
        answer += my_string[i];
    }
    
    return answer;
}