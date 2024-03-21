#include <stdio.h>

int main() {
    int minutes;
    printf("Enter number of minutes played: ");
    scanf("%d", &minutes);
    if (minutes > 120) {
        printf("You played games for too long\n");
        return 0;
    }
    printf("You are under your time limit\n");
    return 0;
}