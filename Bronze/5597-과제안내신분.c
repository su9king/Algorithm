#include <stdio.h>

int main() {
    int submitted[30] = {0}; // 30명의 학생 번호(0~29)
    int studentNumber;

    // 제출한 학생의 번호 입력
    for (int i = 0; i < 28; i++) {
        scanf("%d", &studentNumber);
        submitted[studentNumber - 1] = 1; // 제출한 학생 표시
    }

    // 제출하지 않은 학생 출력
    for (int i = 0; i < 30; i++) {
        if (submitted[i] == 0) {
            printf("%d\n", i + 1); // 학생 번호는 1부터 시작
        }
    }

    return 0;
}
