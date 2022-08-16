#ifndef TopologicalSorting_H
#define TopologicalSorting_H

#include<queue>
#include<list>
class Graph
{
private:
	int V;
	std::list<int> *adj;
	std::queue<int> q;
	int* indegree;

public:
	Graph(int V);
	~Graph();
	void addEdge(int v, int w);
	bool topological_sort();
};

#endif 
