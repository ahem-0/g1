#include <iostream>
#include <vector>
#include <queue>
#include <pair>

using namespace std;

// Pair structure: {weight, destination_node}
typedef pair<int, int> pii;

void primMST(int V, vector<vector<pii>>& adj) {
    // Priority queue to store {edge_weight, vertex}
    // Min-heap ensures we always extract the smallest weight edge
    priority_queue<pii, vector<pii>, greater<pii>> pq;

    int src = 0; // Starting at vertex 0
    vector<int> key(V, 1e9);      // Minimum weight to connect vertex to MST
    vector<int> parent(V, -1);   // To store the resulting MST structure
    vector<bool> inMST(V, false); // To track vertices included in MST

    pq.push({0, src});
    key[src] = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (inMST[u]) continue;

        inMST[u] = true; // Include node in MST

        // Traverse all adjacent vertices of u
        for (auto& edge : adj[u]) {
            int v = edge.second;
            int weight = edge.first;

            // If v is not in MST and weight(u,v) is smaller than current key of v
            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                pq.push({key[v], v});
                parent[v] = u;
            }
        }
    }

    // Print the edges of the MST
    cout << "Edge \tWeight" << endl;
    for (int i = 1; i < V; ++i) {
        cout << parent[i] << " - " << i << " \t" << key[i] << endl;
    }
}

int main() {
    int V = 5;
    vector<vector<pii>> adj(V);

    // Graph edges: {weight, destination}
    adj[0].push_back({2, 1});
    adj[1].push_back({2, 0});

    adj[0].push_back({6, 3});
    adj[3].push_back({6, 0});

    adj[1].push_back({3, 2});
    adj[2].push_back({3, 1});

    adj[1].push_back({8, 5}); // Note: Adjust V if adding more nodes
    adj[1].push_back({5, 4});
    adj[4].push_back({5, 1});

    adj[2].push_back({7, 4});
    adj[4].push_back({7, 2});

    adj[3].push_back({9, 4});
    adj[4].push_back({9, 3});

    primMST(V, adj);

    return 0;
}
