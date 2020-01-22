package com.bryan.test;

import java.util.Random;

import com.bryan.sort.Nlogn;
import com.bryan.sort.Nn;

public class SortTestHelper {

	Random random;
	Nn nn;
	Nlogn nlogn;

	public SortTestHelper() {
		random = new Random();
		nn = new Nn();
		nlogn = new Nlogn();
	}

	public int[] generate_random_array(int n, int left, int right) {
		int[] random_list = new int[n];
		for (int i = 0; i < n; i++) {
			random_list[i] = random.nextInt(right - left + 1) + left;
		}
		return random_list;
	}

	public int[] generate_nearly_ordered_array(int n, int swap_time) {
		int[] nearly_ordered_list = new int[n];
		for (int i = 0; i < n; i++) {
			nearly_ordered_list[i] = i;
		}
		for (int j = 0; j < swap_time; j++) {
			int x = random.nextInt(n + 1);
			int y = random.nextInt(n + 1);
			int temp = nearly_ordered_list[x];
			nearly_ordered_list[x] = nearly_ordered_list[y];
			nearly_ordered_list[y] = temp;
		}
		return nearly_ordered_list;
	}

	public boolean is_sorted(int[] arr) {
		int n = arr.length;
		for (int i = 0; i < n - 1; i++) {
			if (arr[i] > arr[i + 1])
				return false;
		}
		return true;
	}

	public int[] copy_array(int[] arr) {
		int n = arr.length;
		int[] new_list = new int[n];
		for (int i = 0; i < n; i++) {
			new_list[i] = arr[i];
		}
		return new_list;
	}

	public void print_arr(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

	public void run_bubble_sort(int[] arr) {
		long start_time = System.nanoTime();
		nn.bubble_sort(arr);
		long stop_time = System.nanoTime();
		if (is_sorted(arr))
			System.out.println("The list is sorted.");
		else
			System.out.println("The list is not sorted.");
		System.out.println("Bubble sort run time:" + (stop_time - start_time));
	}

	public void run_selection_sort(int[] arr) {
		long start_time = System.nanoTime();
		nn.selection_sort(arr);
		long stop_time = System.nanoTime();
		if (is_sorted(arr))
			System.out.println("The list is sorted.");
		else
			System.out.println("The list is not sorted.");
		System.out.println("Selction sort run time:" + (stop_time - start_time));
	}

	public void run_insertion_sort(int[] arr) {
		long start_time = System.nanoTime();
		nn.insertion_sort(arr);
		long stop_time = System.nanoTime();
		if (is_sorted(arr))
			System.out.println("The list is sorted.");
		else
			System.out.println("The list is not sorted.");
		System.out.println("Insertion sort run time:" + (stop_time - start_time));
	}

	public void run_shell_sort(int[] arr) {
		long start_time = System.nanoTime();
		nn.shell_sort(arr);
		long stop_time = System.nanoTime();
		if (is_sorted(arr))
			System.out.println("The list is sorted.");
		else
			System.out.println("The list is not sorted.");
		System.out.println("Shell sort run time:" + (stop_time - start_time));
	}

	public void run_merge_sort(int[] arr) {
		long start_time = System.nanoTime();
		nlogn.merge_sort(arr);
		long stop_time = System.nanoTime();
		if (is_sorted(arr))
			System.out.println("The list is sorted.");
		else
			System.out.println("The list is not sorted.");
		System.out.println("Merge sort run time:" + (stop_time - start_time));
	}

	public void run_quick_sort(int[] arr) {
		long start_time = System.nanoTime();
		nlogn.quick_sort(arr, 0, arr.length - 1);
		long stop_time = System.nanoTime();
		if (is_sorted(arr))
			System.out.println("The list is sorted.");
		else
			System.out.println("The list is not sorted.");
		System.out.println("Quick sort run time:" + (stop_time - start_time));
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SortTestHelper helper = new SortTestHelper();
		int[] arr1 = helper.generate_random_array(10000, 0, 10000);
		int[] arr2 = helper.copy_array(arr1);
		int[] arr3 = helper.copy_array(arr1);
		int[] arr4 = helper.copy_array(arr1);
		int[] arr5 = helper.copy_array(arr1);
		int[] arr6 = helper.copy_array(arr1);
		helper.run_bubble_sort(arr1);
		helper.run_selection_sort(arr2);
		helper.run_insertion_sort(arr3);
		helper.run_shell_sort(arr4);
		helper.run_merge_sort(arr5);
		helper.run_quick_sort(arr6);
	}

}
