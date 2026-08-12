package org.example;

public class DaemonThreadExample {
  public static void main(String[] args) {
    Thread daemonThread = new Thread(new DaemonTask());
    daemonThread.setDaemon(true); // 设置为后台线程
    daemonThread.start();

    // 主线程继续执行其他任务
    System.out.println("Main thread is running.");

    // 当所有的用户线程结束时，JVM会自动退出，后台线程也会终止
  }
}

class DaemonTask implements Runnable {
  @Override
  public void run() {
    // 后台线程的任务
    while (true) {
      System.out.println("Daemon thread is running.");
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
