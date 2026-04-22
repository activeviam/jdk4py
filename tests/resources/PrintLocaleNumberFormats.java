package resources;

import java.text.DecimalFormatSymbols;
import java.util.Locale;

public class PrintLocaleNumberFormats {

    public static void main(String[] args) {
        for (final Locale locale: DecimalFormatSymbols.getAvailableLocales()) {
            final DecimalFormatSymbols dfs = DecimalFormatSymbols.getInstance(locale);
            System.out.println(
                locale.toLanguageTag()
                    + "\t" + ((int) dfs.getDecimalSeparator())
                    + "\t" + ((int) dfs.getGroupingSeparator())
            );
        }
    }

}
