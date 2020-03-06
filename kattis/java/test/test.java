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