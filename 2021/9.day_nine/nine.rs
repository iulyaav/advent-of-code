use std::env;
use std::fs;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();

    let map : Vec<Vec<u32>> = Vec::new();
    
    for i in 0..lines.len() {
        let line : Vec<u32> = lines[i].chars().map(|x| x.parse::<u32>().unwrap()).collect();
    }

    println!("{:?}", map);
}