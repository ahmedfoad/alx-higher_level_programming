#include "lists.h"

/**
 * check_cycle - linked checker if the 
 * list contains a cycle
 * @list: linked list
 *
 * Return: 1 if the cycle is found, 0 if not found
 */
int check_cycle(listint_t *list)
{
	listint_t *first_ls = list;
	listint_t *sec_ls = list;

	if (!list)
		return (0);

	while (sec_ls->next)
	{
		if (!first_ls || !sec_ls)
			return (0);

		first_ls = first_ls->next;
		sec_ls = sec_ls->next->next;
		if (first_ls == sec_ls)
		{
			return (1);
		}
	}

	return (0);
}

