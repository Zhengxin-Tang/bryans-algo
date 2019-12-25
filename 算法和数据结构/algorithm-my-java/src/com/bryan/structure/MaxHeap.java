package com.bryan.structure;

public class MaxHeap {

	private int[] data;
	private int capacity;
	private int count;
	
	public MaxHeap(int[] arr) {
		int n = arr.length;
		this.data = new int[n+1];
		this.capacity =n;
		this.count = n;
		for(int i=0;i<n;i++)
			this.data[i+1]=arr[i];
		
	}

	public int heap_size() {
		return this.count;
	}
	
	public boolean is_empty() {
		return this.count ==0;
	}
	
	private void shift_up(int k) {
		while(k > 1 && this.data[k/2] < this.data[k]) {
			int temp = this.data[k];
			this.data[k] = this.data[k/2];
			this.data[k/2] = temp;
			k = k/2;
		}
	}
	
	public void insert(int i) {
		if(this.count + 1 <= this.capacity) {
			this.data[this.count + 1]=i;
			this.count++;
			this.shift_up(this.count);
		}
		else {
			System.out.println("Cannot insert item, it reaches the capacity.");
		}
	}
	
	private void shift_down(int k) {
		while(2*k <= this.count) {
			int j = 2*k;
			if(j+1 <= this.count && this.data[j+1]>this.data[j]) {
				j++;
			}
			if(this.data[k] >= this.data[j]) {
				break;
			}
			int temp = this.data[k];
			this.data[k] = this.data[j];
			this.data[j] = temp;
			k = j;
		}
	}
	
	public int extract_max() {
		if(!is_empty()) {
			int res = this.data[1];
			int temp = this.data[1];
			this.data[1] = this.data[this.count];
			this.data[this.count] = temp;
			shift_down(1);
			return res;
		}
		else {
			System.out.println("Cannot extract max, the heap is empty.");
			return 0;
		}
	}
	
	public int[] getData() {
		return data;
	}

	public void setData(int[] data) {
		this.data = data;
	}

	public int getCapacity() {
		return capacity;
	}

	public void setCapacity(int capacity) {
		this.capacity = capacity;
	}

	public int getCount() {
		return count;
	}

	public void setCount(int count) {
		this.count = count;
	}
	
	public String toString() {
		String str = "";
		for(int i=0;i<this.count;i++)
			str += this.data[i];
		return str;
	}
	
}
