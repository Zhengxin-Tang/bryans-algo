package com.bryan.sort;

import java.util.Arrays;
import java.util.Random;

public class Nlogn {

	public void merge_sort(int[] arr) {
		if (arr.length <= 16) {
			new Nn().insertion_sort(arr);
		} else {
			int mid = arr.length / 2;
			int[] left_arr = Arrays.copyOfRange(arr, 0, mid);
			int[] right_arr = Arrays.copyOfRange(arr, mid, arr.length);
			merge_sort(left_arr);
			merge_sort(right_arr);
			if (left_arr[left_arr.length - 1] > right_arr[0])
				merge(arr, left_arr, right_arr);
		}
	}

	private void merge(int[] arr, int[] left_arr, int[] right_arr) {
		int i = 0;
		int j = 0;
		int k = 0;
		while (i < left_arr.length && j < right_arr.length) {
			if (left_arr[i] < right_arr[i]) {
				arr[k] = left_arr[i];
				i++;
			} else {
				arr[k] = right_arr[j];
				j++;
			}
			k++;
		}
		while (i < left_arr.length) {
			arr[k] = left_arr[i];
			i++;
			k++;
		}
		while (j < right_arr.length) {
			arr[k] = right_arr[j];
			j++;
			k++;
		}
	}

	public void quick_sort(int[] arr, int left, int right) {
		if (left < right) {
			if (right - left < 16) {
				new Nn().insertion_sort(arr);
			}
			int p = partition(arr, left, right);
			quick_sort(arr, left, p - 1);
			quick_sort(arr, p + 1, right);
		}
	}

	private int partition(int[] arr, int left, int right) {
		Random r = new Random();
		int random_p = r.nextInt(right - left + 1) + left;
		int temp = arr[left];
		arr[left] = arr[random_p];
		arr[random_p] = temp;

		int p = left;
		for (int i = left + 1; i <= right; i++) {
			if (arr[i] < arr[left]) {
				temp = arr[i];
				arr[i] = arr[p + 1];
				arr[p + 1] = temp;
				p++;
			}
		}
		temp = arr[p];
		arr[p] = arr[left];
		arr[left] = temp;
		return p;
	}
}
