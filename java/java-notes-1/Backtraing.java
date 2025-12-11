/*

//bascic array questiion for understanding

public class Backtraing {
    static void currArr(int arr[],int i, int val){
        //base
        if (i== arr.length){
            printarr(arr);
            return;
        }
        //recursion
        arr[i]=val;
        currArr(arr,i+1,val+1);
        arr[i] = arr[i]-1;  //backtracking is done in this line
    }

    static void printarr(int arr[]){
        for (int i=0;i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int arr[]=new int[5];
        currArr(arr,0,1);
        printarr(arr);

    }
}
*/

//find the subsets of the abc using the backtracking
/*
public class Backtraing {
    static void findSubstrings(String str, String ans, int i){
        //base
        if (i==str.length()){
            if (ans.length()==0){
                System.out.println("null");
            }
            else {
                System.out.println(ans);
            }
            return;
        }
        //backtraking
        //yes choice
        findSubstrings(str,ans+str.charAt(i) , i+1);
        //no
        findSubstrings(str , ans , i+1);
    }


    public static void main(String[] args) {
        String str = "abc";
        findSubstrings(str,"", 0);
    }
}*/

//N quens
/*
public class Backtraing {

    public static void nQueens(char board[][], int row){
            //base
        if (row==board.length){
            printBoard(board);
            return;
        }

        for (int j=0; j<board.length;j++){
        if (isSafe(board,row,j)) {
                board[row][j]='Q';
                nQueens(board,row+1); //puting in next row the Value Q
                board[row][j]='.'; //backtrACKING STEP
                //backtrack : so that only one Q shd be there in each Row
            }
        }

    }
    public static void printBoard(char board[][]){
        int nu=board.length;
        System.out.println("___________CHESS BOARD___________");
        for (int i=0; i<nu;i++){
            for (int j=0;j<nu;j++){
                System.out.print(board[i][j]+ " ");
            }
            System.out.println();
        }
    }

    static boolean isSafe(char board[][],int row,int col){
        //verical up
        for (int i=row-1;i>=0;i--){
            if (board[i][col]=='Q'){
                return false;
            }
        }
        //dia Left up
        for (int i=row-1,j=col-1;i>=0&&j>=0;i--,j--){
            if (board[i][j]=='Q'){
                return false;
            }
        }
        //dia right upwards
        for (int i=row-1,j=col+1;i>=0&&j<board.length;i--,j++){
            if (board[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int n=4;
        char board[][]=new char[n][n];
        //initialze
        for(int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                board[i][j]='.';
            }
        }
        nQueens(board,0);
    }
}
*/

//GRID WAYS
public class Backtraing {

    static int fact(int n){
        if (n==0){
            return 1;
        }
        return n*fact(n-1);
    }

    static int gridWays(int i,int j,int n,int m){
        if (i==n-1 && j==m-1){
            return 1;
        } else if (i==n||j==n){
            return 0;
        }
        int totalWays= (fact(n-1 + m-1))/(fact(n-1)*fact(m-1));    //trick formula for optimized code
        return totalWays;
    }

    public static void main(String[] args) {
        //System.out.println(fact(5));
        System.out.println(gridWays(0,0,3,3));
    }
}
