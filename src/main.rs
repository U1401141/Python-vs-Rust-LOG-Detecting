use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::time::Instant;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        println!("Usage: cargo run -- release -- <filename> <keyword>");
        return Ok(());
    }

    let path = &args[1];
    let keyword = &args[2];

    let start_time = Instant::now();

    // Open the file
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut total = 0;

    // Iterate through lines
    for line in reader.lines() {
        let line = line?;
        if line.contains(keyword) {
            total += 1;
        }
    }

    let duration = start_time.elapsed();
    let total_second = duration.as_secs_f64();

    println!("The amount of '{}': {}", keyword, total);
    println!("{} seconds to find all items", total_second);

    Ok(())
}
