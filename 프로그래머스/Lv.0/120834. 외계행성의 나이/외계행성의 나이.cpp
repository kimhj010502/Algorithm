#include <string>

using namespace std;

const int ALPHABET = 97;

string solution(int age) {
    string answer = "";
    string s = to_string(age); //string 형의 나이
    for (int i = 0; i < s.size(); i++) {
        answer += (char)(s[i] - '0' + ALPHABET);
    }
    return answer;
}