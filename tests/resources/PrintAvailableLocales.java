package resources;

import java.util.Locale;

public class PrintAvailableLocales {

    public static void main(String[] args) {
        for (final Locale locale: java.text.DecimalFormatSymbols.getAvailableLocales()) {
            System.out.println(locale);
        }
    }

}
