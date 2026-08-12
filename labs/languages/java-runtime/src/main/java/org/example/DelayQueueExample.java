package org.example;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.DelayQueue;
import java.util.concurrent.Delayed;
import java.util.concurrent.TimeUnit;

class DelayedElement implements Delayed {
  private long delayTime; // 延迟时间
  private long expire; // 到期时间

  public DelayedElement(long delayTime) {
    this.delayTime = delayTime;
    this.expire = System.currentTimeMillis() + delayTime;
  }

  @Override
  public long getDelay(TimeUnit unit) {
    return unit.convert(expire - System.currentTimeMillis(), TimeUnit.MILLISECONDS);
  }

  @Override
  public int compareTo(Delayed o) {
    if (this.expire < ((DelayedElement) o).expire) {
      return -1;
    }
    if (this.expire > ((DelayedElement) o).expire) {
      return 1;
    }
    return 0;
  }
}

public class DelayQueueExample {
  public static void main(String[] args) throws InterruptedException {
    BlockingQueue<DelayedElement> queue = new DelayQueue<>();

    queue.put(new DelayedElement(1000)); // 延迟1秒
    queue.put(new DelayedElement(3000)); // 延迟2秒

    while (!queue.isEmpty()) {
      DelayedElement element = queue.take(); // 只有延迟过期后才能取出
      System.out.println("取出元素，剩余元素: " + queue.size());
    }
  }
}
