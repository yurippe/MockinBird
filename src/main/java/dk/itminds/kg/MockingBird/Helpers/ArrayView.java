package dk.itminds.kg.MockingBird.Helpers;

import java.util.Iterator;

/**
 * @author Kristian Gausel
 * A view for an array, so you can iterate over ranges of the underlying array without making a copy.
 * The underlying array should not change while iterating!
 */
public class ArrayView<E> implements Iterable<E>{

    private E[] array;
    private int start;
    private int stop;

    public ArrayView(E[] array){
        this.array = array;
    }

    public ArrayView<E> setWindow(int start, int stop){
        this.start = start;
        this.stop = stop;
        return this;
    }

    public int size(){
        return array.length;
    }

    @Override
    public Iterator<E> iterator() {
        final int istart = this.start;
        final int istop = this.stop;

        return new Iterator<E>() {

            private int current = istart;

            @Override
            public boolean hasNext() {
                return current < istop;
            }

            @Override
            public E next() {
                E ret = array[current];
                current++;
                return ret;
            }
        };
    }
}
