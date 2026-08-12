package org.example.concurrent.c82;

public class RequestContext {
  private static ThreadLocal<String> localUserId = new ThreadLocal<>();
  ;
  private static ThreadLocal<Request> localRequest = new ThreadLocal<>();

  public static String getCurrentUserId() {
    return localUserId.get();
  }

  public static void setCurrentUserId(String userId) {
    localUserId.set(userId);
  }

  public static Request getCurrentRequest() {
    return localRequest.get();
  }

  public static void setCurrentRequest(Request request) {
    localRequest.set(request);
  }

  public static class Request { // ...
  }
}
