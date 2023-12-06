import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RMI_InterfaceFact extends Remote{
    public double computeFactorial(double input) throws RemoteException;
}