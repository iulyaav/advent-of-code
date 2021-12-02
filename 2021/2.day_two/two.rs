use std::env;
use std::fs;
use std::collections::VecDeque;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut horizontal: i32 = 0;
    let mut depth: i32 = 0;
    let mut aim: i32 = 0;
    
    for line in contents.lines() {
        let vec: Vec<&str> = line.split(' ').collect();
        let command : String = vec[0].to_string();
        let value : i32 = vec[1].parse().unwrap();

        if command.eq("forward") {
            horizontal += value;
            depth += (aim * value);
        } else if command.eq("up") {
            aim -= value;
        } else if command.eq("down") {
            aim += value;
        }
        
    }

    println!("Result: {}", horizontal * depth);
}