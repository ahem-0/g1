#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    vector<int> indexes; 
    ~TrieNode() {
        for (auto& pair : children) {
            delete pair.second;
        }
    }
};
class SuffixTrie {
private:
    TrieNode* root;
    void insertSuffix(const string& text, int startIndex) {
        TrieNode* curr = root;
        for (int i = startIndex; i < text.length(); i++) {
            char c = text[i];
            if (curr->children.find(c) == curr->children.end()) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
            curr->indexes.push_back(startIndex);
        }
    }
public:
    SuffixTrie(const string& text) {
        root = new TrieNode();
        for (int i = 0; i < text.length(); i++) {
            insertSuffix(text, i);
        }
    }
    ~SuffixTrie() {
        delete root;
    }
    vector<int> search(const string& pattern) {
        TrieNode* curr = root;
        for (char c : pattern) {
            if (curr->children.find(c) == curr->children.end()) {
                return {};
            }
            curr = curr->children[c];
        }
        return curr->indexes;
    }
};

int main() {
    string text = "banana";
    SuffixTrie st(text);
    vector<string> queries = {"ana", "nan", "ban", "apple"};
    for (const string& q : queries) {
        vector<int> matches = st.search(q);
        cout << "Pattern \"" << q << "\": ";
        if (matches.empty()) {
            cout << "Not found\n";
        } else {
            cout << "Found at index ";
            for (int idx : matches) {
                cout << idx << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}





