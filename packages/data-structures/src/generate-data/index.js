"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getData = exports.getTime = void 0;
function getTime(entryfunction, data) {
    performance.mark("marker-a");
    entryfunction(data);
    performance.mark("marker-b");
    performance.measure("A to B", "marker-a", "marker-b");
    let { duration } = performance.getEntriesByType("measure")[0];
    performance.clearMarks();
    performance.clearMeasures();
    return duration;
}
exports.getTime = getTime;
function getData(dataLen) {
    let numberList = [];
    while (numberList.length < dataLen) {
        let randomNumber = Math.round(Math.random() * dataLen + 1) - 1;
        if (numberList.indexOf(randomNumber) === -1) {
            numberList.push(randomNumber);
        }
    }
    return numberList;
}
exports.getData = getData;
console.log(getData(99), getData(99).indexOf(85));
console.log(getTime(getData, 99998));
//# sourceMappingURL=index.js.map