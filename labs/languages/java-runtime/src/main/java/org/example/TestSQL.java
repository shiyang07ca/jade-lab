package org.example;

import java.lang.reflect.Constructor;
import java.sql.*;

public class TestSQL {

  private static <T> T convert(ResultSet set, Class<T> clazz) {
    try {
      Constructor<T> constructor =
          clazz.getConstructor(clazz.getConstructors()[0].getParameterTypes()); // 默认获取第一个构造方法
      Class<?>[] param = constructor.getParameterTypes(); // 获取参数列表
      Object[] object = new Object[param.length]; // 存放参数
      for (int i = 0; i < param.length; i++) { // 是从1开始的
        object[i] = set.getObject(i + 1);
        if (object[i].getClass() != param[i])
          throw new SQLException("错误的类型转换：" + object[i].getClass() + " -> " + param[i]);
      }
      return constructor.newInstance(object);
    } catch (ReflectiveOperationException | SQLException e) {
      e.printStackTrace();
      return null;
    }
  }

  private static void testConnection() {
    try {
      Class.forName("com.mysql.cj.jdbc.Driver");
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
    }

    // 1. 通过DriverManager来获得数据库连接
    try (Connection connection =
            DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "");
        // 2. 创建一个用于执行SQL的Statement对象
        Statement statement = connection.createStatement()) { // 注意前两步都放在try()中，因为在最后需要释放资源！
      // 3. 执行SQL语句，并得到结果集
      ResultSet set = statement.executeQuery("select * from t1");
      // 4. 查看结果
      while (set.next()) {
        System.out.println(set.getString(1));
      }
    } catch (SQLException e) {
      e.printStackTrace();
    }
  }

  private static void insertTestData() {
    try (Connection connection =
            DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "");
        Statement statement = connection.createStatement()) {

      statement.addBatch("insert into t1 values ('f')");
      statement.addBatch("insert into t1 values ('e')"); // 添加每一条批处理语句
      statement.executeBatch(); // 一起执行

    } catch (SQLException e) {
      e.printStackTrace();
    }
  }

  public static void main(String[] args) throws ClassNotFoundException {
    System.out.println("==========");
    testConnection();

    //    insertTestData();
  }
}
