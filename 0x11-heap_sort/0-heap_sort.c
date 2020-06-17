#include "sort.h"

void swap(int *a, int *b, int *array, size_t n) {

	int temp = *a;
	*a = *b;
	*b = temp;
	print_array(array, n);
}


void heapify(int *arr, int n, int i, size_t size) {
	/* Find largest among root, left child and right child */

	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < n && arr[left] > arr[largest])
		largest = left;

	if (right < n && arr[right] > arr[largest])
		largest = right;

	/* Swap and continue heapifying if root is not largest */
	if (largest != i) {
		swap(&arr[i], &arr[largest], arr, size);
		heapify(arr, n, largest, size);
	}

}



void heap_sort(int *array, size_t size)
{

	size_t i;
	/* Build max heap */
	for (i = size / 2 ; i > 0; i--)
		heapify(array, size, i - 1, size);

	/* Heap sort */
	for (i = size - 1; i > 0; i--) {
		swap(&array[0], &array[i], array, size);

		/* Heapify root element to get highest element at root again */
		heapify(array, i, 0, size);
	}
}
