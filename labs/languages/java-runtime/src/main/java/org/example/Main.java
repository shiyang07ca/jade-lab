package org.example;

import java.beans.*;
import java.lang.management.ManagementFactory;
import java.util.Timer;
import java.util.TimerTask;

class Person {
  private String name;
  private int age;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }
}

public class Main {
  public static void main(String[] args) throws Exception {
    Timer t = new Timer();
    t.scheduleAtFixedRate(
        new TimerTask() {
          public void run() {
            System.out.println("3 seconds passed");
          }
        },
        0, // run first occurrence immediately
        3000); // run every three seconds

    //        testIntrospect();

    //    t1();
  }

  static void t1() {
    String jvmName = ManagementFactory.getRuntimeMXBean().getName();
    System.out.println("Current JVM Name: " + jvmName);

    // Extracting the PID if needed
    long pid = Long.parseLong(jvmName.split("@")[0]);
    System.out.println("Current JVM PID: " + pid);
  }

  private static void testIntrospect() throws Exception {
    BeanInfo info = Introspector.getBeanInfo(Person.class);
    for (PropertyDescriptor pd : info.getPropertyDescriptors()) {
      System.out.println(pd.getName());
      System.out.println("  " + pd.getReadMethod());
      System.out.println("  " + pd.getWriteMethod());
    }
  }
}
