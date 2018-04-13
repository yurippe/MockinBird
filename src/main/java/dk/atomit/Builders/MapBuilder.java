package dk.atomit.Builders;

import java.util.HashMap;
import java.util.Map;

/**
 * @author Kristian Gausel
 *
 * Simple Map builder
 */
public class MapBuilder<K, V> {

    private Map<K, V> map;

    /**
     * Uses type inference to create a MapBuilder
     * @param key item key to add
     * @param value item value to add
     * @param <K> Key type
     * @param <V> Value type
     * @return a MapBuilder with one key-value mapping from key to value
     */
    public static <K, V> MapBuilder<K, V> $$(K key, V value){
        return new MapBuilder<K, V>().$(key, value);
    }

    /**
     * Uses type inference to create a MapBuilder
     * @param implementation implementation of Map to use
     * @param key item key to add
     * @param value item value to add
     * @param <K> Key type
     * @param <V> Value type
     * @return a MapBuilder with one key-value mapping from key to value
     */
    public static <K, V> MapBuilder<K, V> $$(Map<K, V> implementation, K key, V value){
        return new MapBuilder<>(implementation).$(key, value);
    }

    /**
     * MapBuilder
     * @param implementation the object to manipulate
     */
    public MapBuilder(Map<K, V> implementation) {
        map = implementation;
    }

    /**
     * Uses a HashMap as the default implementation
     */
    public MapBuilder() {
        map = new HashMap<>();
    }

    /**
     * Calls put on the underlaying map
     * @param key key
     * @param value value
     * @return This MapBuilder
     */
    public MapBuilder<K, V> $(K key, V value) {
        map.put(key, value);
        return this;
    }

    /**
     * Returns the underlying map
     * @return the underlying map
     */
    public Map<K, V> build() {
        return map;
    }


}
