#include "binary_trees.h"

/**
 * heap_extract - extracts the root node of a Max Binary Heap
 * @root: pointer to root
 * Return: value of extracted node
 **/
int heap_extract(heap_t **root)
{
	int value, value_temp;
	heap_t *temp;

	if (!root || !*root)
		return (0);
	temp = *root;
	value = temp->n;
	if (!temp->left && !temp->right && !temp->parent)
	{
		free(temp);
		return (value);
	}
	while (temp->left || temp->right)
	{
		if (temp->left && temp->right)
		{
			if (!temp->right || temp->left->n > temp->right->n)
			{
				value_temp = temp->n;
				temp->n = temp->left->n;
				temp->left->n = value_temp;
				temp = temp->left;
			}
			else if (temp->left->n < temp->right->n)
			{
				value_temp = temp->n;
				temp->n = temp->right->n;
				temp->right->n = value_temp;
				temp = temp->right;

			}
		}
	}
	return (value);
}