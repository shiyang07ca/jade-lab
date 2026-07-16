package org.example.collection;

import java.util.Arrays;
import java.util.Random;

class DynamicArray<E> {
  private static final int DEFAULT_CAPACITY = 10;

  private int size;
  private Object[] elementData;

  public DynamicArray() {
    this.elementData = new Object[DEFAULT_CAPACITY];
  }

  private void ensureCapacity(int minCapacity) {
    int oldCapacity = elementData.length;
    if (oldCapacity >= minCapacity) {
      return;
    }
    int newCapacity = oldCapacity * 2;
    if (newCapacity < minCapacity) newCapacity = minCapacity;
    elementData = Arrays.copyOf(elementData, newCapacity);
  }

  public void add(E e) {
    ensureCapacity(size + 1);
    elementData[size++] = e;
  }

  public E get(int index) {
    return (E) elementData[index];
  }

  public int size() {
    return size;
  }

  public E set(int index, E element) {
    E oldValue = get(index);
    elementData[index] = element;
    return oldValue;
  }
}

public class Test {

  static void testDynamicArray() {
    DynamicArray<Double> arr = new DynamicArray<Double>();
    Random rnd = new Random();
    int size = 1 + rnd.nextInt(10);
    for (int i = 0; i < size; i++) {
      arr.add(Math.random());
    }

    Double d = arr.get(rnd.nextInt(size));
    System.out.println(d);
  }

  public static void main(String[] args) {
    testDynamicArray();
  }
}
