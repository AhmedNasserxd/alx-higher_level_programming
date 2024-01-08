#include <stdlib.h>
#include "lists.h"

/**
*is_palindrome - checks if a singly linked list is a palindrome
*@head: double pointer to the head of the linked list
*Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev_slow = NULL;
listint_t *second_half, *mid_node;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;

// Reverse the first half of the list
listint_t *temp = slow;
slow = slow->next;
temp->next = prev_slow;
prev_slow = temp;
}

// If the number of elements is odd, move to the next node
if (fast != NULL)
slow = slow->next;

second_half = slow;
mid_node = prev_slow;

// Compare the first and second halves
while (second_half != NULL)
{
if (mid_node->n != second_half->n)
{
is_palindrome = 0;
break;
}
mid_node = mid_node->next;
second_half = second_half->next;
}

// Restore the original list
while (prev_slow != NULL)
{
listint_t *temp = prev_slow->next;
prev_slow->next = *head;
*head = prev_slow;
prev_slow = temp;
}

return (is_palindrome);
}
