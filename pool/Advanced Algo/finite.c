#include <stdio.h>
#include <string.h>

#define ALPHABET_SIZE 256

void ComputeTransitionFunction(char P[], int m, int delta[][ALPHABET_SIZE]) {
    int q, a, k;
    for (q = 0; q <= m; q++) {
        for (a = 0; a < ALPHABET_SIZE; a++) {
            k = (q + 1) < m ? (q + 1) : m;
            while (k > 0 && P[k - 1] != a)
                k--;
            delta[q][a] = k;
        }
    }
}

void FiniteAutomatonMatcher(char T[], char P[], int delta[][ALPHABET_SIZE]) {
    int n = strlen(T);
    int m = strlen(P);
    int q = 0;

    ComputeTransitionFunction(P, m, delta);

    for (int i = 0; i < n; i++) {
        q = delta[q][T[i]];

        if (q == m) {
            printf("Pattern occurs with shift %d\n", i - m + 1);
        }
    }
}

int main() {
    char T[] = "ABABDABC";
    char P[] = "AB";
    int delta[strlen(P) + 1][ALPHABET_SIZE];

    FiniteAutomatonMatcher(T, P, delta);

    return 0;
} 
