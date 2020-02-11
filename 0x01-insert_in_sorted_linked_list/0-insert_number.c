#include "lists.h"


/**
 * *insert_node - Insert node in a linked list
 * @head: pointer to head of list
 * @number: number to insert in the node
 * Return: number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	current = *head;

	new = malloc(sizeof(listint_t));
	if (new)
	{
		while(current->next)
		{
			if (current->n < number)
					    current = current->next;
			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				new->n = number;
				return *head;
			}
		}
	}
	return (NULL);
}
