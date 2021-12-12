use std::env;
use std::fs;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();

    let mut fishes: HashMap<i64, i64> = HashMap::new();

    for i in 0..9 {
        fishes.insert(i, 0);
    }

    let mut initial_input: Vec<i64> = lines[0].split(",").map(|x| x.parse::<i64>().unwrap()).collect();

    for i in 0..initial_input.len() {
        println!("{:?}", initial_input[i]);
        *fishes.get_mut(&initial_input[i]).unwrap() += 1;
    }

    println!("Initial state: {:?}", fishes);

    for i in 0..256 {
        let mut new_fishes: HashMap<i64, i64> = HashMap::new();
        for i in 0..9 {
            let key : i64 = i;
            if key == 0 {
                *new_fishes.entry(8).or_insert(0) += fishes[&key];
                *new_fishes.entry(6).or_insert(0) += fishes[&key];
            } else {
                *new_fishes.entry(i - 1).or_insert(0) += fishes[&key];
            }

        }    
        fishes = new_fishes;
    }

    println!("Final state: {:?}", fishes);

    let mut result :i64 = 0;
    for (_, value) in fishes.into_iter() {
        result += value;
    }
    
    println!("Result {:?}", result);
}