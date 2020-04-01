#include <stdlib.h>
#include <stdio.h>

#include "palindrome.h"

/**
 * is_palindrome - Function to check palindromes
 *
 * @n: Number to be checked
 *
 * Return: 0 or 1
 */
int is_palindrome(unsigned long n)
{
	unsigned long t, r = 0;

	t = n;

	while (t != 0)
	{
		r = r * 10;
		r = r + t % 10;
		t = t / 10;
	}
	if (n == r)
		return (1);
	else
		return (0);
}
