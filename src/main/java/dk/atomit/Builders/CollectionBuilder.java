package dk.atomit.Builders;

import java.util.ArrayList;
import java.util.Collection;

/**
 * @author Kristian Gausel
 *
 * Simple Collection builder
 */
public class CollectionBuilder<E> {

    private Collection<E> collection;

    /**
     * Uses type inference to create a CollectionBuilder
     * @param value item value to add
     * @param <E> Value type
     * @return a CollectionBuilder with one value
     */
    public static <E> CollectionBuilder<E> $$(E value){
        return new CollectionBuilder<E>().$(value);
    }

    /**
     * Uses type inference to create a CollectionBuilder
     * @param implementation implementation of Map to use
     * @param value item value to add
     * @param <E> Value type
     * @return a CollectionBuilder with one value
     */
    public static <E> CollectionBuilder<E> $$(Collection<E> implementation, E value){
        return new CollectionBuilder<>(implementation).$(value);
    }

    /**
     * CollectionBuilder
     * @param implementation the object to manipulate
     */
    public CollectionBuilder(Collection<E> implementation){
        collection = implementation;
    }

    /**
     * Uses an ArrayList as the default implementation
     */
    public CollectionBuilder(){
        collection = new ArrayList<>();
    }

    /**
     * Calls add on the underlying Collection
     * @param obj the object to add
     * @return this
     */
    public CollectionBuilder<E> $(E obj){
        collection.add(obj);
        return this;
    }

    /**
     * Returns the underlying Collection
     * @return the underlying Collection
     */
    public Collection<E> build(){
        return collection;
    }
}
