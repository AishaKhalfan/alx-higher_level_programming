#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* check_cycle- function to check if a singly linked list has a cycle in it.
* @list: pointer to head of list
* Return: 0 if no cycle,
* 1 if there is cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
		return (1);
		}
	}
	return (0);
}
