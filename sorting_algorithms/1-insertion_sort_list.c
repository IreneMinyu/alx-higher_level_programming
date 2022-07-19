#include "sort.h"
/**
 * insertion_sort_list - order a dll
 * @list: Double ll
 * Return: Nothing
 */

void insertion_sort_list(listint_t **list)
{
	listint_t *tmp = NULL, *tmp2 = NULL, *tmp3 = NULL;

	if (list == NULL || *list == NULL || (*list)->next == NULL)
	{
		return;
	}
	tmp = *list;
	while (tmp)
	{
		if (tmp->prev)
		{
			if (tmp->prev->n > tmp->n)
			{
				tmp2 = tmp;
				tmp3 = tmp;
				swap(list, tmp->prev, tmp);
				tmp = tmp->next;
				print_list(*list);
				while (tmp3)
				{
					if (tmp3->n > tmp2->n)
					{
						swap(list, tmp3, tmp2);
						print_list(*list);
					}
					tmp3 = tmp3->prev;
				}
			}
		}
		tmp = tmp->next;
	}
}
/**
 * swap - swap the nodes of the list
 * @list: Double ll
 * @node1: Node 1
 * @node2: Node 2
 * Return: Nothing
 */

void swap(listint_t **list, listint_t *node1, listint_t *node2)
{
	listint_t *n1 = node1->prev;
	listint_t *n2 = node2->next;

	if (node1->prev == NULL && node2->next == NULL)
	{
		node1->next = NULL;
		node2->prev = NULL;
		node1->prev = node2;
		node2->next = node1;
		*list = node2;
	}
	else if (node1->prev == NULL)
	{
		node1->next = n2;
		node2->prev = NULL;
		node1->prev = node2;
		node2->next = node1;
		n2->prev = node1;
		*list = node2;
	}
	else if (node2->next == NULL)
	{
		node1->prev = node2;
		node2->next = node1;
		node2->prev = n1;
		n1->next = node2;
		node1->next = NULL;
	}
	else
	{
		node1->prev = node2;
		node2->next = node1;
		node1->next = n2;
		node2->prev = n1;
		n1->next = node2;
		n2->prev = node1;
	}
}
