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
	listint_t *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = *head;
	*head = new;
	return (new);
	free(new);
}
