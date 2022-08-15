#include<iostream>
#include<string>

template<typename T>
class SqList
{
public:
	SqList(){}
	SqList(int size)
	{
		m_size = size;
		elems = new T[size];
		m_length = 0;
	}
	int length()
	{
		return m_length;
	}
	int size()
	{
		return m_size;
	}
	void PushBack(T x)
	{
		if(m_length != m_size)
		{
			elems[m_length] = x;
			m_length++;
		}
	}
	T& operator [](int x)
	{
		if(x >= m_length)
		{
			throw -1;
		}
		else
		{
			return elems[x];
		}
	}
	void Insert(int num, T x)
	{
		if(num >= m_length)
		{
			throw -1;
		}
		else 
		{
			m_length++;
			for(int i = m_length - 1; i > num; i--)
			{
				elems[i] = elems[i - 1];
			}
			elems[num] = x;
		}
	}
	void Delete(int x)
	{
		if(m_length == x)
		{
			m_length--;
		}
		else 
		{
			for(int i = x; i < m_length - 1; i++)
			{
				elems[i] = elems [i+1];
			}
			m_length--;
		}
	}
	void destroyList()
	{
		delete[]elems;
		m_length = 0;
		m_size = 0;
	}
	~SqList()
	{
		delete[]elems;
	}
private:
	T *elems;
	int m_length;
	int m_size;
};

int main()
{
	SqList<std::string> s(20);
	s.PushBack("x");
	s.PushBack("y");
	s.PushBack("z");
	std::cout<<s.length()<<" "<<s[0]<<" "<<s.size()<<std::endl;
	s.Insert(1,"a");
	std::cout<<s[0]<<" "<<s[1]<<" "<<s[2]<<" "<<s[3]<<std::endl;
	s.Delete(1);
	for(int i = 0; i < s.length(); i++)
	{
		std::cout<<s[i]<<" ";
	}
	std::cout<<std::endl;
	return 0;
}

