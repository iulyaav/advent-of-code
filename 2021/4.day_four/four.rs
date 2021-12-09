use std::env;
use std::fs;
use std::iter;

#[derive(Debug)]
struct BingoBox {
    rows: Vec<Vec<String>>
}

impl BingoBox {
    fn mark(&mut self, x: String) {
        for i in 0..5 {
            for j in 0..5 {
                if self.rows[i][j].to_string() == x {
                    self.rows[i][j] = String::from("");
                }
            }
        }
    }

    fn sum(&self) ->i32 {

        let mut total_sum : i32 = 0;
        for i in 0..5 {
            for j in 0..5 {
                if self.rows[i][j].to_string() != "" {
                    let num :i32 = self.rows[i][j].parse().unwrap();
                    total_sum += num;
                }
                
            }
        }
        return total_sum;

    }

    fn check(&self) -> bool {
        for i in 0..5 {
            // check rows
            let mut bingo : bool = true;
            for j in 0..5 {
                if self.rows[i][j].to_string() != "" {
                    bingo = false;
                }
            }
            if bingo {
                return true;
            }

            bingo = true;
            // check columns
            for j in 0..5 {
                if self.rows[j][i].to_string() != "" {
                    bingo = false;
                }
            }

            if bingo {
                return true;
            }

        }
        return false;
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();

    let numbers: Vec<&str> = lines[0].split(',').collect();
    let mut bingo_boxes : Vec<BingoBox> = Vec::new();
    let mut new_box : BingoBox = BingoBox{rows:Vec::new()};

    for i in 2..lines.len() {

        let line = &lines[i];
        if line == "" {
            bingo_boxes.push(new_box);
            new_box = BingoBox{rows:Vec::new()};
        } else if i == lines.len() - 1 {
            let row: Vec<String> = line.split(' ').filter(|&x| !x.is_empty()).map(|x| x.to_string()).collect();
            new_box.rows.push(row);
            bingo_boxes.push(new_box);
            new_box = BingoBox{rows:Vec::new()};
        } else {
            let row: Vec<String> = line.split(' ').filter(|&x| !x.is_empty()).map(|x| x.to_string()).collect();
            new_box.rows.push(row);
        }
    }

    let mut did_i_win : Vec<u32> = iter::repeat(0).take(lines[0].len()).collect();

    for number in numbers {
        for i in 0..bingo_boxes.len() {
            if did_i_win[i] == 1 {
                // println!("Ignoring {:?}", i);
                continue;
            }
            bingo_boxes[i].mark(number.to_string());
            let result : bool = bingo_boxes[i].check();
            if result {
                let mut x :i32 = bingo_boxes[i].sum();
                x = x * number.parse::<i32>().unwrap();
                println!("Result: {:?} in box {:?} after finding {:?}", x, i, number);
                did_i_win[i] = 1;
            }
        }
    }
}