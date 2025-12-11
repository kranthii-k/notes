/*
public class functions {

    public static int mul(int a, int b){
        int m=a*b;
        return m;

    }

    public static void main(String[] args) {
        int a=10;
        int b=4;
        int pro=mul(a,b);
        System.out.println(pro);

    }
}

*/

/*
public class functions {

    public static void binToDec(int binNum){
        int mynum= binNum;
        int pow = 0;
        int decNum= 0;

        while (binNum>0) {
            int ld = binNum % 10;
            decNum+= ld* (int)Math.pow(2,pow);
            pow++;
            binNum=binNum/10;

        }
        System.out.println("dec of " + mynum + " is :" + decNum);
    }

    public static void main(String[] args) {
        binToDec(1010);

    }
}
*/


//: Write a Java method to compute the average of three numbers
/*

public class functions {

    public static void avgth(double a, double b , double c){
        double avg=(a+b+c)/3;
        System.out.println(avg);
    }




    public static void main(String[] args) {
        avgth(4,4,4);
    }
}*/


//: Write a method named isEven that accepts an int argument. The method
//should return true if the argument is even, or false otherwise. Also write a program to test
//your method.


/*
public class functions {

    public static void isEven(int num){
        if (num%2==0){
            System.out.println(true);
        } else {
            System.out.println(false);
        }

    }


    public static void main(String[] args) {
        isEven(9);

    }
}*/


/*  Write a Java program to check if a number is a palindrome in Java? ( 121 is a palindrome, 321 is not)
A number is called a palindrome if the number is equal to the reverse of a number e.g., 121 is
a palindrome because the reverse of 121 is 121 itself. On the other hand, 321 is not a
palindrome because the reverse of 321 is 123, which is not equal to 321.* /
 */


public class functions {

    public static void palin(int num){

        int original=num;
        int reverse=0;

        while (num!=0){
            int ld= num%10;
            reverse=reverse*10 + (ld);
            num=num/10;

        }

        if (original==reverse)  {
            System.out.println("pal");
        } else {
            System.out.println("not pal");
        }
    }


    public static void main(String[] args) {
        palin(1212);
    }
}