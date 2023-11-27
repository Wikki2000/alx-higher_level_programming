#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle using Floyd's algorithm.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is detected, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;

        /* If there is a cycle, the pointers will meet */
        if (slow == fast)
            return 1;  /* Cycle detected */
    }

    return (0);  /* No cycle detected */
}
