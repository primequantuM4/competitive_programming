class Solution {
    public int[][] transpose(int[][] matrix) {
     //to transpose just change i and j places
     //since size of matrix will change create a new array that has m n and n m
     int m = matrix.length;
     int n = matrix[0].length;
     int[][] res = new int[n][m];
     for (int i = 0; i < m; i++){
         for(int j = 0; j < n; j++){
             res[j][i] = matrix[i][j];
         }
     }
     return res;   
    }
}
