#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

struct Node {
    int data[SIZE];
    struct Node* next;
};

typedef struct Node Node;

Node* start = NULL;

void initializeNode(Node* node) {
    for (int p = 0; p < SIZE; p++) {
        node->data[p] = 0;
    }
    node->next = NULL;
}

void createNode(Node* newNode, int v[], int n1) {
    for (int s = 0; s < n1; s++) {
        newNode->data[s] = v[s];
    }
    newNode->next = NULL;
}

int main() {
    int n, events, sent, receive, sentE, recE, commLines = 0;
    Node* temp;
    Node* proc[SIZE];  // array of processes
    printf("Enter no. of processes: ");
    scanf("%d", &n);
    int vector[n];  // representation of data

    /*----------------INITIALIZATION LOOP-------------------------*/
    for (int i = 0; i < n; i++) {  // number of processes
        for (int v = 0; v < n; v++) {
            vector[v] = 0;
        }

        printf("Enter no. of events in process %d: ", i + 1);
        scanf("%d", &events);

        for (int j = 1; j <= events; j++) {
            vector[i] = j;
            Node* newnode = (Node*)malloc(sizeof(Node));
            if (newnode == NULL) {
                perror("Memory allocation failed");
                return 1;
            }
            initializeNode(newnode);
            createNode(newnode, vector, n);
            if (start == NULL) {
                start = newnode;
                temp = start;
            } else {
                temp->next = newnode;
                temp = temp->next;
            }
        }
        proc[i] = start;
        start = NULL;
    }

    /*-------------------DATA GATHERING--------------------*/
    printf("\nEnter the number of communication lines: ");
    scanf("%d", &commLines);
    Node* tempS, * tempR;

    for (int i = 0; i < commLines; i++) {
        printf("\nEnter the sending process: ");
        scanf("%d", &sent);
        printf("\nEnter the receiving process: ");
        scanf("%d", &receive);
        printf("\nEnter the sending event number: ");
        scanf("%d", &sentE);
        printf("\nEnter the receiving event number: ");
        scanf("%d", &recE);

        tempS = proc[sent - 1];
        tempR = proc[receive - 1];

        for (int j = 1; j < sentE; j++)
            tempS = tempS->next;

        for (int j = 1; j < recE; j++)
            tempR = tempR->next;

        for (int j = 0; j < n; j++) {
            tempR->data[j] = (tempR->data[j] < tempS->data[j]) ? tempS->data[j] : tempR->data[j];
        }
    }

    /*-------------------DISPLAYING------------------------*/
    printf("\nThe resulting vectors are:\n\n");
    for (int k = 0; k < n; k++) {
        printf("Process %d: ", k + 1);

        Node* temp1 = proc[k];
        while (temp1) {
            printf("(");
            for (int f = 0; f < n - 1; f++)
                printf("%d,", temp1->data[f]);

            printf("%d)", temp1->data[n - 1]);
            temp1 = temp1->next;
        }
        printf("\n");
    }

    /*-------------------FREE MEMORY-----------------------*/
    for (int i = 0; i < n; i++) {
        Node* current = proc[i];
        while (current != NULL) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }

    return 0;
}

