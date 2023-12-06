#include<stdio.h>
#include<stdlib.h>
int num;
struct node
{
    int data;
    struct node *link;
    struct node *prev_link;
};
struct node *add_prev(struct node *root, int num);
struct node *no_nodes(struct node *head)
{
    struct node *ptr = head;
    int data ,  i  ;
    printf("enter the numbers of nodes to be entered\n");
    scanf("%d"  , &num);
    for(i=0;i<num;i++)
    {   struct  node *temp  = (struct node *)malloc(sizeof(struct node));
    
        if(i==0)
        {   
            head = temp;
        }
           printf("enter the data to be entered\n");
           scanf("%d" , &temp->data);
        
            ptr->link=temp;
            ptr=ptr->link;
            
        }
         ptr->link=NULL;
         head = add_prev(head, num);
         return head;
    }
struct node *print1(struct node *head)
{
    struct node *ptr = head;
    if(ptr==NULL)
    {
        printf("the linked list is empty\n");
    }
    else
    {
        while(ptr!=NULL)
        {
            printf("%d\t" , ptr->data);
            ptr = ptr->link;
        }
        printf("\n");
    }
    return head;
}
struct node *print2(struct node *head)
{
    struct node *ptr = head;
    if(ptr==NULL)
    {
        printf("the linked list is empty\n");
    }
    else
    {
        while(ptr!=NULL)
        {
            printf("%d\t" , ptr->data);
            ptr = ptr->prev_link;
        }
        printf("\n");
    }
    return head;
}
struct node *add_node(struct node *head)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    printf("enter the data to be entered\n");
    scanf("%d" , &temp->data);
    temp->link=head;
    head=temp;
    head = add_prev(head, ++num);
    return head;
}
struct node *add_end(struct node *head)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    struct node *ptr = head;struct node *prev = head;
    printf("enter the data to be entered\n");
    scanf("%d" , &temp->data);
    while(ptr->link!=NULL)
    {
        prev = ptr;
        ptr = ptr->link;
    }
    prev->prev_link = temp;
    ptr->link = temp;
    temp->link = NULL;
    return head;
}
struct node *any_pos(struct node *head, int pos)
{
    struct node *temp =  (struct node *)malloc(sizeof(struct node));
    printf("enter the data value to be entered\n");
    scanf("%d" , &temp->data);
    struct node *ptr = head;
    int i ;
    if(pos == -2)
    {
        printf("Element not found\n");
        exit(0);
    }
    else if(pos==1)
    {
        temp->link = head;
        head = temp;
    }
    else
    {
        for(i=1;i<pos-1;i++)
    {
        ptr = ptr->link;
    }    temp->link = ptr->link;
    ptr->link = temp;
    
}
head = add_prev(head, ++num);
return head;
return head;
}

struct node *add_search(struct node *head, int search){
    struct node *ptr = head;

    int count = 1;
    struct node *prev = head;
    while(!(ptr->data == search)){
        prev = ptr;
        ptr = ptr->link;
        count++;
    }
    printf("%d", count);
    head = any_pos(head, count+1);
    return head;
}

struct node *add_prev(struct node *root, int num){
    struct node *ptr = root;
    while(ptr->link->link!=NULL){
        ptr->prev_link = ptr->link->link;
        ptr=ptr->link;

    }
    return root;
}
int main()
{
    struct node *head = (struct node *)malloc(sizeof(struct node));
    head =  no_nodes(head);
    printf("the linked list without any addition is \n");
    head = print1(head);
    print2(head);
    head = add_node(head);
    printf("the linked list with  addition at beginning is \n");
    head = print1(head);
    print2(head);
    head= add_end(head);
    printf("the linked list with addition at the end is \n");
    head = print1(head);
    print2(head);
    printf("Enter the element to be searched\n");
    int search;
    scanf("%d", &search);
    head = add_search(head, search);
    printf("the linked list with insertion after seraching %d is \n", search);
    head = print1(head);
    print2(head);

}