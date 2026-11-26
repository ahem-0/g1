#include <iostream>
#include <vector>
#include <list>
#include <climits>

using namespace std;

class edge {
public:
    int v;
    int wt;

    edge(int v, int wt) {
        this->v = v;
        this->wt = wt;
    }
};

void bellmanFord(int V, vector<list<edge>>& adj, int src) {
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;

    for (int i = 0; i < V - 1; i++) {
        for (int u = 0; u < V; u++) {
            for (edge& e : adj[u]) {
                if (dist[u] != INT_MAX && dist[u] + e.wt < dist[e.v]) {
                    dist[e.v] = dist[u] + e.wt;
                }
            }
        }
    }
    for (int u = 0; u < V; u++) {
        for (edge& e : adj[u]) {
            if (dist[u] != INT_MAX && dist[u] + e.wt < dist[e.v]) {
                cout << "Graph contains a negative weight cycle\n";
                return;
            }
        }
    }
    for (int i = 0; i < V; i++) {
        cout << "Vertex " << i << " -> Distance: ";
        if (dist[i] == INT_MAX) cout << "INF\n";
        else cout << dist[i] << "\n";
    }
}
int main() {
    int V = 5;
    vector<list<edge>> adj(V);

    adj[0].push_back(edge(1, -1));
    adj[0].push_back(edge(2, 4));
    adj[1].push_back(edge(2, 3));
    adj[1].push_back(edge(3, 2));
    adj[1].push_back(edge(4, 2));
    adj[3].push_back(edge(2, 5));
    adj[3].push_back(edge(1, 1));
    adj[4].push_back(edge(3, -3));

    bellmanFord(V, adj, 0);
    return 0;
}
