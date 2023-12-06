import java.rmi.Naming;
import java.util.Scanner;

public class User2Client {
    public static void main(String[] args) {
        try {
            Calculator calculator = (Calculator) Naming.lookup("rmi://your_server_ip_or_hostname/Calculator");

            Scanner scanner = new Scanner(System.in);

            // Get operand from user 2
            System.out.print("User 2, enter your operand: ");
            int operand2 = scanner.nextInt();

            calculator.setOperand2(operand2);

            // Get the result from the server
            int result = calculator.getResult();
            System.out.println("Result: " + result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

