class MyCircularDeque {
    Deque<Integer> deque = new LinkedList<Integer>();
    private int maxSize;
    private int currentSize = 0;
    private int read;
    private int write;
    public MyCircularDeque(int k) {
        this.maxSize = k;
    }
    
    public boolean insertFront(int value) {
        
        if (isFull()){
            return false;
        } else {
            deque.addFirst(value);
            currentSize ++;
            return true;
        }
        
    }
    
    public boolean insertLast(int value) {
        if (isFull()){
            return false;
        } else {
            deque.addLast(value);
            currentSize ++;
            return true;
        }
        
    }
    
    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        } else {
            deque.removeFirst();
            currentSize --;
            return true;
        }
    }
    
    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        } else {
            deque.removeLast();
            currentSize --;
            return true;
        }
        
    }
    
    public int getFront() {
        if (isEmpty()){
            return -1;
        } else {
           return deque.getFirst();
        }
    }
    
    public int getRear() {
        if (isEmpty()){
            return -1;
        } else {
           return deque.getLast();
        }
        
    }
    
    public boolean isEmpty() {
        if (currentSize == 0){
            return true;
        }
        return false;
        
    }
    
    public boolean isFull() {
        if (currentSize == maxSize)
            return true;
        return false;
                
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
