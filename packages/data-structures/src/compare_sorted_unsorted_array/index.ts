import { getData as getRandomData, getTime } from "../generateData";
import { SortedArray } from "../sorted_array/sortedArray";
import { UnsortedArray } from "../unsorted_array/unsortedArray";

let data = getRandomData(9999);

let sortedArray = new SortedArray(9999);

let unsortedArray = new UnsortedArray(9999);

// Add item to unsorted array
for (let i = 0; i <= 9998; i++) {
  unsortedArray.addItem(data[i]);
}

for (let i = 0; i <= 9998; i++) {
  sortedArray.addItem(i);
}

unsortedArray.removeItem(775);

console.log(sortedArray);
console.log(unsortedArray);
