#include <stdio.h>
#include <string.h>

// Define your hash function d^(m-1) mod q here if not already defined
// You also need to define d and q accordingly.

int RabinKarpMatcher(char T[], char P[], int d, int q) {
    int n = strlen(T);
    int m = strlen(P);
    int spuriousHits = 0;

    // Calculate h
    int h = 1;
    for (int i = 0; i < m - 1; i++) {
        h = (h * d)
         % q;
    }

    // Calculate initial hash values
    int p = 0;
    int t0 = 0;
    for (int i = 0; i < m; i++) {
        p = (d * p + P[i]) % q;
        t0 = (d * t0 + T[i]) % q;
    }

    for (int s = 0; s <= n - m; s++) {
        if (p == t0) {
            // Possible matching, now test to eliminate spurious hits
            if (strncmp(P, T + s, m) == 0) {
                printf("Pattern occurs with shift %d\n", s);
            } else {
                printf("Spurious hit at shift %d\n", s);
                spuriousHits++;
            }
        }
        if (s < n - m) {
            t0 = (d * (t0 - T[s] * h) + T[s + m]) % q;
            if (t0 < 0) {
                t0 += q;
            }
        }
    }

    return spuriousHits;
}

int main() {
    char T[100];
    printf("Enter the  text\n");
    scanf("%s", T);
    char P[10];
    printf("Enter the pattern\n");
    scanf("%s", P);
    int d = 256;             // Radix
    int q = 11;              // Prime

    int totalSpuriousHits = RabinKarpMatcher(T, P, d, q);

    printf("Total spurious hits: %d\n", totalSpuriousHits);

    return 0;
}
