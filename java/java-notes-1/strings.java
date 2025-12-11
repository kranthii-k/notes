/*
import java.util.Scanner;

public class strings {
    public static void main(String[] args) {
        String name="baby";
        //System.out.println(name);
        Scanner sc=new Scanner(System.in);
        String babu;
        babu=sc.nextLine();
        System.out.println(babu);
    }
}
*/

//string is a palindrome or not
/*
public class strings {
    public static boolean isPalindrome(String str){
        for (int i=0;i<str.length()/2;i++){
            if (str.charAt(i)!=str.charAt(str.length()-1-i)){    //n-1-i
                return false;
            }
        }
        return true;
    }


    public static void main(String[] args) {
        String str="rcar";
        //isPalindrome(str);
        System.out.println(isPalindrome(str));

    }
}*/

import javax.swing.plaf.PanelUI;
import java.awt.*;
import java.util.Scanner;
/*

//shortest path
public class strings {
    public static float shortestPath(String path){
        int x=0,y=0;
        for (int i=0; i<path.length();i++){
            char dir=path.charAt(i);
            //south
            if (dir=='S'){
                y--;
            }
            else if (dir=='N'){
                y++;
            }
            else if (dir=='W'){
                x--;
            }
            else {
                x++;
            }
        }
        int X2=x*x;
        int Y2=y*y;
        return (float)Math.sqrt(X2+Y2);
    }


    public static void main(String[] args) {
        String str="WNEENESENNN";
        System.out.println(shortestPath(str));
    }
}*/


/*
//strinj builder
public class strings {
    public static void main(String[] args) {
        StringBuilder sb=new StringBuilder("");
        for (char ch='A'; ch<='Z';ch++){
            sb.append(ch );
        }
        System.out.println(sb);

    }
}*/
/*
//convert the first letter of each word to upperCase
public class strings {

    public static String toUppercasee(String str){
        StringBuilder sb=new StringBuilder("");
        char ch = Character.toUpperCase(str.charAt(0));
        sb.append(ch);

        for (int i=1;i<str.length();i++){
            if (str.charAt(i)==' ' && i<str.length()-1){
                sb.append(str.charAt(i));
                i++;
                sb.append(Character.toUpperCase(str.charAt(i)));
            } else {
                sb.append(str.charAt(i));
            }
        }
return sb.toString();
    }



    public static void main(String[] args) {
        String str="hi i am Kranthi , i can code in java";
        //toUppercasee(str);
        System.out.println(toUppercasee(str));
    }
}*/
//string compression
/*

public class strings {

    //String newStr="";
    public static String compression(String str){
        StringBuilder sb=new StringBuilder("");
        for (int i=0;i<str.length();i++){
            Integer count=1;
            while (i<str.length()-1 && str.charAt(i)==str.charAt(i+1)){
                count++;
                i++;
            }
            sb.append(str.charAt(i));
            if (count>1){
                sb.append(count.toString());
            }

        }
        return sb.toString();

    }

    public static void main(String[] args) {
        String str="aaabbcccddeeee";
        System.out.println(compression(str));
    }
}

*/
/*

public class strings {

    public static String compression(String str){
        String newStr="";
        for (int i=0; i<str.length();i++){
            Integer count=1;
            while (i<str.length()-1 && str.charAt(i)==str.charAt(i+1)){
                count++;
                i++;
            }
            newStr += str.charAt(i);
            if (count>1){
                newStr+=count.toString();
            }
        }
        return newStr;
    }


    public static void main(String[] args) {
        String str="aaabbcccddeeee";
        System.out.println(compression(str));
    }
}*//*


//count how many vowels occuewd

*/

/*
public class strings {


    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String str=sc.nextLine();

        int count=0;
        for (int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            if (ch == 'a' || ch== 'e' || ch=='i' || ch== 'o' || ch== 'u'){
                count++;
                //return true;

            }
        }
       // return false;
        System.out.println(count);
    }
}*/

public class strings {
    public static void main(String[] args) {
        for (int i=1;i<=800;i++){
            System.out.print("1");
        }
    }
}