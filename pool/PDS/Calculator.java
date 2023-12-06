import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {
    void setOperand1(int operand1) throws RemoteException;
    void setOperand2(int operand2) throws RemoteException;
    int getResult() throws RemoteException;
}

