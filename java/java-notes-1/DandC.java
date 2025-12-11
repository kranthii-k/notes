public class DandC {
    public static int search(int arr[] , int tar , int si, int ei){
        //base condition
        if (si>ei){
            return -1;
        }
        int mid=si+(ei-si)/2;
        //case found
        if (tar==arr[mid]){
            return mid;
        }
        //mid on L1
        if (arr[si] <= arr[mid]){
            //L1 Left
            if (arr[si] <= tar && tar <= arr[mid]){
                return search(arr,tar,si,mid-1);
            }
            else {
                return search(arr,tar,mid+1,ei);
            }
        }
        //mid on L2
        else {
            if (arr[mid]<=tar && tar <= arr[ei]){
                return search(arr,tar,mid+1,ei);
            }
            else {
                return search(arr,tar,si,mid-1);
            }
        }
    }

    public static void main(String[] args) {
        int arr[]={4,5,6,7,0,1,2};
        int target=0;
        int IndTarget=search(arr,target,0, arr.length-1);
        System.out.println(IndTarget);
    }
}
