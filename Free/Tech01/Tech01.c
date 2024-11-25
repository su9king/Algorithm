#include <stdio.h>
#include <stdlib.h>

int main() {
    int initial_size = 5;
    int *arr = (int *)malloc(initial_size * sizeof(int)); // 5개의 정수 공간 할당

    // 배열 초기화 
    for (int i = 0; i < initial_size; i++) {
        arr[i] = i + 1;
        printf("%d ", arr[i]);
    }

    // 배열 크기 변경
    int new_size = 10;
    arr = (int *)realloc(arr, new_size * sizeof(int)); // 크기를 10으로 확장

    // 새로운 값 추가
    for (int i = initial_size; i < new_size; i++) {
        arr[i] = i + 1;
    }

    // 배열 출력
    for (int i = 0; i < new_size; i++) {
        printf("%d ", arr[i]);
    }

    free(arr); // 메모리 해제
    return 0;
}
