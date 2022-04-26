function countZeroes(arr) {
    let left = 0;
    let right = arr.length - 1;
    let zeroIndex = -1;
    while (left <= right) {
        let middle = Math.floor((left + right) / 2);
        if (arr[middle] == 0) {
            zeroIndex = middle;
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return zeroIndex == -1 ? 0 : arr.length - zeroIndex;
}