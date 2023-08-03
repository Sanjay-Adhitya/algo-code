import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] final_array =  divide_and_merge_sort(new int[] { 20, 12, 45, 19, 91, 55 });
        for (int i = 0; i < final_array.length; i++) {
            System.out.println(final_array[i]);
        }
    }

    public static int[] divide_and_merge_sort(int[] array){
        if (array.length <= 1){
            return array;
        }
        int mid = array.length / 2;
        int[] r_array = Arrays.copyOfRange(array, 0, mid);
        int[] l_array = Arrays.copyOfRange(array, mid, array.length);
        r_array = divide_and_merge_sort(r_array);
        l_array = divide_and_merge_sort(l_array);
        return compare_merge(r_array, l_array);
    }

    public static int[] compare_merge(int[] r_array,int[] l_array){
        int l_index = 0;
        int r_index = 0;
        int[] merged = new int[r_array.length+l_array.length];
        while(l_index < l_array.length  && r_index < r_array.length ){
            if(r_array[r_index] < l_array[l_index]){
                merged[r_index] = r_array[r_index];
                r_index++;
            }else{
                merged[l_index] = l_array[l_index];
                l_index++;
            }   
        }
        
        System.arraycopy(l_array, 0, merged, 0, l_array.length);
        System.arraycopy(r_array, 0, merged, l_array.length, r_array.length);
        return merged;
    }
}
