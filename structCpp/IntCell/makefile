IntCell.out:IntCell.o IntCellMain.o
	g++ -o IntCell.out IntCell.o IntCellMain.o
IntCellMain.o:IntCellMain.cc
	g++ -c IntCellMain.cc -std=c++11
IntCell.o:IntCell.cc
	g++ IntCell.cc -c -std=c++11
clean:
	rm test IntCell.o IntCellMain.o
