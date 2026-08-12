package org.example.doc;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class OptionalTest {

  public static <T> T requireNonNull(T obj) {
    if (obj == null) {
      throw new NullPointerException();
    } else {
      return obj;
    }
  }

  public static <T> void main(String[] args) {
    Optional<T> optional = Optional.empty();
    //    Optional<T> optional2 = Optional.of(objectT);
    System.out.println(optional);

    Map<String, Object> map = new HashMap<>();
    map.put("foo", "bar");
    String value1 = Optional.ofNullable(map.get("foo")).map(Object::toString).orElse("helloworld");
    String value2 = Optional.ofNullable(map.get("ops")).map(Object::toString).orElse("helloworld");
    System.out.println(Arrays.asList(value1, value2));
  }
}
