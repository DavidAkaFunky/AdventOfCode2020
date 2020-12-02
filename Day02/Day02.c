#include <stdio.h>
#include<stdlib.h>

int part1(FILE* fp){
    char letter;
    char string[30];
    int total, valid = 0, min, max;
    while (fscanf(fp, "%d-%d %c: %s", &min, &max, &letter, string) > 0) {
        total = 0;
        for (int i = 0; string[i]; i++)
            if (string[i] == letter)
                total++;
        if (min <= total && total <= max)
            valid++;
    }
    return valid;
}

int part2(FILE* fp){
    char letter;
    char string[30];
    int valid = 0;
    int arg1, arg2;
    while (fscanf(fp, "%d-%d %c: %s", &arg1, &arg2, &letter, string) > 0) {
        if (string[arg1-1] == letter && string[arg2-1] != letter || string[arg2-1] == letter && string[arg1-1] != letter)
            valid++;
    }
    return valid;
}

int main(){
    FILE* fp = fopen("input.txt", "r");
    if (!fp)
        return 1;
    printf("%d\n", part1(fp));
    rewind(fp);
    printf("%d\n", part2(fp));
    return 0;
}