package org.example.sql;

import java.util.List;
import org.apache.ibatis.session.SqlSession;
import org.example.entity.Student;
import org.example.mapper.TestMapper;

public class TestMybatis {

  public static void main(String[] args) {
    //    testStudent();

    try (SqlSession sqlSession = MybatisUtil.getSession(true)) {
      TestMapper testMapper = sqlSession.getMapper(TestMapper.class);
      List<Student> student = testMapper.selectStudent();
      student.forEach(System.out::println);
    }
  }

  private static void testStudent() {
    Student student = new Student();
    student.setSid(1);
    student.setName("shiyang");
    student.setSex("male");
    System.out.println(student);
  }
}
