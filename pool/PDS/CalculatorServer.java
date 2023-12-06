import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class CalculatorServer {
    public static void main(String[] args) {
        try {
            Calculator calculator = new CalculatorImpl();
            LocateRegistry.createRegistry(1099); // Use the default RMI registry port
            Naming.rebind("Calculator", calculator);
            System.out.println("Calculator server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

