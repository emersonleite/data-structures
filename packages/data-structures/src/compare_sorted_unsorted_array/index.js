"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const generateData_1 = require("../generateData");
const sortedArray_1 = require("../sorted_array/sortedArray");
const unsortedArray_1 = require("../unsorted_array/unsortedArray");
let data = (0, generateData_1.getData)(9999);
let sortedArray = new sortedArray_1.SortedArray(9999);
let unsortedArray = new unsortedArray_1.UnsortedArray(9999);
// Add item to unsorted array
for (let i = 0; i <= 9998; i++) {
    unsortedArray.addItem(data[i]);
}
for (let i = 0; i <= 9998; i++) {
    sortedArray.addItem(i);
}
//# sourceMappingURL=index.js.map