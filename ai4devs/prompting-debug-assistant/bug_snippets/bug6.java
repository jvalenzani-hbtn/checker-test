// goal: add two prices and check a promo code
import java.math.BigDecimal;

public class Checkout {
  public static void main(String[] args) {
    // BUG: BigDecimal from double introduces precision error (use String)
    BigDecimal subtotal = new BigDecimal(0.1).add(new BigDecimal(0.2));
    System.out.println("Total = " + subtotal); // prints 0.30000000000000001665...

    String promo = new String("SAVE10");
    // BUG: String identity comparison instead of equals()
    if (promo == "SAVE10") {
      System.out.println("Promo applied");
    } else {
      System.out.println("Promo rejected"); // executes unexpectedly
    }
  }
}
