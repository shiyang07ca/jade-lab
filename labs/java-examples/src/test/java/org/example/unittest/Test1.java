package org.example.unittest;

import org.junit.*;
import org.junit.Assert;
import org.junit.Test;

// 被测试的Java类
class Calculator {
  public int add(int number1, int number2) {
    return number1 + number2;
  }

  public double divide(int numerator, int denominator) {
    if (denominator == 0) {
      throw new IllegalArgumentException("Denominator cannot be zero.");
    }
    return (double) numerator / denominator;
  }
}

// 测试类

public class Test1 {
  @Test
  public void testAdd() {
    Calculator calculator = new Calculator();
    Assert.assertEquals(5, calculator.add(2, 3));
  }

  @Test
  public void testDivideByZero() {
    Calculator calculator = new Calculator();
    Assert.assertThrows(IllegalArgumentException.class, () -> calculator.divide(5, 0));
  }

  @Test
  public void whenAdding2And3_thenAnswerIs5() {
    Calculator calculator = new Calculator();
    Assert.assertEquals("Adding 2 and 3 should equal 5", 5, calculator.add(2, 3));
  }

  @Test(expected = IllegalArgumentException.class)
  public void whenDividingByZero_thenThrowIllegalArgumentException() {
    Calculator calculator = new Calculator();
    calculator.divide(10, 0);
  }
}
