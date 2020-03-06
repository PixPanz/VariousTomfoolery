import java.util.Scanner;

public class take_two_stones {

    public static void main(String [] args) {

        Scanner scan = new Scanner(System.in);
        int stones;
        stones = scan.nextInt();

        if (stones % 2 == 0) {
            System.out.println("Bob");
        }
        else {
            System.out.println("Alice");
        }
        scan.close();
    }
}