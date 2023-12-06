import java.rmi.Naming;
import java.util.Scanner;

public class User1Client {
    public static void main(String[] args) {
        try {
            Calculator calculator = (Calculator) Naming.lookup("rmi://your_server_ip_or_hostname/Calculator");

            Scanner scanner = new Scanner(System.in);

            // Get operand from user 1
            System.out.print("User 1, enter your operand: ");
            int operand1 = scanner.nextInt();

            calculator.setOperand1(operand1);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

