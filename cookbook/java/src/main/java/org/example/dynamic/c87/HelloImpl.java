package org.example.dynamic.c87;

public class HelloImpl implements IHelloService {
  @Override
  public void sayHello() {
    System.out.println("hello from the reloadable implementation");
  }
}
