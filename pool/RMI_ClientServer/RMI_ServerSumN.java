import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;



public class RMI_ServerSumN extends UnicastRemoteObject implements RMI_InterfaceSumN{
    public RMI_ServerSumN() throws RemoteException{
        super();
    }

    @Override
    public double sumUptoN(double n) throws RemoteException{
        System.out.println("Computing sum for " + n);
        double res = (n*(n+1))/2;
        System.out.println("Sum upto "+n+" : " + res);
        return res;
    }

    public static void main(String[] args) {
        try{
            Registry registry = LocateRegistry.createRegistry(8888); 
            registry.bind("sumn", new RMI_ServerSumN());
            System.out.println("The RMI Sum App is running and ready...");
        }catch(Exception e){
            System.out.println("Error : The RMI Sum App is not running...");

        }
    }
}
