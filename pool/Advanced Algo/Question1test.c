#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct min_heap {
    int data; 
    int i2, i3, i5;     
};
struct min_heap* newmin_heap(int data, int i2,  int i3, int i5) {
    struct min_heap* node = (struct min_heap*)malloc(sizeof(struct min_heap));
    node->data = data;
    node->i2 = i2;
    node->i3 = i3;
    node->i5 = i5;
    return node;
}


void minHeapify(struct min_heap** heap, int heap_size, int r_i) {
    int smallest = r_i;
    int left_child = 2 * r_i + 1;
    int right_child = 2 * r_i + 2;

    if (left_child < heap_size && heap[left_child]->data < heap[smallest]->data)
        smallest = left_child;

    if (right_child < heap_size && heap[right_child]->data < heap[smallest]->data)
        smallest = right_child;

    if (smallest != r_i) {
        struct min_heap* temp = heap[r_i];
        heap[r_i] = heap[smallest];
        heap[smallest] = temp;

        minHeapify(heap, heap_size, smallest);
    }
}


 int findNthNumber(int n) {
    int* arr = ( int*)malloc(sizeof( int) * n);
    int idx2 = 0, idx3 = 0, idx5 = 0;
    
    arr[0] = 1;

    for (int i = 1; i < n; i++) {
         int num2 = arr[idx2] * 2;
         int num3 = arr[idx3] * 3;
         int num5 = arr[idx5] * 5;

        arr[i] = (num2 < num3) ? ((num2 < num5) ? num2 : num5) : ((num3 < num5) ? num3 : num5);

        if (arr[i] == num2) idx2++;
        if (arr[i] == num3) idx3++;
        if (arr[i] == num5) idx5++;
    }

    int result = arr[n - 1];
    free(arr);
    return result;
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("n should be a positive integer.\n");
        return 1;
    }

  int nth_number = findNthNumber(n);
    printf("The %d-th number of the arr is: %d\n", n, nth_number);
    return 0;
}
