fn part1(input_data: String) {

}

fn part2(input_data: String) {
    
}

#[cfg(test)]
mod tests {
    use crate::template::{part1, part2};
    use crate::test_lib::tests;


    tests! {
        part1_real: part1 -> (include_str!("input"), 0),
        part2_real: part2 -> (include_str!("input"), 0),
    }
}