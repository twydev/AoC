1. What is the difference between methodA and methodB:
```
class Test {
  int i = 0;
  
  synchronized void methodA() {
    i += 1;
    System.out.println(i);
  }
  
  void methodB() {
    synchronized (this) {
      i += 1;
      System.out.println(i);
    }
  }
}
```
- methodA is more efficient than methodB.
- methodB is more efficient than methodA.
- They are equivalent.
- None of the above.


---
2. What is the output for the following code:
```
public class Test {
  String str = "hello";
  
  public Test() {
    System.out.println("world");
  }
  
  public static void main(String[] args) {
    Test test = new Test();
    System.out.println(str);
  }
}
```
- hello
- world
- null
- compilation error.


---
3. Which of the following is true:
- If object obj1 references object obj2, and obj2 is eligible for garbage collection, then obj1 is also eligible.
- The delete keyword may be used in java code to trigger garbage collection.
- If an object cannot be accessed by any running threads, it will be garbage collected immediately.
- None of the above.


---
4. What is the output for the following code:
```
public class TestRun implements Runnable{
  String str;
  public TestRun(String str) {
    this.str = str;
  }
  public void run() {
    while (true) {
      System.out.print(str);
    }
  }
}

public class RunTest {
  public static void main(String[] args) {
    Thread runA = new Thread(new TestRun("A"));
    Thread runB = new Thread(new TestRun("B"));
    
    runB.start();
    runA.start();
  }
}
```
- BABABABA...
- AABAABAAB...
- Output sequence cannot be determined.
- None of the above.
