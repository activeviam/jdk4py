package resources;

import java.util.Arrays;
import java.util.Locale;
import java.util.stream.Collectors;

public class GetLocale {

    public static void main(String[] args) {
        System.out.println(
            Arrays.stream(
                java.text.DecimalFormatSymbols.getAvailableLocales()
            ).map(Locale::toString)
            .collect(Collectors.toList())
        );
    }

}