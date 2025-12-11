/*
import java.util.Scanner;

public class loops {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("enter the num to be printed");
        int range=sc.nextInt();


        int count=1;
        while (count<=range)   {
            System.out.println(count);
            count++;
        }
    }
}
*/

/*

public class loops {
    public static void main(String[] args) {
        int coum=0;
        while(coum<2999) {
            System.out.println("hello world");
            coum++;
        }
    }
}*/

/*
public class loops {
    public static void main(String[] args) {
        for (int i=1; i<=4; i++) {
            System.out.println("hello world");
        }
    }
}
*/

/*
public class loops {
    public static void main(String[] args) {
        int n=10899;

        while (n>0) {
            int lastdig = n % 10; //getting rem which is last digit
            System.out.print(lastdig);
            n = n / 10; //decreasing the exixting n value by dividing byb 10(last digit removed)
        }
    }
}
*/

//public class loops {
//    public static void main(String[] args) {
//        int count=0;
//        do{
//            System.out.println("hiii");
//            count++;
//
//        } while (count<4);
//    }
//}

/*

import java.util.Scanner;

public class loops {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);


        while(true){
            System.out.println("enter the num :");
            int n=sc.nextInt();
            if(n%10==0){
                break;
            }
            System.out.println(n);
        }
    }
}*/

/*

public class loops {
    public static void main(String[] args) {
        for (int i=1;i<=10;i++){
            if (i==7 || i==5 || i<=2){
                continue;
            }
            System.out.println(i);
        }
    }
}*/
/*

import java.util.Scanner;

public class loops {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);


        do {
            System.out.println("enter the num:");
            int num=sc.nextInt();
            if (num%10==0){
                continue;
            }
            System.out.println(num);

        } while(true);
    }
}*/


/*
import java.util.Scanner;

public class loops {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();

    boolean isprime=true;
    for (int i=2;i<=Math.sqrt(n);i++){
        if (n%i==0){
            isprime=false;
        }
    }
    if (isprime==true){
        System.out.println("prime");
    }else {
        System.out.println("not prime");


    }
    }
}*/
/*
public class loops {
    public static void main(String[] args) {
        int i;
        for (i=0; i<=5; i++){
            System.out.println("i="+i);

        }
        System.out.println("i after loop= " + i);
    }
}*/
/*

public class loops {
    public static void main(String[] args) {
        int n=4;

        for (int line=1; line<=n; line++){
            for(int num=1; num<=line; num++){
                System.out.print(num);
            }
            System.out.println();
        }
    }
}
*/


import java.util.Arrays;

public class loops {
    public static void main(String[] args) {
        char ch= 'A';
        int n=4;
        for (int i=1;i<=n; i++){
            for (int j=1;j<=i; j++){
                System.out.print(ch);
                ch++;
            }
            System.out.println();
        }
    }
}