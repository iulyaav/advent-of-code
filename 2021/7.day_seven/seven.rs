use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();
    let crabs: Vec<i32> = lines[0].split(",").map(|x| x.parse::<i32>().unwrap()).collect();

    let max : i32 = *crabs.iter().max().unwrap();
    let mut result = i32::MAX;
    let mut fuel :i32 = 0;

    for i in 0..(max+1) {
        fuel = 0;
        for crab in &crabs {
            let dif = (crab - i).abs();
            fuel += (dif * (dif+1)) / 2;
        }
        if fuel < result {
            result = fuel;
        }
    }

    println!("Result {:?}", result)

}