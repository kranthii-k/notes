/*
import java.util.Scanner;

public class m2d_arrays {

    public static boolean search(int matrix[][], int key){
        for (int i=0;i<matrix.length;i++){
            for (int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]==key){
                    System.out.println("element found at =  ( " + i + ","+ j + " )");
                }
            }
        } return false;
    }
    public static void main(String[] args) {

        int matrix[][]=new int[3][3];
        int n=matrix.length;      //rows length
        int m=matrix[0].length; //cols length
        Scanner sc=new Scanner(System.in);
        for (int i=0;i<n;i++){
            for (int j=0; j<m;j++){
                matrix[i][j]=sc.nextInt();
            }
        }
        //output
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        search(matrix,5);
    }
}
*/
/*

//spiral matrix
public class m2d_arrays {

    public static void printspiral(int matrix[][]){
        int startRow=0;
        int startCol=0;
        int endRow= matrix.length-1;
        int endCol= matrix[0].length-1;

        while (startRow<=endRow && startCol<=endCol){
            //top
            for (int j=startCol;j<=endCol;j++){
                System.out.print(matrix[startRow][j]+" ");
            }
            //right
            for (int i=startRow+1;i<=endRow;i++){
                System.out.print(matrix[i][endCol]+" ");
            }
            //bottom
            for (int j=endCol-1;j>=startCol;j--){
                if (startRow==endRow){
                    break;
                }
                System.out.print(matrix[endRow][j]+" ");
            }
            //left
            for (int i=endRow-1;i>=startRow+1;i--){
                if (startCol==endCol){
                    break;
                }
                System.out.print(matrix[i][startCol]+" ");
            }
            startRow++;
            startCol++;
            endCol--;
            endRow--;

        }




    }

    public static void main(String[] args) {
        int matrix[][]={{1,2,3,4},
                        {5,6,7,8},
                        {12,31,22,43}};
        printspiral(matrix);

    }
}*/

/*

//diagonal sum
public class m2d_arrays {

    public static int diagonalSum(int matrix[][]){
        int sum=0;
        for (int i=0;i< matrix.length;i++){
            //primary diagonal
            sum+=matrix[i][i];
            //sd
            if (i!= matrix.length-i-1){
                sum+=matrix[i][matrix.length-1-i];
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int matrix[][]={{1,2,3,4},
                        {5,6,7,8},
                        {9,10,11,12},
                        {13,14,15,16}};

        //diagonalSum(matrix);
        System.out.println(diagonalSum(matrix));
    }
}

*/
//search in sorted 2d array
public class m2d_arrays {

    public static boolean stairCase(int matrix[][],int key){
        int row=0,col=matrix[0].length-1;
        while (row < matrix.length && col >= 0){
            if (matrix[row][col]==key){
                System.out.println("key found at : ( " + row + " , " + col + " )");
                return true;
            }
            else if (matrix[row][col]>key){
                col--;
            }
            else {
                row++;
            }

        }
        System.out.println("key not found ");
        return false;
    }

    public static void main(String[] args) {
        int matrix[][] = {  {1, 2, 3, 4},
                            {5, 6, 7, 8},
                            {9, 10, 11, 12},
                            {13, 14, 15, 16}};
        int key=14;
        stairCase(matrix,key);
    }
}