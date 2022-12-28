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
void create_matrix(matrix_t* matrix, int size);
matrix_t *process (matrix_t matrix, int Q);
void free_matrix(matrix_t* matrix);
void print_matrix(matrix_t* matrix);
void parallel_process(matrix_t* matrix, std::vector<matrix_t> results, int count_threads, int thread_index, int Q);
std::vector<matrix_t> multithreading(int count_threads, matrix_t* matrix, int Q);

#endif
