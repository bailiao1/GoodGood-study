#include <stdlib.h>
#include <stdio.h>

typedef struct Node{
    int data;
    struct Node* next;
    struct Node* prev;
}Node;

typedef struct {
    Node* head;
    Node* tail;
} List;

Node* makenew(int v)
{
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode -> data = v;
    newnode -> next = NULL;
    newnode -> prev = NULL;
    return newnode;
}


List headcha(List list, int v)
{
    Node* new_node = makenew(v);

    if (list.head != NULL)
    {
        list.head->prev = new_node;
        new_node->next = list.head;
        new_node->prev = list.tail;
        list.head = new_node;
    }
    else
    {
        new_node->next = new_node;
        new_node->prev = new_node;
        list.head = list.tail = new_node;
    }

    return list;
}


void dayin(Node* head)
{
    if (head == NULL) return;
    Node* c;
    do {
        c = head;
        printf("%d <=> ", c->data);
        head = head -> next;
    } while (c != head);
    printf("(back to head)\n");
}


void shan(Node* head)
{
    if (head == NULL) return;

    Node* c;
    do {
        c = head;
        head = head -> next;
        free(c);
    } while (c != head);
    printf("(删光了)\n");
}


int main()
{
    List list = {NULL, NULL};  // 初始链表为空

    list = headcha(list, 10);
    list = headcha(list, 20);
    list = headcha(list, 30);

    dayin(list.head);  // 打印链表
    shan(list.head);   // 释放链表

    return 0;
}
