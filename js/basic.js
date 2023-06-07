console.log("##### STDOUT #####");
console.log('Hello World');


console.log("##### AND/OR #####");
console.log(true && false);  // >>> false
console.log(true || false);  // >>> true
console.log(true && !true);  // >>> false
console.log(true || !true);  // >>> true


console.log("##### ARRAY #####");
languages = ["hoge", "fuga", "piyo"];
console.log(languages[1]);


console.log("##### HASH #####");
dicts = { "a": "hoge", "b": "fuga", "c": "piyo" };
console.log(dicts["a"]);
console.log(dicts.b);


console.log("##### LOOPING #####");
for (let i = 0; i < 5; i++) {
  console.log("Hello world");
}
