package org.example;

public class TestVolatile {
  public static void main(String[] args) {
    SharedObject sharedObject = new SharedObject();

    // 线程 1
    new Thread(sharedObject::increment).start();

    // 线程 2
    new Thread(
            () -> {
              System.out.println(sharedObject.getCounter());
            })
        .start();
  }
}

class SharedObject {
  private volatile int counter = 0;

  public void increment() {
    counter++;
  }

  public int getCounter() {
    return counter;
  }
}
