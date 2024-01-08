#include "lists.h"

/**
*is_palindrome - to see if singly linked list is palindrome
*@head: pointer
*Return: 0 if not, 1 if palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *tmp = *head;
unsigned int size = 0, i = 0;
int data[10240];

if (head == NULL || *head == NULL) /* Non-existing or empty list is palindrome */
return (1);

while (tmp) /* Find size of linked list and pull node data into array */
{
data[i++] = tmp->n;
tmp = tmp->next;
size += 1;
}

for (i = 0; i <= (size / 2); i++)
{
if (data[i] != data[size - i - 1])
return (0);
}
return (1);
}
