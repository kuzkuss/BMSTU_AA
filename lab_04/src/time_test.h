#ifndef TIME_TEST_H
#define TIME_TEST_H

#include <fstream>
#include <string>

#include "matrix.h"
#include "constants.h"

#define ITERS  100
#define IN_SEC 1e9

#define NAME_MULTI        "time_multi.csv"
#define NAME_SINGLE       "time_single.csv"

#define FILE_MULTI        1
#define FILE_SINGLE       2

#define FILE_MSG "Выберите файл для записи:\n" \
                 "1. time_multi.csv\n" \
                 "2. time_single.csv\n" \
                 "Выбор: "

void measure_time(int size);
void write_in_file(int size, int count_threads, double time_result, int choice);
void test_count_threads();
#endif