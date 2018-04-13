package dk.atomit.Builders;

import java.util.Collection;
import java.util.Map;

/**
 * @author Kristian Gausel
 *
 * EntryPoint class for other builder. This is just for the sake of readability and convenience
 */
public class Builders {

    /*------------------------------------------------------------------
    | Map
    --------------------------------------------------------------------*/
    public static <K, V> MapBuilder<K, V> $(Map<K, V> implementation){
        return new MapBuilder<>(implementation);
    }

    public static <K, V> MapBuilder<K, V> $(K key, V value){
        return MapBuilder.$$(key, value);
    }

    /*------------------------------------------------------------------
    | Collection
    --------------------------------------------------------------------*/
    public static <E> CollectionBuilder<E> $(Collection<E> implementation){
        return new CollectionBuilder<>(implementation);
    }

    public static <E> CollectionBuilder<E> $(E value){
        return CollectionBuilder.$$(value);
    }

}
