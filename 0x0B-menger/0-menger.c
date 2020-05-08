#include "menger.h"

/**
 * menger - Entry point
 *
 * @level: Level of menger sponge
 *
 */

void menger(int level)
{
	int size, i, j, x, y;
	char s;

	size = pow(3, level);

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size;)
		{
			s = '#';
			x = i;
			y = j++;
			while (x > 0 || y > 0)
			{
				if (x % 3 == 1 && y % 3 == 1)
					s = ' ';
				x /= 3;
				y /= 3;
			}
			printf("%c", s);
		}
		printf("\n");
	}

}
