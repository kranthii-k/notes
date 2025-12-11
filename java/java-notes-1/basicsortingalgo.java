public class basicsortingalgo {

    public static void Bubblesort(int arr[]){
        for (int turn=0;turn<= arr.length-2; turn++){  //n-2 becfause we compare 2 -2 eles at once
            int swap=0;
            for (int j=0;j<= arr.length-2-turn;j++){
                if (arr[j+1]<arr[j]){
                    //swap
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                    swap++;
                }
            }
            System.out.println(swap);
        }
    }
    //funtion to print this arrey
    public static void prbubblesortedarr(int arr[]){
        for (int i=0; i< arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }

    public static void selectionSort(int arr[]){
        for (int i=0;i< arr.length-1;i++){
            int minPos=i;          //current as minPOstiion
            for (int j=i+1;j< arr.length;j++){
                if (arr[minPos]>arr[j]){
                    minPos=j;
                }
            }
            //swap
            int temp=arr[minPos];
            arr[minPos]=arr[i];
            arr[i]=temp;

        }
    }
    public static void insertionSort(int arr[]){
        for (int i=1;i< arr.length;i++){
            int curr=arr[i];
            int prev=i-1;
            //finding out correct podition to insert
            while(prev>=0 && arr[prev]>curr){
                arr[prev+1]=arr[prev];
                prev--;

            }
            //insertion
            arr[prev+1]=curr;
        }
    }
    public static void main(String[] args) {
        int arr[]={5,4,3,2,1};
        //Bubblesort(arr);
        //selectionSort(arr);
        insertionSort(arr);
        prbubblesortedarr(arr);

    }
}
