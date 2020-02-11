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
		new->n = number;
		new->next = NULL;
		if (*head == NULL || (*head)->n >= new->n)
		{
			new->next = *head;
			*head = new;
		}
		while(current->next && current->next->n < new->n)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
		return new;
	}
	return (NULL);
}
