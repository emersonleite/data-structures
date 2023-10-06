export function getTime(entryfunction: (data: any) => any, data: any) {
  performance.mark("marker-a");

  entryfunction(data);

  performance.mark("marker-b");

  performance.measure("A to B", "marker-a", "marker-b");

  let { duration } = performance.getEntriesByType("measure")[0];

  performance.clearMarks();

  performance.clearMeasures();

  return duration;
}

export function getData(dataLen: number) {
  let numberList: number[] = [];

  while (numberList.length < dataLen) {
    let randomNumber = Math.round(Math.random() * dataLen + 1) - 1;

    if (numberList.indexOf(randomNumber) === -1) {
      numberList.push(randomNumber);
    }
  }

  return numberList;
}

/* console.log(getData(99), getData(99).indexOf(85));

console.log(getTime(getData, 99998)); */
