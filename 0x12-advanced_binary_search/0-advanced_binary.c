#include "search_algos.h"


/**
 * print_array - Entry point
 *
 * @array: Array
 * @first: Size of array
 * @last: Value to find
 * Return: Always EXIT_SUCCESS
 */
void print_array(int *array, int first, int last)
{
	int i;

	printf("Searching in array: ");
	for (i = first; i < last; i++)
		printf("%d, ", array[i]);
	printf("%d", array[i]);
	printf("\n");
}

/**
 * rec_bin - Recursive advanced binary search
 * @array: Array
 * @first: First element of array
 * @last: Last element of array
 * @value: Value to find
 * Return: Always EXIT_SUCCESS
 */

int rec_bin(int *array, size_t first, size_t last, int value)
{
	size_t half;

	if (first < last)
	{
		half = first + (last - first) / 2;
		print_array(array, (int)first, (int)last);
		if (array[half] >= value)
			return (rec_bin(array, first, half, value));
		else
			return (rec_bin(array, half + 1, last, value));
				return ((int)(half));
	}
	if (array[first] == value)
		return (first);
	print_array(array, (int)first, (int)last);
	return (-1);
}


/**
 * advanced_binary - Entry point
 *
 * @array: Array
 * @size: Size of array
 * @value: Value to find
 * Return: Always EXIT_SUCCESS
 */
int advanced_binary(int *array, size_t size, int value)
{
	size_t first;
	size_t last;

	if (!array)
		return (-1);

	first = 0;
	last = size - 1;
	return (rec_bin(array, first, last, value));

}
