#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct min_heap {
    int data;
    int i2, i3, i5;
};

struct min_heap* newmin_heap(int data, int i2, int i3, int i5) {
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
    int* arr = (int*)malloc(sizeof(int) * n);
    int idx2 = 0, idx3 = 0, idx5 = 0;

    // Create a min-heap of struct min_heap pointers
    struct min_heap** min_heap_arr = (struct min_heap**)malloc(sizeof(struct min_heap*) * n);
    min_heap_arr[0] = newmin_heap(1, 0, 0, 0);

    for (int i = 0; i < n; i++) {
        struct min_heap* min_node = min_heap_arr[0];
        arr[i] = min_node->data;

        // Update indices for the next candidates
        idx2 = min_node->i2;
        idx3 = min_node->i3;
        idx5 = min_node->i5;

        // Generate the next candidates and add them to the min-heap
        min_heap_arr[0] = newmin_heap(arr[idx2] * 2, idx2 + 1, idx3, idx5);
        min_heap_arr[0]->data = (min_heap_arr[0]->data < arr[idx3] * 3) ? min_heap_arr[0]->data : arr[idx3] * 3;
        min_heap_arr[0]->data = (min_heap_arr[0]->data < arr[idx5] * 5) ? min_heap_arr[0]->data : arr[idx5] * 5;

        // Re-heapify the min-heap
        minHeapify(min_heap_arr, i + 1, 0);
    }

    // Clean up the min-heap
    free(min_heap_arr[0]);
    free(min_heap_arr);

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
    printf("The %d-th number of the array is: %d\n", n, nth_number);
    return 0;
}
