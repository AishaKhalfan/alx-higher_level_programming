#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* insert_node -inserts a number into a sorted singly linked list
* @head: pointer to head of list
* Return: address of new node
* or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	if(current == NULL)
		return (NULL);
	else
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = current->next;

		current->next = new;
	}
	return (new);
}
