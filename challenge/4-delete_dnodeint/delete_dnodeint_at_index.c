#include "lists.h"

/**
 * delete_dnodeint_at_index - Supprime un nœud à un index spécifique dans une liste doublement chaînée
 *
 * @head: Un pointeur vers l'adresse du premier élément de la liste
 * @index: L'index du nœud à supprimer
 *
 * Return: 1 en cas de succès, -1 en cas d'échec
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current = *head;
    unsigned int i;


    if (*head == NULL)
    {
        return (-1);
    }


    for (i = 0; current != NULL && i < index; i++)
    {
        current = current->next;
    }


    if (current == NULL)
    {
        return (-1);
    }


    if (current->prev == NULL)
    {
        *head = current->next;
        if (*head != NULL)
        {
            (*head)->prev = NULL;
        }
    }
    else
    {

        current->prev->next = current->next;


        if (current->next != NULL)
        {
            current->next->prev = current->prev;
        }
    }


    free(current);
    return (1);
}
