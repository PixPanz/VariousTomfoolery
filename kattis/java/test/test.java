// Just checking to see if I remember how to write basic Java code :)
// ...though it did take me a second to remember how to indicate a comment :/

import java.util.Scanner;

public class test {

    public static void main(String [] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Please enter anything at all");
        String variablename = scan.nextLine();
        scan.close();
        System.out.println("Cool here you go!\n" + variablename);
    }
}

// Also I needed to figure out how to build the code without an IDE...
