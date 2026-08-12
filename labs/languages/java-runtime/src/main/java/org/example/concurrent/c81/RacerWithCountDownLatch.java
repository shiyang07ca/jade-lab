package org.example.concurrent.c81;

import java.util.concurrent.CountDownLatch;

public class RacerWithCountDownLatch {

  public static void main(String[] args) throws InterruptedException {
    int num = 10;
    CountDownLatch latch = new CountDownLatch(1);
    Thread[] racers = new Thread[num];
    for (int i = 0; i < num; i++) {
      racers[i] = new Racer(latch);
      racers[i].start();
    }
    Thread.sleep(1000);
    latch.countDown();
  }

  static class Racer extends Thread {
    CountDownLatch latch;

    public Racer(CountDownLatch latch) {
      this.latch = latch;
    }

    @Override
    public void run() {
      try {
        this.latch.await();
        System.out.println(getName() + " start run " + System.currentTimeMillis());
      } catch (InterruptedException e) {
      }
    }
  }
}
