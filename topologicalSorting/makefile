topologicalSorting.out:topologicalSorting.o main.o
	g++ -o topologicalSorting.out topologicalSorting.o main.o
topologicalSorting.o:topologicalSorting.cc
	g++ -c topologicalSorting.cc
main.o:main.cc
	g++ -c main.cc
clean: 
	-rm *.o *.h.gch
do:
	./topologicalSorting.out
