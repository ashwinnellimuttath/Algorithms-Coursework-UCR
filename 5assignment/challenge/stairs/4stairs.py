import heapq

class Cell:
    def __init__(self, row, time):
        self.row = row
        self.time = time

class Compare:
    def __call__(self, c1, c2):
        return c1.time > c2.time

def find_minimal_time(matrix, r, dest):
    adjacency = [[] for _ in range(r)]
    for row in matrix:
        adjacency[row[0]].append((row[1], row[2]))
        adjacency[row[1]].append((row[0], row[2]))
        adjacency[row[2]].append((row[0], row[1]))

    visited = [False] * r
    pq = []
    heapq.heappush(pq, Cell(0, 0))

    while pq:
        curr = heapq.heappop(pq)
        if visited[curr.row]:
            continue
        visited[curr.row] = True
        timer = curr.time
        if curr.row == dest:
            return timer
        first = 0
        second = 0
        if timer % 2 == 0:
            first = 2
            second = 1
        else:
            first = 1
            second = 2
        for platform, time in adjacency[curr.row]:
            if visited[platform]:
                continue
            heapq.heappush(pq, Cell(platform, timer + (first if time == 0 else second)))

    return -1

def main():
    r, c, dest = map(int, input().split())
    matrix = []
    for _ in range(c):
        matrix.append(list(map(int, input().split())))
    print(find_minimal_time(matrix, r, dest))

if __name__ == "__main__":
    main()


#include <iostream>
#include <vector>
#include <queue>
using namespace std;
struct Cell {
    int row;
    int time;
 
    Cell(int r, int t) : row(r), time(t) {}
};
struct Compare {
    bool operator()(const Cell& c1, const Cell& c2) {
        return c1.time > c2.time;
    }
};
int find_minimal_time(vector<vector<int>> matrix,int r, int dest)
{
    // int r = matrix.size();
    // cout<<"Hello";
    
    vector<int> adjacency[r][2];
    for(int i=0;i<matrix.size();i++)
    {
        
            adjacency[matrix[i][0]][0].push_back(matrix[i][1]);// For source at 0 no issues with odd even
            adjacency[matrix[i][0]][1].push_back(matrix[i][2]);
            
            adjacency[matrix[i][1]][1].push_back(matrix[i][0]);// But if getting on from destination, odd even switched
            adjacency[matrix[i][2]][0].push_back(matrix[i][0]);
            
            adjacency[matrix[i][1]][1].push_back(matrix[i][2]);// But if getting on from destination, odd even switched
            adjacency[matrix[i][2]][0].push_back(matrix[i][1]);
            
            

    }
    vector<bool> visited(r,false);
    priority_queue<Cell, vector<Cell>,Compare> pq;
    pq.push(Cell(0,0));
    while(!pq.empty())
    {
        Cell curr = pq.top();
        pq.pop();
        if(visited[curr.row])
        continue;
        visited[curr.row] = true;
        // cout<<curr.row<<curr.time<<"\n";
        int timer = curr.time;
        if(curr.row==dest)
        return timer;
        int first=0,second=0;
        if(timer%2==0)
        {
            first=2;
            second=1;
        }
        else
        {
            first=1;
            second=2;
        }
        for(auto platform : adjacency[curr.row][0])
        {
            if(visited[platform])
            continue;
            pq.push(Cell(platform,timer+first));
        }
         for(auto platform : adjacency[curr.row][1])
        {
            if(visited[platform])
            continue;
            pq.push(Cell(platform,timer+second));
        }
        
        
    }
    return -1;
    
}

int main()
{
    int r,c,dest;
    vector<vector<int>> matrix;
    cin>>r>>c>>dest;
   
    matrix.resize(c,vector<int>(3));
    
    for(int i=0;i<c;i++)
    {
        for(int j=0;j<3;j++)
        {
            cin>>matrix[i][j];
        }
    }
 
    // for(int i=0;i<c;i++)
    // {
    //     for(int j=0;j<3;j++)
    //     {
    //         cout<<matrix[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }
    // cout<<"Hello";
    
    cout<<"\n"<<find_minimal_time(matrix,r,dest);
    
 
return 0;
}