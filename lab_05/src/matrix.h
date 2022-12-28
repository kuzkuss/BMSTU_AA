#ifndef GRAPH_T_H
#define GRAPH_T_H

#include <iostream>
using namespace std;

#include <thread>
#include <chrono>
#include <vector>
#include <ctime>

typedef struct {
    int *AN;
    int *NR;
    int *NC;
    int *JR;
    int *JC;
    size_t size;
    size_t amount;
} matrix_t;

#define OK           0

#define MAX_NUM     10

void init_matrix(matrix_t* matrix);
void create_matrix(matrix_t* matrix);
void free_matrix(matrix_t* matrix);
void print_matrix(matrix_t* matrix, int num);
void delete_elements_from_matrix(matrix_t *matrix, int k);

#endif
