/*

//set bits google and amazon question

public class bitManipulation {

    public static int countSetbits(int n){
        int count=0;
        while (n>0){
            if ((n&1)!=0){
                count++;
            }
            n=n>>1;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countSetbits(10));
    }
}
*/


//fast exponantion
public class bitManipulation {

    public static int fastExpo(int a, int n){
        int ans=1;
        while (n>0){
            if ((n & 1) !=0){
                ans=ans*a;
            }
            a=a*a;
            n=n>>1;
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(fastExpo(5,2));

    }
}
