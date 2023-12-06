#include <stdio.h>
#include <string.h>

void computePrefixFunction(char pattern[], int m, int pi[]) {
    int k = 0;
    pi[0] = 0;

    for (int q = 1; q < m; q++) {
        while (k > 0 && pattern[k] != pattern[q]) {
            k = pi[k - 1];
        }

        if (pattern[k] == pattern[q]) {
            k++;
        }

        pi[q] = k;
    }
}

void kmpMatcher(char text[], char pattern[]) {
    int n = strlen(text);
    int m = strlen(pattern);
    int pi[m];
    computePrefixFunction(pattern, m, pi);
    int q = 0;

    printf("Prefix Array (pi): ");
    for (int i = 0; i < m; i++) {
        printf("%d ", pi[i]);
    }
    printf("\n");

    for (int i = 0; i < n; i++) {
        while (q > 0 && pattern[q] != text[i]) {
            q = pi[q - 1];
        }

        if (pattern[q] == text[i]) {
            q++;
        }

        if (q == m) {
            printf("Pattern occurs with shift %d\n", i - m + 1);
            q = pi[q - 1];
        }
    }
}

int main() {
    char text[100]; //= "ABABDABACDABABCABAB";
    char pattern[10]; //= "BA";
    printf("Enter the text\n");
    scanf("%s", text);
    printf("Enter the pattern\n");
    scanf("%s", pattern);
    kmpMatcher(text, pattern);

    return 0;
}
