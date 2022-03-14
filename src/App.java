import java.util.Scanner;

public class App {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Prosze podac n: ");
        
        int n = scanner.nextInt();
        scanner.close();

        int sum = 0;

        for(int i = 1; i < n; i++){
            int j = 0;
            int a = 1;  
            switch(i%4){
                case 0:
                    
                    break;
                case 1:
                    break;
                case 2:
                    break;
                case 3:
                    break;
                
            }

            for(int q = 1; q < i; q++) a *= q;

        }
    }
}
