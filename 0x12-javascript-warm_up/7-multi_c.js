#!/usr/bin/node

const num = process.argv[2];
if (isNaN(num)) {
	console.log('Missing number of occurrences');
} else {
	count = Number(num);
	for (let i = 0; i < count; i++) {
		console.log('C is fun');
	}
}
