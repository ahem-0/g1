#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

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

int findParent(int i, vector<int>& parent) {
    if (parent[i] == i)
        return i;
    return parent[i] = findParent(parent[i], parent); 
}

void unionSets(int u, int v, vector<int>& parent) {
    int rootU = findParent(u, parent);
    int rootV = findParent(v, parent);
    if (rootU != rootV) {
        parent[rootU] = rootV;
    }
}

void kruskalMST(int V, vector<list<edge>>& adj) {
    vector<pair<int, pair<int, int>>> edges;
    for (int u = 0; u < V; u++) {
        for (edge& e : adj[u]) {
            edges.push_back({e.wt, {u, e.v}});
        }
    }

    sort(edges.begin(), edges.end());

    vector<int> parent(V);
    for (int i = 0; i < V; i++) parent[i] = i;

    int mstWeight = 0;
    cout << "Edges in MST:\n";

    for (auto& it : edges) {
        int wt = it.first;
        int u = it.second.first;
        int v = it.second.second;

        if (findParent(u, parent) != findParent(v, parent)) {
            unionSets(u, v, parent);
            mstWeight += wt;
            cout << u << " -- " << v << " (wt: " << wt << ")\n";
        }
    }

    cout << "Total MST Weight: " << mstWeight << "\n";
}

int main() {
    int V = 4;
    vector<list<edge>> adj(V);

    auto addEdge = [&](int u, int v, int wt) {
        adj[u].push_back(edge(v, wt));
        adj[v].push_back(edge(u, wt));
    };

    addEdge(0, 1, 10);
    addEdge(0, 2, 6);
    addEdge(0, 3, 5);
    addEdge(1, 3, 15);
    addEdge(2, 3, 4);

    kruskalMST(V, adj);
    return 0;
}