fibonacci: main.c fibonacci.c headers/fibonacci.h
	gcc -Iheaders main.c fibonacci.c -o fibonacci

run: fibonacci
	./fibonacci

clean:
	rm -f fibonacci

.PHONY: run clean
