package org.example.dynamic.c87;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class MyClassLoader extends ClassLoader {

  private static final String BASE_DIR = "data/c87/";

  @Override
  protected Class<?> findClass(String name) throws ClassNotFoundException {
    String fileName = name.replaceAll("\\.", "/");
    fileName = BASE_DIR + fileName + ".class";
    try {
      byte[] bytes = Files.readAllBytes(Path.of(fileName));
      return defineClass(name, bytes, 0, bytes.length);
    } catch (IOException ex) {
      throw new ClassNotFoundException("failed to load class " + name, ex);
    }
  }
}
