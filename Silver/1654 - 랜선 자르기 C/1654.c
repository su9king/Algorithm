#include <stdio.h>

int num1, num2;
int list[1000000];

long long check(long long mid) {
    long long sum = 0;
    for (int i = 0; i < num1; i++) {
        sum += list[i] / mid;
    }
    return sum;
}

int main() {
    scanf("%d %d", &num1, &num2);
    long long high = 0, low = 1;
    
    for (int i = 0; i < num1; i++) {
        scanf("%d", &list[i]);
        if (high < list[i]) {
            high = list[i];
        }
    }

    long long result = 0;
    while (low <= high) {
        long long mid = (high + low) / 2;
        if (check(mid) < num2) {
            high = mid - 1;
        } else {
            result = mid; // 가능한 최대 길이 업데이트
            low = mid + 1;
        }
    }

    printf("%lld\n", result);
    return 0;
}
