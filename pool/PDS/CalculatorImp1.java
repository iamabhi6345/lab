import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalculatorImpl extends UnicastRemoteObject implements Calculator {
    private int operand1;
    private int operand2;

    public CalculatorImpl() throws RemoteException {
        // Constructor
    }

    @Override
    public void setOperand1(int operand1) throws RemoteException {
        this.operand1 = operand1;
    }

    @Override
    public void setOperand2(int operand2) throws RemoteException {
        this.operand2 = operand2;
    }

    @Override
    public int getResult() throws RemoteException {
        return operand1 + operand2;
    }
}

