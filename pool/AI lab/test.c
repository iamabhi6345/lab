#include <stdio.h>
#include <stdlib.h>

// Define a structure for the max stack
typedef struct {
    int* mainStack;
    int* maxStack;
    int top;
} MaxStack;

// Function to initialize the max stack
MaxStack* createMaxStack(int maxSize) {
    MaxStack* stack = (MaxStack*)malloc(sizeof(MaxStack));
    stack->mainStack = (int*)malloc(maxSize * sizeof(int));
    stack->maxStack = (int*)malloc(maxSize * sizeof(int));
    stack->top = -1;
    return stack;
}

// Function to push an element onto the max stack
void push(MaxStack* stack, int x) {
    // Update main stack
    stack->top++;
    stack->mainStack[stack->top] = x;

    // Update max stack
    if (stack->top == 0 || x >= stack->maxStack[stack->top - 1]) {
        stack->maxStack[stack->top] = x;
    } else {
        stack->maxStack[stack->top] = stack->maxStack[stack->top - 1];
    }
}

// Function to pop an element from the max stack
int pop(MaxStack* stack) {
    if (stack->top == -1) {
        fprintf(stderr, "Stack is empty\n");
        exit(EXIT_FAILURE);
    }

    int popped = stack->mainStack[stack->top];
    stack->top--;

    return popped;
}

// Function to get the top element of the max stack
int top(MaxStack* stack) {
    if (stack->top == -1) {
        fprintf(stderr, "Stack is empty\n");
        exit(EXIT_FAILURE);
    }

    return stack->mainStack[stack->top];
}

// Function to get the maximum element in the max stack
int getMax(MaxStack* stack) {
    if (stack->top == -1) {
        fprintf(stderr, "Stack is empty\n");
        exit(EXIT_FAILURE);
    }

    return stack->maxStack[stack->top];
}

void freeMaxStack(MaxStack* stack) {
    free(stack->mainStack);
    free(stack->maxStack);
    free(stack);
}

int main() {
    MaxStack* maxStack = createMaxStack(100);

    push(maxStack, 5);
    push(maxStack, 2);
    push(maxStack, 10);

    printf("Max: %d\n", getMax(maxStack)); 

    pop(maxStack);

    printf("Max after pop: %d\n", getMax(maxStack));  

    freeMaxStack(maxStack);

    return 0;
}
