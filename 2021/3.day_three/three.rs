use std::env;
use std::fs;
use std::iter;
use std::collections::HashSet;

fn A(capacity: usize, lines: &Vec<String>) {
    let total = lines.len();
    let mut positions: Vec<u32> = iter::repeat(0).take(lines[0].len()).collect();
    for line in lines {
        for i in 0..line.len() {
            positions[i] = positions[i] + line.chars().nth(i).unwrap().to_digit(10).unwrap();
        }
    }
    let mut gamma: String = String::new();
    let mut epsilon: String = String::new();
    
    for i in 0..positions.len() {
        if positions[i] >= (total / 2) as u32 {
            gamma += "1";
            epsilon += "0";
        } else {
            gamma += "0";
            epsilon += "1";
        }
    } 

    let gamma_int = isize::from_str_radix(&gamma, 2).unwrap();
    let epsilon_int = isize::from_str_radix(&epsilon, 2).unwrap();
    
    println!("Result A: {}", gamma_int * epsilon_int);
}

fn solve_B(lines: &Vec<String>, inverse: bool) -> isize {
    let mut ignore_list : HashSet<String> = HashSet::new();
    let capacity = lines[0].len();
    let total = lines.len();
    for i in 0..capacity {
        let mut ones : usize = 0;
        let mut zeroes : usize = 0;

        if ignore_list.len() >= (total - 1) {
            break;
        }

        for line in lines {
            if !ignore_list.contains(line) && line.chars().nth(i).unwrap() == '1' {
                ones += 1;
            } else if !ignore_list.contains(line) && line.chars().nth(i).unwrap().to_string() == "0" {
                zeroes += 1
            }
        }

        println!("Zeroes {:?} Ones {:?}", zeroes, ones);

        let mut look_for : String = String::from("0");

        if inverse {
            if zeroes <= ones {
                look_for = "0".to_string();
            }
            else {
                look_for = "1".to_string();
            }

        } else {
            if ones >= zeroes {
                look_for = "1".to_string();
            } else {
                look_for = "0".to_string();
            }
        }

        let mut ignored_now: Vec<String> = vec![];
        for line in lines {
            if !ignore_list.contains(line) && line.chars().nth(i).unwrap().to_string() != look_for {
                ignore_list.insert(line.to_string());
                println!("Ignoring {:?}", line);
            }
        }
    }

    let mut rating : String = String::new();

    for line in lines {
        if !ignore_list.contains(line) {
            rating = line.to_string();
        }
    }

    return isize::from_str_radix(&rating, 2).unwrap();

}

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();
    let copy_lines = lines.clone();
    let capacity = lines[0].len();
    
    let total = lines.len();
    A(capacity, &lines);


    let oxygen = solve_B(&lines, false);
    let co2 = solve_B(&lines, true);
    println!("oxygen = {:?}, co2 = {:?}, answer for B = {:?}", oxygen, co2, (oxygen * co2));
    

}