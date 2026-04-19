function celsiusToFahrenheit(c) {
  return (c * 9/5) + 32;
}

function fahrenheitToCelsius(f) {
  return (f - 32) * 5/9;
}

console.log(`60°C is ${celsiusToFahrenheit(60)}°F`);
console.log(`45°F is ${fahrenheitToCelsius(45)}°C`);