// goal: trim a query parameter and parse an integer
import java.util.Map;

public class Parser {
  public static int parseLimit(Map<String, String> query) {
    // BUG: query.get("limit") may be null -> NullPointerException on trim()
    String raw = query.get("limit").trim();
    return Integer.parseInt(raw); // may also throw NumberFormatException
  }

  public static void main(String[] args) {
    System.out.println(parseLimit(Map.of())); // triggers NPE
  }
}
