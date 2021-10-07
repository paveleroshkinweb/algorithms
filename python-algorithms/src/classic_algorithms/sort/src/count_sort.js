function countSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }
    const maxElement = Math.max(...arr);
    const countMap = {};
    for (let element of arr) {
        countMap[element] = (countMap[element] || 0) + 1
    }
    let resultArray = [];
    for (let i = 1; i < maxElement; i++) {
        if (i in countMap) {
            for (let j = 0; j < countMap[i]; j++) {
                resultArray.push(i);
            }
        }
    }
    return resultArray;
}
