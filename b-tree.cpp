#include <iostream>
#include <vector>
using namespace std;
class BTreeNode {
public:
    vector<int> keys;
    vector<BTreeNode*> children;
    int t;      
    bool leaf;  
    BTreeNode(int min_degree, bool is_leaf) : t(min_degree), leaf(is_leaf) {}
    ~BTreeNode() {
        for (BTreeNode* child : children) {
            delete child;
        }
    }
    void traverse() const {
        size_t i = 0;
        for (; i < keys.size(); ++i) {
            if (!leaf) {
                children[i]->traverse();
            }
            std::cout << keys[i] << " ";
        }
        if (!leaf) {
            children[i]->traverse();
        }
    }
    bool search(int k) const {
        size_t i = 0;
        while (i < keys.size() && k > keys[i]) {
            ++i;
        }
        if (i < keys.size() && keys[i] == k) {
            return true;
        }
        if (leaf) {
            return false;
        }
        return children[i]->search(k);
    }
    void splitChild(int i, BTreeNode* y) {
        BTreeNode* z = new BTreeNode(y->t, y->leaf);
        for (int j = 0; j < t - 1; ++j) {
            z->keys.push_back(y->keys[j + t]);
        }
        if (!y->leaf) {
            for (int j = 0; j < t; ++j) {
                z->children.push_back(y->children[j + t]);
            }
            y->children.resize(t);
        }

        int median = y->keys[t - 1];
        y->keys.resize(t - 1);

        keys.insert(keys.begin() + i, median);
        children.insert(children.begin() + i + 1, z);
    }
    void insertNonFull(int k) {
        int i = static_cast<int>(keys.size()) - 1;

        if (leaf) {
            while (i >= 0 && keys[i] > k) {
                --i;
            }
            keys.insert(keys.begin() + i + 1, k);
        } else {
            while (i >= 0 && keys[i] > k) {
                --i;
            }
            ++i;

            if (static_cast<int>(children[i]->keys.size()) == 2 * t - 1) {
                splitChild(i, children[i]);
                if (keys[i] < k) {
                    ++i;
                }
            }
            children[i]->insertNonFull(k);
        }
    }
};

class BTree {
private:
    BTreeNode* root = nullptr;
    int t;

public:
    explicit BTree(int min_degree) : t(min_degree) {}
    ~BTree() {
        delete root;
    }
    void traverse() const {
        if (root != nullptr) {
            root->traverse();
        }
        cout << "\n";
    }
    bool search(int k) const {
        return (root == nullptr) ? false : root->search(k);
    }
    void insert(int k) {
        if (root == nullptr) {
            root = new BTreeNode(t, true);
            root->keys.push_back(k);
            return;
        }
        if (static_cast<int>(root->keys.size()) == 2 * t - 1) {
            BTreeNode* new_root = new BTreeNode(t, false);
            new_root->children.push_back(root);
            new_root->splitChild(0, root);

            int i = (new_root->keys[0] < k) ? 1 : 0;
            new_root->children[i]->insertNonFull(k);
            root = new_root;
        } else {
            root->insertNonFull(k);
        }
    }
};
int main() {
    BTree tree(3);  
    for (int val : {10, 20, 5, 6, 12, 30, 7, 17}) {
        tree.insert(val);
    }
    cout << "Sorted traversal: ";
    tree.traverse();  
    cout << "Search 6:  " << (tree.search(6) ? "Found" : "Not Found") << "\n";
    cout << "Search 15: " << (tree.search(15) ? "Found" : "Not Found") << "\n";
}


