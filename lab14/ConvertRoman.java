import java.util.Scanner;//get the input from user
//print does not need Scanner

public class ConvertRoman{
  public static void main(String[] args){
    Scanner myscanner = new Scanner(System.in);
    //this is really essential
    //The way you want to cout something in terminal
    boolean done = false;
    while (!done){
      System.out.print("Enter a Roman Numeral as a string: ");
      String romannumeral = myscanner.nextLine();//get the next line of the strings
      if (romannumeral.length() == 0) //objects and primitives;
        done = true;
      else
        System.out.println("Decimal value: " + convertRoman(romannumeral)+"\n");
    }
  }

  public static int convertDigit(char letter){
    String digits = "IVXLCDM";

    char[] Arr = digits.toCharArray();
    int[] values = {1,5,10,50,100,500,1000};
    int i = 0;
    while((i < digits.length()) && (letter != Arr[i]))
      i = i +1;
    if (i < digits.length())
      return values[i];
    return 0;
  }

  public static int convertRoman(String istr){
    int lastvalue = 0;
    int decimalval = 0;
    for(char ch : istr.toCharArray()) {
    //for(int i = 0; i < istr.lenght(); i++)
      int currentvalue = convertDigit(ch);
      if (lastvalue < currentvalue)
        decimalval -= lastvalue;
      else
        decimalval += lastvalue;
      lastvalue = currentvalue;
    }
      return decimalval + lastvalue;

  }


}
