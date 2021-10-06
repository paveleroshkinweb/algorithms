function updateLeftBorder(found, index, middleGreater, left, right) {
    return found || middleGreater ?  [left, index - 1] : [index + 1, right];
}

function updateRightBorder(found, index, middleGreater, left, right) {
    return found || !middleGreater ? [index + 1, right] : [left, index - 1];
}

function findBorder(arr, n, update) {
    let left = 0;
    let right = arr.length - 1;
    let result = -1;
    while (left <= right) {
        let middle = Math.floor((left + right) / 2);
        let middleGreater = arr[middle] > n;
        if (arr[middle] == n) {
            result = middle;
            [left, right] = update(true, middle, middleGreater, left, right);
        } else {
            [left, right] = update(false, middle, middleGreater, left, right);
        }
    }
    return result;
}

function sortedFrequency(arr, n) {
    const leftBorder = findBorder(arr, n, updateLeftBorder);
    const rightBorder = findBorder(arr, n, updateRightBorder);
    if (leftBorder == -1) {
        return -1;
    }
    return rightBorder - leftBorder + 1;
}