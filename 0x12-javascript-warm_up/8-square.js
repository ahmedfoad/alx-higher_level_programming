#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const count = parseInt(process.argv[2]);
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
} else {
  console.log('Missing size');
}

