/*
import java.util.Scanner;

public class patadv {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number of rows to print halllow rectangle : ");
        int totrows= sc.nextInt();

        Scanner sec=new Scanner(System.in);
        System.out.println("enter the number of columns to print halllow rectangle : ");
        int totcols= sec.nextInt();

        for(int i=1;i<=totrows;i++){
            for (int j=1;j<=totcols; j++){

                if (i==1 || j==1 || i==totrows || j==totcols){
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }

            }System.out.println();

        }
    }
}
*/

public class patadv {

    public static void holloRec(int totrows,int totcols){
        for(int i=1;i<=totrows;i++){
            for (int j=1;j<=totcols; j++){

                if (i==1 || j==1 || i==totrows || j==totcols){
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }

            }System.out.println();
    }
}


    public static void half_py_w_nums(int n){
        //outer loop for number of lines
        for (int i=1;i<=n;i++){
            //inner-loop for number printing
            for (int j=1; j<=n-i+1;j++){
                System.out.print(j);
            }System.out.println();
        }

    }

    public static void floyds_triangle(int n){
        int counter=1;
        //lines
        for (int i=1; i<=n;i++){
            //inner-to print counter how many times
            for (int j=1;j<=i;j++){
                //printing counter
                System.out.print(counter+" ");
                //incrimenting counter
                counter++;

            }
            //next line after printing each line of tri
            System.out.println();
        }
    }
    public static void o_1triagle(int n){
        for (int i=1;i<=n;i++){
            for (int j=1; j<=i;j++){
                if((i+j)%2==0){
                    System.out.print("1 ");
                }  else {
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
    }

    public static void butterfly(int n){

        for (int i=1;i<=n;i++){
            for (int j=1;j<=i;j++ ) {
                System.out.print("*");
            }
            for (int j=1; j<=2*(n-i);j++){
                System.out.print(" ");
                }
            for (int j=1;j<=i;j++ ) {
                System.out.print("*");
            } System.out.println();
        }

        for (int i=n; i>=1;i--){
            for (int j=1;j<=i;j++) {
                System.out.print("*");
            }
            for (int j=1; j<=2*(n-i);j++){
                System.out.print(" ");
            }
            for (int j=1;j<=i;j++) {
                System.out.print("*");
            } System.out.println();
        }

    }

    public static void palnum(int n){

        for (int i=1;i<=n;i++){
            //space
            for (int j=1; j<=n-i; j++){
                System.out.print(" ");
            }

            //num
            for (int j=i;j>=1;j--){
                System.out.print(j);
            }
            //dec
            for (int j=2; j<=i ; j++){
                System.out.print(j);
            }
            System.out.println();
            //asc

        }



    }

    public static void main(String[] args) {
        //holloRec(4,5);
        //floyds_triangle(5);
        //half_py_w_nums(5);
        //o_1triagle(5);
        //butterfly(20);
        //palnum(5);
    }
}


