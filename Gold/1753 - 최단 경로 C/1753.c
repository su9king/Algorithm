#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_NODES 20005
#define INITIAL_CAPACITY 4

typedef struct {
    int node;   // 연결된 노드
    int weight; // 가중치
} Edge;

typedef struct {
    Edge* edges;    // 간선 배열 (동적)
    int size;       // 현재 저장된 간선 수
    int capacity;   // 배열 크기
} Node;

Node graph[MAX_NODES]; // 그래프 (인접 리스트)
int distances[MAX_NODES]; // 최단 거리 저장
int visited[MAX_NODES];   // 방문 여부

// 우선순위 큐용 구조체
typedef struct {
    int node;
    int cost;
} QueueNode;

typedef struct {
    QueueNode* heap;
    int size;
    int capacity;
} PriorityQueue;

// 노드 초기화
void initNode(Node* node) {
    node->edges = (Edge*)malloc(sizeof(Edge) * INITIAL_CAPACITY);
    node->size = 0;
    node->capacity = INITIAL_CAPACITY;
}

// 간선 추가
void addEdge(Node* node, int to, int weight) {
    if (node->size >= node->capacity) {
        node->capacity *= 2;
        node->edges = (Edge*)realloc(node->edges, sizeof(Edge) * node->capacity);
    }
    node->edges[node->size].node = to;
    node->edges[node->size].weight = weight;
    node->size++;
}

// 우선순위 큐 초기화
PriorityQueue* createPriorityQueue(int capacity) {
    PriorityQueue* pq = (PriorityQueue*)malloc(sizeof(PriorityQueue));
    pq->heap = (QueueNode*)malloc(sizeof(QueueNode) * capacity);
    pq->size = 0;
    pq->capacity = capacity;
    return pq;
}

// 우선순위 큐 삽입
void push(PriorityQueue* pq, int node, int cost) {
    if (pq->size >= pq->capacity) {
        pq->capacity *= 2;
        pq->heap = (QueueNode*)realloc(pq->heap, sizeof(QueueNode) * pq->capacity);
    }
    int i = pq->size++;
    while (i > 0 && pq->heap[(i - 1) / 2].cost > cost) {
        pq->heap[i] = pq->heap[(i - 1) / 2];
        i = (i - 1) / 2;
    }
    pq->heap[i].node = node;
    pq->heap[i].cost = cost;
}

// 우선순위 큐 pop
QueueNode pop(PriorityQueue* pq) {
    QueueNode root = pq->heap[0];
    QueueNode last = pq->heap[--pq->size];
    int i = 0;
    while (2 * i + 1 < pq->size) {
        int left = 2 * i + 1, right = 2 * i + 2, min = left;
        if (right < pq->size && pq->heap[right].cost < pq->heap[left].cost) {
            min = right;
        }
        if (last.cost <= pq->heap[min].cost) break;
        pq->heap[i] = pq->heap[min];
        i = min;
    }
    pq->heap[i] = last;
    return root;
}

// 다익스트라 알고리즘
void dijkstra(int start, int numNodes) {
    PriorityQueue* pq = createPriorityQueue(numNodes);
    push(pq, start, 0);
    distances[start] = 0;

    while (pq->size > 0) {
        QueueNode current = pop(pq);
        int curNode = current.node;
        int curCost = current.cost;

        if (visited[curNode]) continue;
        visited[curNode] = 1;

        for (int i = 0; i < graph[curNode].size; i++) {
            Edge edge = graph[curNode].edges[i];
            int nextNode = edge.node;
            int weight = edge.weight;

            if (distances[nextNode] > curCost + weight) {
                distances[nextNode] = curCost + weight;
                push(pq, nextNode, distances[nextNode]);
            }
        }
    }

    free(pq->heap);
    free(pq);
}

// 메모리 해제
void freeGraph(int numNodes) {
    for (int i = 0; i <= numNodes; i++) {
        free(graph[i].edges);
    }
}

// 메인 함수
int main() {
    int V, E, start;
    scanf("%d %d %d", &V, &E, &start);

    // 그래프 초기화
    for (int i = 1; i <= V; i++) {
        initNode(&graph[i]);
        distances[i] = INT_MAX;
        visited[i] = 0;
    }

    // 간선 입력
    for (int i = 0; i < E; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        addEdge(&graph[u], v, w);
    }

    // 다익스트라 실행
    dijkstra(start, V);

    // 결과 출력
    for (int i = 1; i <= V; i++) {
        if (distances[i] == INT_MAX) {
            printf("INF\n");
        } else {
            printf("%d\n", distances[i]);
        }
    }

    // 메모리 해제
    freeGraph(V);
    return 0;
}
