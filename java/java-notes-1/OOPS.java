/*
public class OOPS {

    public static void main(String[] args) {
        Pen p1=new Pen();
        p1.Setcolor("bluee");
        System.out.println();
    }
}

class Pen {
    private String color;
    private int tip;

    void Setcolor(String color){
        this.color=color;
    }
    void SetTip(int newTip){
        tip=newTip;
    }
}
*/


/*

//20 abstract class
public class OOPS {
    public static void main(String[] args) {
        Horse h = new Horse();
        h.eat();
        h.walk();

        Chick c= new Chick();
        c.eat();
        c.walk();

        */
/*Animal a = new Animal() {
            @Override
            void walk() { //error becz we cannot
                }
            }*//*


    }
}

abstract class Animal {
    void eat() {
        System.out.println("animal eats");
    }

    abstract void walk();
}
class Horse extends Animal{
    void walk() {
        System.out.println("walks on 4 legs");
    }
}

class Chick extends Animal {
    void walk() {
        System.out.println("walks on 2 straw like legs");
    }
}
*/

//21 interfaces
/*

public class OOPS {
    public static void main(String[] args) {
        Queen q = new Queen();
        q.moves();
        King k= new King();
    }
}

interface Harbiover{

}
interface carnivour {

}
class mammles implements Harbiover , carnivour{

}


interface ChessPlayer {
    void moves();
}
class Queen implements ChessPlayer{
    public void moves() {
        System.out.println("up,down,left,right,diagonal");
    }
}
class King implements ChessPlayer {
    public void moves()  {
        System.out.println("one step but he is king");
    }
}*/

//printing n to 1 and n to 1 using recuersion

/*
public class OOPS {

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
public class OOPS {

}