package test;

public class ExampleJavaClass {
    private final double barDoubleNumber = 3.0;

    public static void main(String[] args) {
        // This is a comment
        System.out.println("Hello World");
    }

    public double getBar() {
        int foo = 42;
        return this.barDoubleNumber + foo;
    }

    public void foo(int fooValue) {
        System.out.println(fooValue);
    }

    public void doSomething(String somethingNew) {
        System.out.println(somethingNew);
    }
}