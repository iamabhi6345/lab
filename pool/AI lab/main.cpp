#include <bits/stdc++.h>
using namespace std;

/* Link list node */
class Node {
public:
    int data;
    Node *next;
};

/* Function to get the intersection point of two linked lists head1 and head2 */
Node *getIntesectionNode(Node *head1, Node *head2) {
    while (head2) {
        Node *temp = head1;
        while (temp) {
            // if both Nodes are same
            if (temp == head2)
                return head2;
            temp = temp->next;
        }
        head2 = head2->next;
    }
    // intersection is not present between the lists
    return NULL;
}

int main() {
    /*
        Create two linked lists

        A: 3->7->8->10
        B: 99->1->8->10

        Intersection Point: 8
    */

    Node *newNode;
    Node *head1 = new Node();
    head1->data = 3;
    newNode = new Node();
    newNode->data = 7;
    head1->next = newNode;
    newNode = new Node();
    newNode->data = 8;
    head1->next->next = newNode;
    newNode = new Node();
    newNode->data = 10;
    head1->next->next->next = newNode;
    head1->next->next->next->next = NULL;

    Node *head2 = new Node();
    head2->data = 99;
    newNode = new Node();
    newNode->data = 1;
    head2->next = newNode;
    newNode = new Node();
    newNode->data = 8;
    head2->next->next = newNode;
    newNode = new Node();
    newNode->data = 10;
    head2->next->next->next = newNode;
    Node *intersectionPoint = getIntesectionNode(head1, head2);

    if (!intersectionPoint)
        cout << "No Intersection Point\n";
    else
        cout << "Intersection Point: " << intersectionPoint->data << endl;

    return 0;
}
