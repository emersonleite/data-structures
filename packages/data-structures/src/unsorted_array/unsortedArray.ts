export class UnsortedArray {
  private vectorLength: number;
  private lastPosition: number;
  private values: number[];

  constructor(vectorLength: number) {
    this.vectorLength = vectorLength;
    this.lastPosition = -1;
    this.values = Array(vectorLength);
  }

  printValues() {
    if (this.lastPosition === -1) {
      console.log("The array is empty");
    } else {
      for (let i = 0; i < this.lastPosition + 1; i++) {
        console.log(`${i} - ${this.values[i]}`);
      }
    }
  }

  addItem(value: any) {
    if (this.lastPosition === this.vectorLength - 1) {
      console.log("The array is full");
    } else {
      this.lastPosition += 1;
      this.values[this.lastPosition] = value;
    }
  }

  searchItem(value: any) {
    for (let i = 0; i < this.lastPosition + 1; i++) {
      if (value === this.values[i]) {
        return i;
      }
    }
    return -1;
  }

  removeItem(value: number) {
    let position = this.searchItem(value);

    if (position === -1) {
      return -1;
    } else {
      for (let i: number = position; i <= this.lastPosition; i++) {
        this.values[i] = this.values[i + 1];
      }
      this.lastPosition -= 1;
    }
  }
}

/* let a = new UnsortedArray(10);

a.addItem(3);
a.addItem(2);
a.addItem(4);
a.addItem(5);
a.addItem(6);
a.addItem(1);

a.printValues();

a.searchItem(5);
a.searchItem(9);

a.removeItem(5);
a.addItem(5);

console.log("-----");

a.printValues(); */
