#include "lists.h"
#include <stdio.h>
#include <stddef.h>
/**
 * insert_sorted - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Author: Ahmed Fouad
 * Description: Given a sorted singly-linked list,
 * 				this function inserts a new
 *              node with the given number in
 * 				the correct position such that
 *              the list remains sorted.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	for (node = *head; node->next && node->next->n < number; node = node->next)
		;

	new->next = node->next;
	node->next = new;

	return (new);
}
