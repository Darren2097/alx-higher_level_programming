#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *once, *twice;

	once = list;
	twice = list;

	while ((once != NULL) && (twice != NULL))
	{
		if (once->next == NULL)
			return (0);

		once = once->next;
		twice = twice->next->next;
		if (once == twice)
			return (1);
	}

	return (0);
}
