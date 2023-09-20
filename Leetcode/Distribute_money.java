import java.util.Scanner;

public class Distribute_money {
    
    // Divide money among children
    // no child recieves exactly 4 dollars
    // Every child recieves at least 1 dollar

    private static int divide_money(int money, int children) {
        if (children > money) 
            return -1;
        
        boolean stop = false;
        int leftmoney, leftchildren, result = 0;

        while (!stop) {
            leftmoney = money - 8;
            leftchildren = children - 1;
            result = result + 1;

            if ((leftmoney == 1) && (leftchildren > 1))
                return -1;
            
        }
            
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int money = sc.nextInt();
        int children = sc.nextInt();
        System.out.println(divide_money(money, children));
        sc.close();
    }
}