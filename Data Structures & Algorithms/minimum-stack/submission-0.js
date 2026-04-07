class MinStack {
    stack = []
    min = []; 

    constructor() {
        return null;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (this.min.length === 0) this.min.push(val)
        else this.min.push(Math.min(this.min[this.min.length-1], val))
        return null;
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop();
        this.min.pop();
        return null;
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length-1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min[this.min.length-1];
    }
}
