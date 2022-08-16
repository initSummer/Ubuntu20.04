#include"topologicalSorting.h"
#include<iostream>

Graph::Graph(int V)
{
	this->V = V;
	adj = new std::list<int>[V];

	indegree = new int[V];
	for(int i = 0; i < V; i++)
	{
		indegree[i] = 0;
	}
}

Graph::~Graph()
{
	delete [] adj;
	delete [] indegree;
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	++indegree[w];
}

bool Graph::topological_sort()
{
	for(int i = 0; i < V; i++)
	{
		if(indegree[i] == 0)
		{
			q.push(i);
		}
	}	
	int count = 0;
	while(!q.empty())
	{
		int v = q.front();
		q.pop();

		std::cout<<v<<" ";
		count++;

		std::list<int>::iterator beg = adj[v].begin();
		for(; beg != adj[v].end(); beg++)
		{
			if(!(--indegree[*beg]))
			{
				q.push(*beg);
			}
		}
	}

	std::cout<<std::endl;

	if(count < V)
	{
		std::cout<<"ERROR"<<std::endl;
		return false;
	}
	else 
	{
		return true;
	}
}

