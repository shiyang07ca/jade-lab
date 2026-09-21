package org.example.sql;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public final class MybatisUtil {
  private static final SqlSessionFactory SQL_SESSION_FACTORY = createSessionFactory();

  private MybatisUtil() {}

  private static SqlSessionFactory createSessionFactory() {
    Properties properties = new Properties();
    properties.setProperty("db.url", requireEnvironment("LAB_MYSQL_URL"));
    properties.setProperty("db.username", requireEnvironment("LAB_MYSQL_USERNAME"));
    properties.setProperty("db.password", requireEnvironment("LAB_MYSQL_PASSWORD"));

    try (InputStream config = Resources.getResourceAsStream("mybatis-config.xml")) {
      return new SqlSessionFactoryBuilder().build(config, properties);
    } catch (IOException error) {
      throw new ExceptionInInitializerError(error);
    }
  }

  private static String requireEnvironment(String name) {
    String value = System.getenv(name);
    if (value == null || value.isBlank()) {
      throw new IllegalStateException("missing required environment variable: " + name);
    }
    return value;
  }

  public static SqlSession getSession(boolean autoCommit) {
    return SQL_SESSION_FACTORY.openSession(autoCommit);
  }
}
