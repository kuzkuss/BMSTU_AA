#ifndef TIME_TEST_H
#define TIME_TEST_H

#include <fstream>
#include "conveyor.h"

#define TYPE_MSG "Тип обработки:\n" \
                 "1. последовательный\n" \
                 "2. параллельный\n" \
                 "Выбор: "

#define LINEAR    1
#define PARALLEL  2

#define NAME_MULTI        "time_multi.csv"
#define NAME_SINGLE       "time_single.csv"

#define ITERS  100

void test_n();

#endif
