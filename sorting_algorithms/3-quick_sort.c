#include "sort.h"
/**
 *quick_sort - sorts an array of integers in ascending order
 *@array: array
 *@size: size of array
 *Return: nothing
 */
void quick_sort(int *array, size_t size)
{
	if (array == NULL || size < 2)
		return;

	sorter(array, 0, size - 1, size);
}
/**
 *sorter - recursion for quick-sort
 *@array: the array
 *@start: start of array
 *@next: next number
 *@size: the size
 *Return: piv index
 */

void sorter(int *array, ssize_t start, ssize_t next, size_t size)
{
	if (start < next)
	{
		int piv = partitioner(array, start, next, size);

		sorter(array, start, piv - 1, size);
		sorter(array, piv + 1, next, size);
	}
}

/**
 * swaper - swap numbers
 * @a: int a
 * @b: int
 * Return: Nothing
 */
void swaper(int *a, int *b)
{
	int i = *a;
	*a = *b;
	*b = i;
}

/**
 *partitioner - defines array partition
 *@array: the array
 *@start: start of array
 *@next: next number
 *@size: the size
 *Return: pivot index
 */

int partitioner(int *array, ssize_t start, ssize_t next, size_t size)
{
	int piv = array[next];
	ssize_t j = start, i;

	for (i = start; i < next; i++)
	{
		if (array[i] < piv)
		{
			if (j != i)
			{
				swaper(&array[j], &array[i]);
				print_array(array, size);
			}

			j++;
		}
	}
	if (next != j && array[next] != array[j])
	{
		swaper(&array[next], &array[j]);
		print_array(array, size);
	}
	return (j);
}
