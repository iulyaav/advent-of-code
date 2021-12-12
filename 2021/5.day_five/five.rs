use std::env;
use std::fs;
use std::collections::HashMap;
// use std::iter;


fn create_point(x:i32, y:i32) -> String {
    return format!("{}:{}", x, y);
}


fn draw_line(x1:i32, y1:i32, x2:i32, y2: i32) -> Vec<String>{
    let mut points: Vec<String> = Vec::new();
    if x1 == x2 && y1 <= y2 {
        for i in y1..y2+1 {
            points.push(create_point(x1, i));
        }   
    } else if x1 == x2 && y1 > y2 {
        for i in y2..y1+1 {
            points.push(create_point(x1, i));
        } 
    } else if y1 == y2 && x1 <= x2 {
        for i in x1..x2+1 {
            points.push(create_point(i, y1));
        }  
    } else if y1 == y2 && x1 > x2 {
        for i in x2..x1+1 {
            points.push(create_point(i, y1));
        } 
    } else if (x1-x2).abs() == (y1-y2).abs() {
        let dif :i32 = (x1-x2).abs();
        for i in 0..dif+1 {
            let mut x : i32 = 0;
            let mut y : i32 = 0;
            if x1 < x2 {
                x = x1 + i;
            } else {
                x = x1 - i;
            }

            if y1 < y2 {
                y = y1 + i;
            } else {
                y = y1 - i;
            }
            points.push(create_point(x, y));

        }
    }
    return points;
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];
    println!("Opening file {}", filename);

    let lines: Vec<String> = fs::read_to_string(filename).unwrap().lines().map(|line| line.to_string()).collect();

    let mut points :HashMap<String, i32> = HashMap::new();
    
    let mut two_or_more : i32 = 0;

    for i in 0..lines.len() {
        let coordinates: Vec<String> = lines[i].split(" -> ").filter(|&x| !x.is_empty()).map(|x| x.to_string()).collect();
        let start: Vec<i32> = coordinates[0].split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        let end: Vec<i32> = coordinates[1].split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        let result = draw_line(start[0], start[1], end[0], end[1]);

        for res in result {
            let mut val : i32 = 0;
            match points.get_mut(&res) {
                Some(v) => {val = *v + 1;},
                None => val = 1
            };
            points.insert(res, val);
        }
    }

    for (key, value) in points.into_iter() {
        if value >= 2 {
            two_or_more += 1;
        }
    }

    println!("Result {:?}", two_or_more);
}