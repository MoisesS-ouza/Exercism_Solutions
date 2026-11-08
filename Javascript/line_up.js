//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  if (String(number).endsWith('1') && !String(number).endsWith('11')) {
    return `${name}, you are the ${number}st customer we serve today. Thank you!`;
  }
  else if (String(number).endsWith('2') && !String(number).endsWith('12')) {
    return `${name}, you are the ${number}nd customer we serve today. Thank you!`;
  }
  else if (String(number).endsWith('3') && !String(number).endsWith('13')) {
    return `${name}, you are the ${number}rd customer we serve today. Thank you!`;
  }
  else {
    return `${name}, you are the ${number}th customer we serve today. Thank you!`;
  }
};

console.log(format('Mary', 112))