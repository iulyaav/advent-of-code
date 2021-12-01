use std::env;
use std::fs;
use std::collections::VecDeque;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let split = contents.split("\n");
    let mut first : bool = true;

    let mut previous_single: Option<i32> = None;
    let mut increase = 0;

    let split2 = split.clone();
    // First problem
    for (_, element) in split.enumerate() {
        if first {
            previous_single = Some(element.parse().unwrap());
            first = false;
            continue;
        } else {
            if previous_single != None && previous_single < Some(element.parse().unwrap()) {
                increase += 1;
                // println!("Previous: {:?}, Current {:?}", previous, element)
            }
        }
        previous_single = Some(element.parse().unwrap());
        
    }

    let mut little_sum = 0;
    let mut sum_increase = 0;
    let mut previous_sum: Option<i32> = None;
    let mut vector: VecDeque<i32> = VecDeque::new();
    
    //Second problem
    for (i, element) in split2.enumerate() {

        let num: i32 = element.parse().unwrap();

        if i < 2 {
            vector.push_back(num);
        } else {
            if i >= 3 {
                vector.pop_front();
            }
            vector.push_back(num);
            little_sum = vector.iter().sum();
            if previous_sum != None && previous_sum < Some(little_sum) {
                sum_increase += 1;
            }
            previous_sum = Some(little_sum);

        }
    }

    println!("First answer: {}", increase);
    println!("Second answer: {}", sum_increase);
}