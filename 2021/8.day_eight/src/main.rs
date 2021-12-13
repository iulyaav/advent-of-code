use std::env;
use std::fs;
use std::collections::HashSet;
use std::collections::HashMap;
use std::iter::FromIterator;


fn sort_and_return(s: String) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    chars.sort();
    return String::from_iter(chars);
}


fn analyse(_input: Vec<String>) -> HashMap<String, i32> {

    let mut hashed_input = HashMap::from([
        (2, Vec::new()),
        (3, Vec::new()),
        (4, Vec::new()),
        (5, Vec::new()),
        (6, Vec::new()),
        (7, Vec::new()),
    ]);
    let mut hashed_output : HashMap<String, i32> = HashMap::new();

    for i in 0.._input.len() {
        let length = _input[i].len();
        let vec_of_chars : Vec<String> = _input[i].to_string().chars().map(|x| x.to_string()).collect();
        let mut set_of_chars : HashSet<String> = HashSet::new();
        for v in vec_of_chars {
            set_of_chars.insert(v);
        }
        hashed_input.entry(length).or_insert(Vec::new()).push(set_of_chars);
    }

    // Determine 1
    let one: String = hashed_input[&2][0].clone().into_iter().map(|i| i.to_string()).collect::<String>();
    hashed_output.insert(sort_and_return(one), 1);

    // Determine 4
    let four: String = hashed_input[&4][0].clone().into_iter().map(|i| i.to_string()).collect::<String>();
    hashed_output.insert(sort_and_return(four), 4);

    // Determine 7
    let seven: String = hashed_input[&3][0].clone().into_iter().map(|i| i.to_string()).collect::<String>();
    hashed_output.insert(sort_and_return(seven), 7);

    // Determine 8
    let eight: String = hashed_input[&7][0].clone().into_iter().map(|i| i.to_string()).collect::<String>();
    hashed_output.insert(sort_and_return(eight), 8);

    let mut three : HashSet<String> = HashSet::new();

    // Identify the 3 digit out of len 5 that has the same digits as len 2
    for example in &hashed_input[&5] {
        if (&hashed_input[&2])[0].difference(&example).collect::<Vec<&String>>().len() == (0 as usize) {
            three = example.clone();
            break;
        }
    }

    // Add 3
    hashed_output.insert(sort_and_return(three.clone().into_iter().map(|i| i.to_string()).collect::<String>()), 3);

    // Compare digit 3 with digit 4 (len=4) and what is common but not part of 1 -> is the middle
    let three_four_common : HashSet<String> = three.intersection(&hashed_input[&4][0]).collect::<Vec<&String>>().into_iter().map(|x| x.to_string()).collect();
    let middle = three_four_common.difference(&hashed_input[&2][0]).collect::<Vec<&String>>();

    // What is not common between digit 3 and 4 is up_left
    let up_left = (&hashed_input[&4][0]).difference(&three).collect::<Vec<&String>>()[0];

    // One of len=5 that has up_left => 5. The other one that is neither 3 nor 5 will be 2
    let mut five : HashSet<String> = HashSet::new();
    for example in &hashed_input[&5] {
        if example.contains(up_left) {
            five = example.clone();
            break;
        }
    }
    hashed_output.insert(sort_and_return(five.clone().into_iter().map(|i| i.to_string()).collect::<String>()), 5);

    let mut two : HashSet<String> = HashSet::new();
    for example in &hashed_input[&5] {
        if example.intersection(&three).collect::<Vec<&String>>().len() != 5 && example.intersection(&five).collect::<Vec<&String>>().len() != 5{
            two = example.clone();
            break;
        }
    }
    hashed_output.insert(sort_and_return(two.clone().into_iter().map(|i| i.to_string()).collect::<String>()), 2);

    // Zero is one of length 6 without the middle
    let mut zero : HashSet<String> = HashSet::new();
    for example in &hashed_input[&6] {
        if !example.contains(middle[0]){
            zero = example.clone();
            break;
        }
    }
    hashed_output.insert(sort_and_return(zero.clone().into_iter().map(|i| i.to_string()).collect::<String>()), 0);

    // 9 is one of length 6 that looks like a five and the extra segment is part of one
    let mut nine : HashSet<String> = HashSet::new();
    let one_vector = hashed_input[&2][0].clone().into_iter().map(|i| i.to_string()).collect::<Vec<String>>();

    for example in &hashed_input[&6] {
        if example.contains(middle[0]) && example.contains(&one_vector[0]) && example.contains(&one_vector[1]){
            nine = example.clone();
            break;
        }
    }
    hashed_output.insert(sort_and_return(nine.clone().into_iter().map(|i| i.to_string()).collect::<String>()), 9);

    // 6 is one of length 6 that is not 0 and not 9
    let mut six : HashSet<String> = HashSet::new();
    for example in &hashed_input[&6] {
        if example.intersection(&zero).collect::<Vec<&String>>().len() != 6 && example.intersection(&nine).collect::<Vec<&String>>().len() != 6{
            six = example.clone();
            break;
        }
    }
    hashed_output.insert(sort_and_return(six.clone().into_iter().map(|i| i.to_string()).collect::<String>()), 6);

    return hashed_output;
} 


fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();

    let unique_lenghts = HashSet::<u32>::from([2, 3, 4, 7]);

    let mut unique_lengths_number :u32 = 0;
    let mut result_b : i32 = 0;
    
    for i in 0..lines.len() {
        let line : Vec<String> = lines[i].split(" | ").map(|x| x.to_string()).collect::<Vec<String>>();
        let output : String = (*line[1]).to_string();
        let output_collection : Vec<String> = output.split(" ").map(|x| x.to_string()).collect();
        let input_collection : Vec<String> = (*line[0]).to_string().split(" ").map(|x| x.to_string()).collect();

        let analysis = analyse(input_collection);
        

        let mut result_sum : i32 = 0;
        let mut index : i32 = 0;
        for elem in output_collection {
            if  unique_lenghts.contains(&(elem.to_string().len() as u32)) {
                unique_lengths_number += 1;
            }

            let digit = analysis[&sort_and_return(elem.to_string())];
            match index {
                0 => result_sum += digit * 1000,
                1 => result_sum += digit * 100,
                2 => result_sum += digit * 10,
                3 => result_sum += digit,
                _ => result_b += 0
            }
            index += 1;
        }
        result_b += result_sum;

    }

    println!("Result A {:?}", unique_lengths_number);
    println!("Result B {:?}", result_b);

}