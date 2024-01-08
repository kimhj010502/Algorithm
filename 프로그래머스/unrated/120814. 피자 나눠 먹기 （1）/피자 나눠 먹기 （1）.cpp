#include <string>
#include <vector>

using namespace std;

const int PIZZA = 7;

int solution(int n) {
    if (n % PIZZA == 0) {
        return n / PIZZA;
    }
    return n / PIZZA + 1;
}