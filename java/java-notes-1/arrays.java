/*
import java.util.Scanner;
//creating input output updating
public class arrays {
    public static void main(String[] args) {
        int marks[]=new int[10];
        Scanner sc=new Scanner(System.in);

        marks[0]= sc.nextInt();
        marks[1]= sc.nextInt();
        marks[2]= sc.nextInt();

        System.out.println("phy = " + marks[0]);
        System.out.println("matth =" +marks[1]);

        marks[2]=100; //updating
        System.out.println("che = " +marks[2]);
        System.out.println("percentage = " + (marks[0]+marks[1]+marks[2])/3 +"%");

    }
}
*/



//lineear search in arrays
/*

public class arrays {

    public static int LinSea(int num[] , int key){
        for (int i=0;i<num.length;i++){
            if (num[i]==key){
                return i;
            }

        } return -1;

    }

    public static void main(String[] args) {
        int num[]={1,2,3,4,5,6,7,89,9};
        int key=924;

        int index=LinSea(num , key);
        if (index==-1){
            System.out.println("not found");
        } else {
            System.out.println("index of thye given key value is = " +index);
        }

    }
}*/


//largest smallest in an array
/*

public class arrays {

    public static int getLarge(int num[]){
        int largest=Integer.MIN_VALUE;
        int smallest=Integer.MAX_VALUE;

        //access all the els in arr from index 0 to length of that arr
        for (int i=0;i< num.length;i++){
            //largest check , if larg is small than num[i] , we assign num to that larg variable
            if (largest<num[i]){
                largest=num[i];
            }
            if (smallest>num[i]){
                smallest=num[i];
            }

        }
        System.out.println("the smallest ele amaog the array = " + smallest);
        return largest;

    }


    public static void main(String[] args) {
        int nunb[]={1,4,5,6,3,8,2 , -80 ,-9};
//        getLarge(num);
        System.out.println("llargest  of this given array : " + getLarge(nunb));


    }
}*/


//binary search
/*

public class arrays {

    public static int binsearch(int num[] , int key ){
        int start=0, end=num.length-1;

        while(start<=end) {
            int mid=(start+end)/2;

            if (num[mid]==key) {
                return mid;
            }
            if (num[mid]<key){    //right
                start= mid+1;   //imp : start is after the mid value bczz of that num at mid is less than key
            } else {    //left
                end= mid-1;    //imp
            }
        } return -1;
    }


    public static void main(String[] args) {
        int nub[]={1,2,3,4,5,6,7,8,9,12,23,45,67,89,90,99};
        int ke=4;
        System.out.println("the key element  at the index of sorted array : " + binsearch(nub,ke));

    }
}*/


//reverse an array

/*
public class arrays {
    public static void reverse(int num[]){
        int first=0,last=num.length-1;

        while (first<=last){
            //swap
            int temp=num[last];
            num[last]=num[first];
            num[first]=temp;

            first++;
            last--;

        }

    }

    public static void main(String[] args) {
        int numbers[]={1,3,5,7,8,9};
        reverse(numbers);
        //print the reversrsed arra
//        System.out.print("reversed arrray is = ");
        for (int i=0;i< numbers.length;i++){
            System.out.print( numbers[i] +" ");
        }
        System.out.println();
    }
}
*/

//PAIRS IN ARR
/*

public class arrays {
    public static void ptintPairs(int num[]){
        int start=0;
        int last=num.length-1;
        for (int i=0;i< num.length;i++){
            int curr=num[i];
            for (int j=i+1; j< num.length;j++){
                System.out.print("(" + curr + ","+num[j] +")");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int num[]={1,2,34,4,6,89,5};
        ptintPairs(num);
    }
}
*/

/*

//print sub arrays
public class arrays {

    public static void printsubarr(int num[]){
        int tp=0;
        for(int i=0; i<num.length;i++){                           //start
            for (int j=i; j< num.length;j++){                     //end i.e.,from i++
                for (int k=i;k<=j;k++){                          //print from start to end
                    System.out.print(num[k]+" ");
                }
                tp++;
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("total number of sub arrays are tp= " + tp);
    }
    public static void main(String[] args) {
        int numbers[]={2,4,6,8,10};
        printsubarr(numbers);
    }
}
*/
/*

//MAX subarr I
public class arrays {

    public static void printsubarr(int num[]){
        int currSum=0;
        int maxSum=Integer.MIN_VALUE; //-infinity
        for(int i=0; i<num.length;i++){                           //start
            for (int j=i; j< num.length;j++){
                currSum=0;                                      //end i.e.,from i++
                for (int k=i;k<=j;k++){                          //print sum
                    currSum +=num[k];
                }
                System.out.println(currSum); //cursum no nheeeed just to check code is working
                if (maxSum<currSum){
                    maxSum=currSum;
                }

            }
        }
        System.out.println("MAx sum of sub array= " + maxSum);
    }
    public static void main(String[] args) {
        int numbers[]={2,4,6,8,10};
        //printsubarr(numbers);
        printsubarr(numbers);
    }
}*/
/*

//prefix subarray II
public class arrays {

    public static void subarraysum(int num[]){
        int currsum=0;
        int maxSum=Integer.MIN_VALUE;
        int prefix[]= new int[num.length];
        prefix[0]=num[0];
        for (int i=1; i< prefix.length;i++){          //creating a prefix array by calculating all prev sum + num[i]
            prefix[i]=prefix[i-1]+num[i];
        }
        for (int i=0;i<num.length;i++) {
            int start = i;
            for (int j = i; j < num.length; j++) {
                int end = j;
                currsum = start == 0 ? prefix[end] : prefix[end] - prefix[start - 1];


            }
            if (maxSum < currsum) {
                maxSum = currsum;
            }
        }
        System.out.println(maxSum);
    }

    public static void main(String[] args) {
            int numbers[]={2,4,6,8,10};
            subarraysum(numbers);

        }
}
*/

//subarrays III - kadans algorithm

/*public class arrays {

    public static void kadans(int num[]){
        int cs=0;
        int ms=Integer.MIN_VALUE;

        for (int i=0;i<num.length;i++){
            cs = cs + num[i];
            if (cs < 0) {
                cs = 0;
            }
            ms = Math.max(cs, ms);
        }
        System.out.println(ms);
    }

    public static void main(String[] args) {
        int numbers[]={2,4,6,8,10};
        kadans(numbers);
    }
}*/
/*

public class arrays {

    public static int trappedrainw(int height[]){
        int n= height.length;
        //calculate left maax boundary -array


    }

    public static void main(String[] args) {

    }
}
*/


//buy aand sell stoocks
public class arrays{

    public static int buyandsellstocks(int prices[]){
        int buyprice=Integer.MAX_VALUE;
        int maxprofit=0;

        for (int i=0;i<prices.length;i++){
            if (buyprice<prices[i]){
                int profit=prices[i]-buyprice;
                maxprofit=Math.max(maxprofit,profit);
            } else {
                buyprice=prices[i];
            }
        } return maxprofit;

    }

    public static void main(String[] args) {
        int prices[]={7,1,5,3,6,4};
        System.out.println(buyandsellstocks(prices));

    }
}