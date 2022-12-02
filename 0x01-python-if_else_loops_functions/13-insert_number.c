#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* insert_node -inserts a number into a sorted singly linked list
* @head: pointer to head of list
* @number: number to be inserted into a sorted linked list
* Return: address of new node
* or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *old;

	current = *head;

	if (current == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	old = NULL;

	for (; current != NULL && current->n < number;)
	{
		old = current;
		current = current->next;
	}

	new->next = current;

	if (old != NULL)
		old->next = new;
	else
		current->next = new;

	return (new);
}
