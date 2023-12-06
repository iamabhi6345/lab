import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.util.Scanner;

public class RMI_Client {

    private static Scanner scan = null;
    public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
        try{
            RMI_InterfaceFact fact = (RMI_InterfaceFact) Naming.lookup("rmi://localhost:7777/fact");
            RMI_InterfaceSumN sumN = (RMI_InterfaceSumN) Naming.lookup("rmi://localhost:8888/sumn");
            scan = new Scanner(System.in);

            for(;;){
                System.out.println("*******************************************");
                System.out.println("THE RMI App for Factorial and Sum upto N");
                System.out.println();
                
                System.out.println("Enter number for factorial : ");
                double f = fact.computeFactorial(getInput());
                System.out.println("Factorial : " + f);
                System.out.println("Enter number for Sum : ");
                double n =sumN.sumUptoN(getInput());
                System.out.println("Sum : " + f);

                System.out.println("Total Sum : " + (f+n));
                System.out.println();
            }

        }catch(Exception e){
            System.out.println("ERROR: The RMI_Client is not working...");
            e.printStackTrace();
        }
    }

    public static double getInput(){
        try{
            double input = scan.nextInt();
            return input;

        }catch(Exception e){
            System.err.println("ERROR: Please try a valid number. ");
            return getInput();
        }
    }
    
}
