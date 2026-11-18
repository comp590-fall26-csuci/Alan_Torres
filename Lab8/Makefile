fibonacci: main.c fibonacci.c headers/fibonacci.h
	gcc -Iheaders main.c fibonacci.c -o fibonacci

fibonacci_tests: test_fibonacci.c fibonacci.c headers/fibonacci.h headers/utest.h
	gcc -Iheaders test_fibonacci.c fibonacci.c -o fibonacci_tests

run: fibonacci
	./fibonacci

test: fibonacci_tests
	./fibonacci_tests

clean:
	rm -f fibonacci fibonacci_tests

.PHONY: run test clean
