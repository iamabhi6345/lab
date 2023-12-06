#include <stdio.h>
#include <stdlib.h>

// Red-Black Tree Node Structure
struct Node {
    int key;
    char color; // 'R' for red, 'B' for black
    struct Node* parent;
    struct Node* left;
    struct Node* right;
};

// Initialize a new Red-Black Tree node
struct Node* createNode(int key) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->color = 'R'; // Newly inserted nodes are always red
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->parent = NULL;
    return newNode;
}

// Function to perform left rotation
void leftRotate(struct Node** root, struct Node* x) {
    struct Node* y = x->right;
    x->right = y->left;
    if (y->left != NULL)
        y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL)
        *root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;
    y->left = x;
    x->parent = y;
}

// Function to perform right rotation
void rightRotate(struct Node** root, struct Node* y) {
    struct Node* x = y->left;
    y->left = x->right;
    if (x->right != NULL)
        x->right->parent = y;
    x->parent = y->parent;
    if (y->parent == NULL)
        *root = x;
    else if (y == y->parent->left)
        y->parent->left = x;
    else
        y->parent->right = x;
    x->right = y;
    y->parent = x;
}

// Function to fix violations of Red-Black Tree properties after insertion
void insertFixup(struct Node** root, struct Node* z) {
    while (z->parent != NULL && z->parent->color == 'R') {
        if (z->parent == z->parent->parent->left) {
            struct Node* y = z->parent->parent->right;
            if (y != NULL && y->color == 'R') {
                z->parent->color = 'B';
                y->color = 'B';
                z->parent->parent->color = 'R';
                z = z->parent->parent;
            } else {
                if (z == z->parent->right) {
                    z = z->parent;
                    leftRotate(root, z);
                }
                z->parent->color = 'B';
                z->parent->parent->color = 'R';
                rightRotate(root, z->parent->parent);
            }
        } else {
            // Symmetric case
            struct Node* y = z->parent->parent->left;
            if (y != NULL && y->color == 'R') {
                z->parent->color = 'B';
                y->color = 'B';
                z->parent->parent->color = 'R';
                z = z->parent->parent;
            } else {
                if (z == z->parent->left) {
                    z = z->parent;
                    rightRotate(root, z);
                }
                z->parent->color = 'B';
                z->parent->parent->color = 'R';
                leftRotate(root, z->parent->parent);
            }
        }
    }
    (*root)->color = 'B'; // Root should always be black
}

// Function to insert a key into the Red-Black Tree
void rbInsert(struct Node** root, int key) {
    struct Node* z = createNode(key);
    struct Node* y = NULL;
    struct Node* x = *root;

    while (x != NULL) {
        y = x;
        if (z->key < x->key)
            x = x->left;
        else
            x = x->right;
    }

    z->parent = y;
    if (y == NULL)
        *root = z;
    else if (z->key < y->key)
        y->left = z;
    else
        y->right = z;

    insertFixup(root, z);
}

// Inorder traversal to print Red-Black Tree
void inorderTraversal(struct Node* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("Key: %d, Color: %c\n", root->key, root->color);
        inorderTraversal(root->right);
    }
}

// Main function to test Red-Black Tree with user input
int main() {
    struct Node* root = NULL;
    int key;

    printf("Enter keys to insert into the Red-Black Tree (enter -111 to exit):\n");
    while (1) {
        printf("Enter key: ");
        scanf("%d", &key);
        if (key == -111)
            break;
        rbInsert(&root, key);
        printf("Inorder Traversal:\n");
    inorderTraversal(root);
    }

    

    return 0;
}
