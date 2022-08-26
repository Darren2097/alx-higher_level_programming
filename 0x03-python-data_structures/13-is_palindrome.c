#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *rev_list, *node, *next, *prev;

	if (head == NULL)
		return (1);

	rev_list = malloc(sizeof(listint_t));

	node = *head;
	prev = NULL;
	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	node = prev;
	rev_list = node;

	if (*head == rev_list)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
