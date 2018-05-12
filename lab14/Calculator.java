import java.util.Scanner;

public class Calculator {
  private double value1;
  private double value2;

  public Calculator(double v1, double v2) {
    value1 = v1;
    value2 = v2;
  }
  public void setValue(double v1, double v2) {
    value1 = v1;
    value2 = v2;
  }
  public double sum() {
    return value1 + value2;
  }

  public double difference() {
    return value1 - value2;
  }
  public double product(){
    return value1 * value2;
  }

  public double quotient(){
    return value1/value2;
  }

  public static void main(String[] args) {
    Calculator c = new Calculator(0,0);
    int n = 20;
    int i = 0;
    int[] Arr = new [20];
    while(n >0){

      c = new Calculator(n,n);
      Arr[i] = c;
      System.out.println("sum " + c.sum());
      System.out.println("diffrence " + c.difference());
      System.out.println("product " + c.product());
      System.out.println("quotient " + c.quotient());
      
      n--;
      i++;
    }

    c.setValue(3, 4);

}
}
