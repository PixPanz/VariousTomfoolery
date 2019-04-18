import java.util.Scanner;

public class newMain {
    
    public static void main(String [] args) {

        Scanner scan = new Scanner(System.in);
        String inText = scan.nextLine();
        String [] sText = inText.split("-");
        String ans = "";
        for (String s : sText)
        {
            ans += s.charAt(0);    
        }
        System.out.println(ans);
    }
}