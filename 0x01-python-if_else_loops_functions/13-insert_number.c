#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted singly linked
 * list
 * @head: pointer to pointer address of head node
 * @number: number to be inserted into list
 *
 * Return - Singly lnked list with new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *inserted_node;
	listint_t *temp;

	/* Temp is node for traversal */
	temp = *head;
	inserted_node = (listint_t *)malloc(sizeof(listint_t));
	if (inserted_node == NULL)
	{
		return (NULL);
	}
	inserted_node->n = n;
	inserted_node->next = NULL;
	if (temp == NULL)
	{
		*head = inserted_node;
	}
	/* When untrue make the nemp->next into inserted_node */
	while (temp->next != NULL)
	{
		/* Traverse to the penultimate node */
		temp = temp->next;
	}
	temp->next = inserted_node;
	return (inserted_node);
	free(inserted_node);
}
