CC := g++
FLAGS := -pthread
TARGET := app.exe


.PHONY: run clean

$(TARGET) : main.cpp matrix.cpp conveyor.cpp time_test.cpp
	$(CC) $(FLAGS) -o $@ $^

clean:
	$(RM) -rf *.exe
run:
	./app.exe

