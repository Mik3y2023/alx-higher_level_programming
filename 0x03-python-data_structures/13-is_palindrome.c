#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - function that checks if a linked list is a palindrome
 * @head: double pointer to linked list
 *
 * Return: 1 if it's a palindrome,
 *	0 if it's not
 */
int is_palindrome(listint_t **head)
{
	/* find the midpoint of the list*/
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *mid_node = *head;
	listint_t *dup = NULL;

	/* check if list is empty or has only element */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			dup = slow_ptr->next;
			break;
		}
		if (!fast_ptr->next)
		{
			dup = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}
	reverse_listint(&dup);

	while (dup && mid_node)
	{
		if (mid_node->n == dup->n)
		{
			dup = dup->next;
			mid_node = mid_node->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);
	return (0);
}

/**
 * reverse_listint - function that reverses a linked list
 * @head: pointer to the first node
 *
 * Return: pointer to first node in reversed list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev_node = NULL;
	listint_t *current_node = *head;
	listint_t *next_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}
	*head = prev_node;
}
