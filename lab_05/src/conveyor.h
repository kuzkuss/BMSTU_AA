#ifndef CONVEYOR_H
#define CONVEYOR_H

#include <iostream>
#include <string>
#include <queue>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono>
#include <stdio.h>

#include "matrix.h"

#define IN_SEC        1e9
#define COUNT_THREADS 3

void linear_mode(int size, int n);
void parallel_mode(int size, int n);

#endif
