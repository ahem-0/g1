#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<int>> Matrix;

// Add two matrices
Matrix add(Matrix A, Matrix B) {
    int n = A.size();
    Matrix C(n, vector<int>(n));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    return C;
}

// Subtract two matrices
Matrix sub(Matrix A, Matrix B) {
    int n = A.size();
    Matrix C(n, vector<int>(n));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
    return C;
}

Matrix strassen(Matrix A, Matrix B) {
    int n = A.size();

    // Base case
    if(n == 1) {
        return {{A[0][0] * B[0][0]}};
    }

    int half = n / 2;

    // Split A and B into 4 submatrices each
    Matrix A11(half, vector<int>(half)), A12(half, vector<int>(half)),
           A21(half, vector<int>(half)), A22(half, vector<int>(half));
    Matrix B11(half, vector<int>(half)), B12(half, vector<int>(half)),
           B21(half, vector<int>(half)), B22(half, vector<int>(half));

    for(int i = 0; i < half; i++) {
        for(int j = 0; j < half; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + half];
            A21[i][j] = A[i + half][j];
            A22[i][j] = A[i + half][j + half];

            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + half];
            B21[i][j] = B[i + half][j];
            B22[i][j] = B[i + half][j + half];
        }
    }

    // 7 Strassen products
    Matrix M1 = strassen(add(A11, A22), add(B11, B22));
    Matrix M2 = strassen(add(A21, A22), B11);
    Matrix M3 = strassen(A11, sub(B12, B22));
    Matrix M4 = strassen(A22, sub(B21, B11));
    Matrix M5 = strassen(add(A11, A12), B22);
    Matrix M6 = strassen(sub(A21, A11), add(B11, B12));
    Matrix M7 = strassen(sub(A12, A22), add(B21, B22));

    // Combine into result quadrants
    Matrix C11 = add(sub(add(M1, M4), M5), M7);
    Matrix C12 = add(M3, M5);
    Matrix C21 = add(M2, M4);
    Matrix C22 = add(sub(add(M1, M3), M2), M6);

    // Merge quadrants into result matrix
    Matrix C(n, vector<int>(n));
    for(int i = 0; i < half; i++) {
        for(int j = 0; j < half; j++) {
            C[i][j]               = C11[i][j];
            C[i][j + half]        = C12[i][j];
            C[i + half][j]        = C21[i][j];
            C[i + half][j + half] = C22[i][j];
        }
    }
    return C;
}

void printMatrix(Matrix A) {
    for(auto row : A) {
        for(auto val : row)
            cout << val << " ";
        cout << endl;
    }
}

int main() {
    // Matrix size must be a power of 2
    Matrix A = {{1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}};

    Matrix B = {{1, 0, 0, 1},
                {0, 1, 0, 0},
                {0, 0, 1, 0},
                {1, 0, 0, 1}};

    Matrix C = strassen(A, B);
    printMatrix(C);

    return 0;
}
