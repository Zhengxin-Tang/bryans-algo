package com.bryan.sort;

public class Nn {

	public void bubble_sort(int[] arr) {
		boolean exchange = false;
		int n = arr.length;
		for (int i = n - 1; i >= 0; i--) {
			for (int j = 0; j < i; j++) {
				if (arr[j] > arr[j + 1]) {
					int temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
					exchange = true;
				}
			}
			if (!exchange)
				break;
		}
	}

	public void selection_sort(int[] arr) {
		int n = arr.length;
		for (int i = 0; i < n; i++) {
			int min_index = i;
			for (int j = i + 1; j < n; j++) {
				if (arr[j] < arr[min_index])
					min_index = j;
			}
			int temp = arr[i];
			arr[i] = arr[min_index];
			arr[min_index] = temp;
		}
	}

	public void insertion_sort(int[] arr) {
		int n = arr.length;
		for (int i = 1; i < n; i++) {
			int current = arr[i];
			int j = i;
			while (j > 0 && arr[j - 1] > current) {
				arr[j] = arr[j - 1];
				j--;
			}
			arr[j] = current;
		}
	}

	public void shell_sort(int[] arr) {
		int n = arr.length;
		int gap = n / 2;
		while (gap > 0) {
			for (int start_p = 0; start_p < gap; start_p++) {
				gap_insertion_sort(arr, start_p, gap);
			}
			gap = gap / 2;
		}
	}

	private void gap_insertion_sort(int[] arr, int start_p, int gap) {
		int n = arr.length;
		for (int i = start_p + gap; i < n; i += gap) {
			int current = arr[i];
			int j = i;
			while (j > start_p && arr[j - gap] > current) {
				arr[j] = arr[j - gap];
				j -= gap;
			}
			arr[j] = current;
		}
	}
}
