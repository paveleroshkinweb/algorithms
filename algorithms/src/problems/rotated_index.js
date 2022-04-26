function findMiddle(arr) {
    let pivot = arr[0];
    let left = 0;
    let right = arr.length - 1;
    let result = -1;
    while (left <= right) {
        let middle = Math.floor((left + right) / 2);
        if (arr[middle] > pivot) {
            left = middle + 1;
        } else {
            result = middle;
            right = middle - 1;
        }
    }
    return result;
}


function binarySearch(arr, number) {
    let left = 0;
    let right = arr.length - 1;
    while (left <= right) {
        let middle = Math.floor((left + right) / 2)
        if (arr[middle] == number) {
            return middle;
        } else if (arr[middle] > number) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return -1;
}


function findRotatedIndex(arr, number) {
    if (arr.length == 0) {
        return -1;
    }
    let middle = findMiddle(arr);
    if (middle != -1) {
        if (number > arr[0]) {
            let leftArray = arr.slice(0, middle);
            let index = binarySearch(leftArray, number);
            return index;
        } else {
            let rightArray = arr.slice(middle);
            let index = binarySearch(rightArray, number);
            if (index != -1) {
                return index + middle;
            }
            return index;
        }
    }
    return binarySearch(arr, number);
}