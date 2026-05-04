#include<iostream>
#include <vector>
#include <climits>
#include <list>
#include <queue>
using namespace std;

class graph{
    int V;
    list <int> *l;

public:
    graph(int V){
        this-> V = V;
        l = new list<int>[V];
    }
    void addEdge(int u, int v){
        l[u].push_back(v);
        l[v].push_back(u);
        
    }
    void printAdjlist(){
        for (int i = 0; i<V;i++){
            cout << i << ":";
            for (int neigh : l[i]){
                cout << neigh << " ";
            }
            cout << endl;
        }
    }
    void bfs(){
        queue<int> q;
        vector<bool> vis(V);

        q.push(0);
        vis[0] = true;

        while (q.size()>0){
            int u = q.front();
            q.pop();
            cout << u << " ";

            for (int v : l[u]){
                if (!vis[v]){
                    vis[v] = true;
                    q.push(v);
                }
            }
        }
        cout << endl;
    }
    void dfsH(int u, vector<bool>& vis){
        cout << u <<" ";
        vis[u]= true;
        for (int v : l[u]){
            if (!vis[v]){
                dfsH(v,vis);
                
            }
        }
    }
    void dfs(){
        int src = 0;
        vector<bool> vis (V,false);
        dfsH(src,vis);
        cout << endl;
    }
};
int main(){
    graph g(5);
    
    g.addEdge(0,1);
    g.addEdge(1,2);
    g.addEdge(1,3);
//  g.addEdge(2,3);
    g.addEdge(2,4);

   // g.printAdjlist();
    g.bfs();
    g.dfs();
    return 0;
    
}