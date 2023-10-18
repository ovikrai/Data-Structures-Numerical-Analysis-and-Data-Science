compile:
	g++ -Wall -c main.cpp
	mv ./*.o ./objects

link:
	g++ -Wall -o ./build/main ./objects/*.o

clean:
	rm -r ./build/main ./objects/*.o

run:
	./build/main

build: compile link run


run-py:
	python3 main.py
