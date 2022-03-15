import java.math.BigDecimal;
import java.util.Scanner;
import javax.swing.JFrame;

import java.awt.Graphics;
// import java.awt.Graphics2D;
// import java.awt.geom.Line2D;

public class App extends JFrame{

    public App(){
        super("Rysowanie maclarina");

        setSize(900, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Prosze podac n: ");
        
        int n = scanner.nextInt();
        scanner.close();

        double x = 0;

        BigDecimal drawA = new BigDecimal(0);
        BigDecimal drawB = getFormula(x, n);
    }

    void drawGraph(Graphics g, BigDecimal a, BigDecimal b){
        g.drawLine(a.intValue(), a.intValue(), b.intValue(), b.intValue());
    }

    public void paint(Graphics g){
        super.paint(g);
        // drawGraph(g, drawA, drawB);
    }

    public static BigDecimal getFormula(double x, int n){
        BigDecimal resoult = new BigDecimal(0);
        BigDecimal element = new BigDecimal(0);
        for(int i = 1; i < n; i++){
            element = new BigDecimal(0);
            double k = 1; 
            int j = switch(i%4){
                case 0 -> 0;
                case 1 -> -1;
                case 2 -> 0;
                case 3 -> 1;
                default -> throw new IllegalArgumentException("Unexpected value: " + i%4);
            };

            element.add(new BigDecimal(Math.pow(x, k) * j)); 

            for(int q = 1; q < i; q++) k *= q;

            element.divide(new BigDecimal(k)); 
            resoult.add(element);
        }
        return resoult;
    }
}
