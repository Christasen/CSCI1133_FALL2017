import java.util.Scanner;//get the input from user
//print does not need Scanner
//str.charAt(index)
//String cat = "meow"
//char[] catArr = cat.toCharArray()
//char[] catArr = {'m','e','o','w'}
//char[] arr = new char[50]

public class PerfectNum{
  public static void main(String[] args) {
    Scanner myscanner = new Scanner(System.in); //this is really essential
    System.out.print("Enter the upper limit: "); //The way you want to cout something in terminal
    int limit = myscanner.nextInt(); //is a methond //next is default to a string //nextDouble()
    int n = 1;
    while (n <= limit){
      int i = 1;
      int fact = 0;
      while ( i < n){
        if (n%i == 0)
          fact += i;
        i  += 1;
      }
      if (fact == n)
        System.out.println(n+" is a perfect number!"); //print something in a new line
      n = n +1;
    }





  } //this is the sample of main function //main by default takes strings
}
