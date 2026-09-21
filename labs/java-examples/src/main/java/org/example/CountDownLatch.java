package org.example;

class CountDownLatch {
  public static void main(String[] args) throws InterruptedException {
    int numberOfTasks = 3;
    java.util.concurrent.CountDownLatch latch =
        new java.util.concurrent.CountDownLatch(numberOfTasks);

    for (int i = 0; i < numberOfTasks; i++) {
      new Thread(new Worker(latch)).start();
    }

    // 等待所有任务完成
    latch.await();
    System.out.println("所有任务已完成，主线程继续执行。");
  }
}

class Worker implements Runnable {
  private final java.util.concurrent.CountDownLatch latch;

  Worker(java.util.concurrent.CountDownLatch latch) {
    this.latch = latch;
  }

  public void run() {
    try {
      // 模拟任务执行
      Thread.sleep((long) (Math.random() * 1000));
      System.out.println("任务完成");
    } catch (InterruptedException e) {
      e.printStackTrace();
    } finally {
      // 完成任务时计数减一
      latch.countDown();
    }
  }
}
