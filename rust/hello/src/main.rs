fn main() {
    let i: i32 = 4;
    println!("{}", twice(i));
}

fn twice(x: i32) -> i32 {
    let x2: i32 = x * 2;
    return x2;
}
