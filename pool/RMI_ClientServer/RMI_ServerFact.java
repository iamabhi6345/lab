import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;



public class RMI_ServerFact extends UnicastRemoteObject implements RMI_InterfaceFact{
    public RMI_ServerFact() throws RemoteException{
        super();
    }

    @Override
    public double computeFactorial(double n) throws RemoteException{

        System.out.println("Computing factorial for " + n);
        double fact = 1;
        for(int i = 1;i<=n;i++){
            fact = fact * i;
        }
        System.out.println("Factorial : " + fact);
        return fact;
    }
    public static void main(String[] args) {
        try{
            Registry registry = LocateRegistry.createRegistry(7777); 
            registry.bind("fact", new RMI_ServerFact());
            System.out.println("The RMI Factorial App is running and ready...");
        }catch(Exception e){
            System.out.println("Error : The RMI Factorial App is not running...");

        }
    }
}
