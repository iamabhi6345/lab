#include<stdio.h>
#include<stdlib.h>
struct node{
    struct node *lchild;
    struct node *rchild;
    int val;
    int balFactor;
};
struct node *leftRotate(struct node *root);
int getHeight(struct node *root);
int max(int x, int y);
void printPreorder(struct node *root);
void printPorder(struct node *root);
struct node *rightRotate(struct node *root);
struct node *addNode(struct node *root, int data){

    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->val = data;
    newNode->lchild = NULL;
    newNode->rchild = NULL;
    newNode->balFactor = getHeight(root);
    return newNode;
}
struct node *insertNode(struct node *root, int data){
    if(root == NULL){
        root = addNode(root, data);
    }
    else if(data < root->val){
        root->lchild = insertNode(root->lchild, data);
    }
    else if(data > root->val){
        root->rchild = insertNode(root->rchild, data);
    }
    int bal = getHeight(root->lchild) - getHeight(root->rchild);
    if(bal > 1){
        int childBal = getHeight(root->lchild->lchild) - getHeight(root->lchild->rchild);
        if(childBal > 0){
            // Case for left left 
            printf("Left Left case: Performing RR rotation\n");
            root = rightRotate(root);
        }
        else if(childBal < 0){
            // Left right case
            printf("Right left case: Performing RL rotation\n");
            root->lchild = leftRotate(root->lchild);
            root = rightRotate(root);
        }
    }
    else if(bal < -1){
        int childBal = getHeight(root->rchild->lchild) - getHeight(root->rchild->rchild);
        if(childBal > 0){
            // Case for right left 
            printf("Left Right case: Performing LR rotation\n");
            root->rchild = rightRotate(root->rchild);
            root = leftRotate(root);
        }
        else if(childBal < 0){
            // right right case
            printf("Right Right case: Performing LL rotation\n");
            root = leftRotate(root);
        }
    }
    else{
        root->balFactor = getHeight(root);
    }
    return root;


}
struct node *leftRotate(struct node *root){
    struct node *newNode = root->rchild;
    struct node *temp = newNode->lchild;
    newNode->lchild = root;
    root->rchild = temp;
    root->balFactor = getHeight(root);
    newNode->balFactor = getHeight(newNode);
    return newNode;
    
}
struct node *rightRotate(struct node *root){
    struct node *newNode = root->lchild;
    struct node *temp = newNode->rchild;
    newNode->rchild = root;
    root->lchild = temp;
    root->balFactor = getHeight(root);
    newNode->balFactor = getHeight(newNode);
    return newNode;
}
int getHeight(struct node *root){
    if(root == NULL){
        return -1;
    }
    int left  = getHeight(root->lchild);
    int right = getHeight(root->rchild);
    return max(left,right)+1;
}
int max(int x, int y){
    return x>y?x:y;
}
void printInorder(struct node *root){
    if(root == NULL){
        return;
    }
    printInorder(root->lchild);
    printf("%d ", root->val);
    printInorder(root->rchild);
}
void printPostorder(struct node *root){
    if(root == NULL){
        return;
    }
    printPostorder(root->lchild);
    printPostorder(root->rchild);
    printf("%d ", root->val);
    
}
void printPreorder(struct node *root){
    if(root == NULL){
        return;
    }
    printf("%d ", root->val);
    printPreorder(root->lchild);
    printPreorder(root->rchild);
    
    
}

int main(){
    struct node *root = NULL;
    int choice;
    while(1){
        printf("-------------------------------\nEnter the choice\n1)Insert the node\n2)Print Inorder\n3)Print Preorder\n4)Print PostOrder\n5)Exit\n");
        int choice;
        scanf("%d", &choice);
        switch(choice){
            case 1:
            printf("Enter the data to be entered in the AVL tree\n");
            int data;
            scanf("%d", &data);
            root = insertNode(root, data);
            break;
            case 2:
            printInorder(root);
            printf("\n");
            break;
            case 3:
            printPreorder(root);
            printf("\n");
            break;
            case 4:
            printPostorder(root);
            printf("\n");
            break;
            case 5:
            exit(0);
        }
    }
    return 0;

}