# 交替打印FooBar

我们提供一个类：
```
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
```
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。

**示例 1:**
```
输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
```
**示例 2:**
```
输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
```

**思路1:**
使用synchronized:
```java
class FooBar {
    private int n;
    private boolean flag = true;
    private Object lock = new Object();

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            synchronized(lock){
                while(!flag){
                    lock.wait();
                }
                // printFoo.run() outputs "foo". Do not change or remove this line.
        	    printFoo.run();
                flag = false;
                lock.notify();
            }
        	
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            synchronized(lock){
                while(flag){
                    lock.wait();
                }
                // printBar.run() outputs "bar". Do not change or remove this line.
        	    printBar.run();
                flag = true;
                lock.notify();
            }
            
        }
    }
}
```

**思路2:**
使用volatile修饰一个flag变量来判断该由谁执行，并且使用yield让不该执行的进程进入就需状态
```java
class FooBar {
    private int n;
    private volatile boolean flag = true;

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            while(!flag){
                Thread.yield();
            }
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
            flag = false;

        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            while(flag){
                Thread.yield();
            }
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
            flag = true;
        }
    }
}
```
