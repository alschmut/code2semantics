package test;

public class ExampleJavaClass {
    private final double barDoubleNumber = 3.0;

    public static void main(String[] args) {
        // This is a comment
        System.out.println("Hello World");
    }

    public double getBar() {
        return this.barDoubleNumber;
    }

    public void foo(int fooValue) {
        System.out.println(fooValue);
    }

    private void doSomething(String somethingNew) {
        System.out.println(somethingNew);
    }
}