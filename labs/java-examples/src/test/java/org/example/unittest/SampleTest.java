package org.example.unittest;

import org.junit.*;

public class SampleTest {

  private static Resource expensiveResource;

  @BeforeClass
  public static void setUpClass() {
    expensiveResource = new Resource();
    expensiveResource.initialize();
  }

  @AfterClass
  public static void tearDownClass() {
    expensiveResource.cleanup();
  }

  @Before
  public void setUp() {
    System.out.println("Running before each test...");
  }

  @After
  public void tearDown() {
    System.out.println("Running after each test...");
  }

  @Test
  public void testMethod1() {
    Assert.assertTrue(true);
    System.out.println("Running testMethod1");
  }

  @Test
  public void testMethod2() {
    Assert.assertTrue(true);
    System.out.println("Running testMethod2");
  }
}
