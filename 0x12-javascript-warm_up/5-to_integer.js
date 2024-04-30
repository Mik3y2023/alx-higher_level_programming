
#!/usr/bin/node
// script that prints My number: <first argument converted to int>

const argument = process.argv[2];

if (!isNaN(argument)) {
  const number = parseInt(argument);
  if (!isNaN(number)) {
    console.log(`My number: ${number}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
