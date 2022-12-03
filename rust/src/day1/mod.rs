fn parse_data(input_data: String) -> Vec<i32> {
    input_data
        .split("\n\n")
        .into_iter()
        .map(|lines| lines.lines().map(|num| num.parse::<i32>().unwrap()).sum())
        .collect()
}

fn part1(input_data: String) -> i32 {
    parse_data(input_data).into_iter().max().unwrap()
}

fn part2(input_data: String) -> i32 {
    let mut nums = parse_data(input_data);
    nums.sort();
    nums.reverse();
    nums[..3].into_iter().sum()
}

#[cfg(test)]
mod tests {
    use crate::day1::{part1, part2};
    use crate::test_lib::tests;

    tests! {
        part1_real: part1 -> (include_str!("input"), 67633),
        part2_real: part2 -> (include_str!("input"), 199628),
    }
}
