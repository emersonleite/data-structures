"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SortedArray = void 0;
class SortedArray {
    constructor(vectorLength) {
        this.vectorLength = vectorLength;
        this.lastPosition = -1;
        this.values = Array(vectorLength);
    }
    printValues() {
        if (this.lastPosition === -1) {
            console.log("The array is empty");
        }
        else {
            for (let i = 0; i < this.lastPosition + 1; i++) {
                console.log(`${i} - ${this.values[i]}`);
            }
        }
    }
    addItem(value) {
        if (this.lastPosition === this.vectorLength - 1) {
            console.log("The array is full");
            return;
        }
        let position = 0;
        for (let i = 0; i <= this.lastPosition + 1; i++) {
            position = i;
            if (this.values[i] > value) {
                break;
            }
            if (i == this.lastPosition) {
                position = i + 1;
            }
        }
        let x = this.lastPosition;
        while (x >= position) {
            this.values[x + 1] = this.values[x];
            x -= 1;
        }
        this.values[position] = value;
        this.lastPosition += 1;
    }
    linearSearch(value) {
        for (let i = 0; i <= this.lastPosition + 1; i++) {
            if (this.values[i] > value) {
                return -1;
            }
            if (this.values[i] == value) {
                return i;
            }
            if (i == this.lastPosition) {
                return -1;
            }
        }
    }
    binarySearch(value) {
        let bottomLimit = 0;
        let topLimit = this.lastPosition;
        while (true) {
            let currentPosition = Math.floor((bottomLimit + topLimit) / 2);
            if (this.values[currentPosition] == value) {
                return currentPosition;
            }
            if (bottomLimit > topLimit) {
                return -1;
            }
            else {
                if (this.values[currentPosition] < value) {
                    bottomLimit = currentPosition + 1;
                }
                else {
                    topLimit = currentPosition - 1;
                }
            }
        }
    }
    removeItem(value) {
        let position = this.binarySearch(value);
        if (position === -1) {
            return -1;
        }
        else {
            for (let i = position; i <= this.lastPosition; i++) {
                this.values[i] = this.values[i + 1];
            }
            this.lastPosition -= 1;
        }
    }
}
exports.SortedArray = SortedArray;
let a1 = new SortedArray(10);
a1.addItem(3);
a1.addItem(2);
a1.addItem(6);
a1.addItem(4);
a1.addItem(1);
a1.addItem(85);
a1.addItem(52);
a1.addItem(8);
a1.addItem(9);
a1.addItem(5);
a1.removeItem(9);
a1.removeItem(85);
a1.removeItem(6);
a1.addItem(6);
a1.addItem(7);
a1.printValues();
//# sourceMappingURL=sortedArray.js.map