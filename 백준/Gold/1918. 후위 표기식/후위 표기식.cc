#include <iostream>
#include <stack>

using namespace std;


//연산자 우선순위 반환 
int priority(char ch) {
    switch (ch) {
        case '(': return 0;
        case '+': case '-': return 1;
        case '*': case '/': return 2;
    }
}

//중위표기식 -> 후위표기식 
string postfix(string input) {
    string output = "";
    stack<char> s;
    
    for (int i = 0; i < input.size(); i++) {
        char ch = input[i];
        
        switch (ch) {
            case '(':
                s.push(ch);
                break;
            
            case ')':
                while(!s.empty() && s.top() != '(') {
                    output += s.top();
                    s.pop();
                }
                s.pop(); //여는 괄호 삭제
                break;
            
            case '+': case '-': case '*': case '/':
                while (!s.empty() && priority(ch) <= priority(s.top()) ) {
                    output += s.top();
                    s.pop();
                }
                s.push(ch);
                break;
            
            //알파벳 (피연산자) 
            default:
                output += ch;
        }
    }
    
    while(!s.empty()) {
        output += s.top();
        s.pop();
    }
    
    return output;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    //입력
    string input;
    
    cin >> input;
    
    //입력 & 출력 
    cout << postfix(input);
    
    return 0;
}