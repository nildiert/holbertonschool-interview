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
	size_t half;
	size_t last;
	size_t first_value;

	if (!array)
		return (-1);

	first_value = 0;
	first = 0;
	last = size - 1;
	while (first <= last)
	{
		print_array(array, (int)first, (int)last);
		half = first + (last - first) / 2;
		if (array[half] == value)
		{
			if (array[half - 1] == value)
				first_value = 1;
			else
				return ((int)(half));
		}
		if (array[half] < value)
			first = half + 1;
		else
		{
			if (first_value)
			{
				last = half;
				first_value = 0;
			}
			else
				last = half - 1;
		}
	}

	return (-1);
}
