#include <iostream>
#include <vector>

using namespace std;

const int SIZE = 50;
const int CLEAN = 2;
int n, m; //방의 크기
int cnt = 0; //청소한 칸 개수

vector<vector<int>> board(SIZE, vector<int>(SIZE)); //방 (0: 빈 칸, 1: 벽, 2: 청소 완료)

//4가지 방향: { 북, 동, 남, 서 }
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

void dfs(int row, int col, int dir) {
    //1. 현재 위치 청소
    if (board[row][col] != CLEAN) {
        cnt++;
        board[row][col] = CLEAN;
    }

    //[현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는가]
    //3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for (int i = 0; i < 4; i++) { //3-1. 반시계 방향으로 90º 회전
        int new_dir = (dir - i + 3) % 4;
        int new_row = row + dy[new_dir], new_col = col + dx[new_dir];

        if (board[new_row][new_col] == 0) { //3-2. 아직 청소되지 않은 빈 칸 발견
            dfs(new_row, new_col, new_dir); //한 칸 전진
            return;
        }
    }

    //2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    int back_dir = (dir + 2) % 4;
    int back_row = row + dy[back_dir], back_col = col + dx[back_dir];

    //[바라보는 방향을 유지한 채로 한 칸 후진할 수 있는가]
    //2-2. 뒤쪽 칸이 벽이라 후진할 수 없는 경우
    if (board[back_row][back_col] == 1) {
        return;
    }

    //2-1. 바라보는 방향을 유지한 채로 한 칸 후진
    dfs(back_row, back_col, dir); //방향 유지한 상태로 후진 (2-3)
    return;
}

int main() {
    int r, c, d; //로봇 청소기 정보

    //입력
    cin >> n >> m;
    cin >> r >> c >> d;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    //연산
    dfs(r, c, d);

    //출력
    cout << cnt;

    return 0;
}