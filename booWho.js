function booWho(bool) {
  return typeof bool === "boolean";
}

console.log(booWho(null));
console.log(booWho(false));
console.log(booWho({ a: 1 }));
