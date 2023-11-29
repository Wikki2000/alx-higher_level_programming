#include "lists.h"

listint_t *insert_node(listint_t **head, int number) {
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (!*head || number < (*head)->n) {
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	current = *head;
	prev = NULL;

	while (current && current->n < number) {
		prev = current;
		current = current->next;
	}

	new_node->next = current;
	prev->next = new_node;

	return new_node;
}
