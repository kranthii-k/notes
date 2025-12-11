//printing n to 1 and n to 1 using recuersion

/*
public class Recursion {

    public static void printDec(int n){
        if (n==1){
            System.out.print(1 +" ");
            return;
        }
        printDec(n-1);
        System.out.print(n + " ");
    }
    public static void main(String[] args) {
        int n=10;
        printDec(n);
    }
}*/

//print the factorial of a num n
/*
public class Recursion {
    public static int fact(int n){
        if (n==0){
            return 1;
        }
        int fn=n*fact(n-1);
        return fn;
    }
    public static void main(String[] args) {
        System.out.println(fact(0));

    }

}*/

//print the sum fo n natural nums
/*
public class Recursion {
    public static int printNnums(int n){
        if (n==1){
            return 1;
        }
        int numN = n+printNnums(n-1);
        return numN;
    }

    public static void main(String[] args) {
        System.out.println(printNnums(2));

    }
}*/

/*
//fabnoci
public class Recursion {
    public static int fab(int n){
        if (n==0 || n==1){
            return n;
        }
        int fn1=fab(n-1);
        int fn2=fab(n-2);
        return fn1+fn2;
    }
    public static void main(String[] args) {
        System.out.println(fab(10));
    }
}
*/
//check the given array is sorted & first & last  occcurance in an aarray
/*
public class Recursion {

    public static boolean isSorted(int[] arr, int i){
        if (i== arr.length-1){
            return true;
        }
        if(arr[i]>arr[i+1]){
            return false;
        }
        return isSorted(arr ,i+1);
    }

    public static int firstOcccur(int arr[],int key,int i){
        if (i== arr.length){
            return -1;
        }
        if (arr[i]==key){
            return i;
        }
        return firstOcccur(arr,key,i+1);
    }

    public static int lastOcccur(int arr[],int key,int i){
        if (i==arr.length){
            return -1;
        }
        int isfoundd=lastOcccur(arr,key,i+1);
        if (isfoundd == -1 && arr[i]==key ){
            return i;
        }
        return isfoundd;
    }
    public static int pr_x_pow_n(int x,int n){
        if (n==0){
            return 1;
        }
        return x * pr_x_pow_n(x,n-1);
    }

    public static int optPow(int a, int n){
        if (n==0){
            return 1;
        }
        int halfPow=optPow(a,n/2);
        int halpowSq = halfPow * halfPow;
        if (n%2!=0){
            return a*halpowSq;
        }
        return halpowSq;
    }
    public static void main(String[] args) {

        //int arr[]={1,3,5,7,9,5};
        //System.out.println(isSorted(arr,0));
        //System.out.println(firstOcccur(arr,7,1));
        //System.out.println(lastOcccur(arr,5,0));
        //System.out.println(pr_x_pow_n(2,10));
        //System.out.println(optPow(2,5));
    }
}*/

//tiling problem
/*public class Recursion {
    public static int tail(int n){//2 x n
        //base case
        if (n==0 || n==1) {
            return 1;
        }
        //kaam
        //vertical choice
        int verticalTiles = tail(n-1);

        //horizontal choice
        int horTiles = tail(n-2);

        int toatalWays = verticalTiles + horTiles;
        return toatalWays;
    }
    public static void main(String[] args) {
        System.out.println(tail(3));
    }
}*/
//remove the duplicates in a string


/*

//friends pairing problem
public class Recursion {
public static int friendPairing(int n){
    if (n==1 || n==2){
        return n;
    }
    return friendPairing(n-1) + (n-1) * friendPairing(n-2);
}

    public static void main(String[] args) {
        System.out.println(friendPairing(4));
    }
}

*/
/*

public class Recursion {

    static int fibon(int n){
        if (n<2){
            return n;
        }
        return fibon(n-1) + fibon(n-2);
    }
    public static void main(String[] args) {
        int num = 10;
        for (int i=0 ; i<=num;i++){
            System.out.print(fibon(i) +" ");
        }
        //System.out.println(fibon(10));
    }
}*/
/*
public class Recursion {

    static void PrintBinSttr(int n, int LastPlace , String str){
        if (n==0){
            System.out.println(str);         //base condit
            return;
        }
        //kaaam
        PrintBinSttr(n-1, 0, str+"0");
        if (LastPlace==0){
            PrintBinSttr(n-1,1,str+"1");
        }
    }
    public static void main(String[] args) {
        PrintBinSttr(3, 0, "");
    }
}*/
/*
public class Recursion {

    static void PrintBinSttr(int n, int LastPlace , String str){
        if (n==0){
            System.out.println(str);         //base condit
            return;
        }
        //kaaam
        PrintBinSttr(n-1, 0, str+"1");
        if (LastPlace==0) {
            PrintBinSttr(n - 1, 1, str + "0");
        }
    }
    public static void main(String[] args) {
        PrintBinSttr(3, 0, "");
    }
}*/

public class Recursion {

    public static int printSumofDig(int n){
        if (n==0){
            return 0;
        }
//        int num=n/10;
//        int remLastNum=n%10;
//        int result= + printSumofDig(num);
        return (n%10)*10 + printSumofDig(n/10);
    }

    public static void main(String[] args) {
        int a=1345;
        System.out.println(printSumofDig(a));
    }
}