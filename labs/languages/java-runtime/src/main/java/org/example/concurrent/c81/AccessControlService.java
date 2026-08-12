package org.example.concurrent.c81;

import java.util.concurrent.Semaphore;

public class AccessControlService {
  private static final int MAX_PERMITS = 100;
  private Semaphore permits = new Semaphore(MAX_PERMITS, true);

  public boolean login(String name, String password) {
    if (!permits.tryAcquire()) {
      // 同时登录用户数超过限制
      throw new ConcurrentLimitException();
    }
    // ..其他验证
    return true;
  }

  public void logout(String name) {
    permits.release();
  }

  public static class ConcurrentLimitException extends RuntimeException {
    private static final long serialVersionUID = 1L;
  }
}
