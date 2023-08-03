public class BubbleSort{
    public static void swap(int[] array, int from, int to){
        int temp = array[from]; 
        array[from] = array[to]; 
        array[to] = temp;
    }
    public static void bubble(int[] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = array.length - 1 ; j > i; j--) {
                if (array[j] < array[j-1])
                    swap(array,j,j-1);
            }
        }
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }
    public static void main(String args[]) {
        bubble(new int[] { 20, 12, 45, 19, 91, 55 });
    }
}

