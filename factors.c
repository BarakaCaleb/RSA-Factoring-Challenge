#include <stdio.h>

/**
 * main - The main entry to the program
 *
 * Return: Always 0 in success
 */

int main()
{
	long long int number = 239809320265259;
	long int factor one = 2;
	long int factor two;

	while (number % factor one)
	{
		if (factor one <= number)
		{
			factor one++;
		}
		else
		{
			return (-1);
		}
	}

	factor two = number / factor one;
	printf("%lld = %ld * %ld\n, number, factor two, factor one");
	return (0);
}
