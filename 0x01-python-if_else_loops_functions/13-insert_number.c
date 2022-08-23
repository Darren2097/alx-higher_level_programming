#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of list
 * @number: number to be added
 *
 * Return: address of new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new = *head;

	while (*head != NULL)
	{
		if ((*head)->n >= number)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			node = *head;
			while (node->next != NULL && (node->next->n < number))
			{
				node = node->next;
			}
			new->next = node->next;
			node->next = new;
		}
	}

	return (new);
	free(new);
}
