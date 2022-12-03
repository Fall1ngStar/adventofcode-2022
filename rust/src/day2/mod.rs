#[derive(Copy, Clone)]
enum Move {
    ROCK,
    PAPER,
    SCISORS,
}

enum Ending {
    WIN,
    DRAW,
    LOSE,
} 

impl Ending {
    fn from(letter: char) -> Self {
        match letter {
            'X' => Ending::LOSE,
            'Y' => Ending::DRAW,
            'Z' => Ending::WIN,
            _ => panic!("Invalid ending")
        }
    }
}

impl Move {
    fn from(letter: char) -> Self {
        match letter {
            'A' | 'X' => Move::ROCK,
            'B' | 'Y' => Move::PAPER,
            'C' | 'Z' => Move::SCISORS,
            _ => panic!("Invalid move"),
        }
    }

    fn pick_score(&self) -> i32 {
        match self {
            Move::ROCK => 1,
            Move::PAPER => 2,
            Move::SCISORS => 3,
        }
    }

    fn match_score(&self, against: Move) -> i32 {
        match self {
            Move::ROCK => match against {
                Move::ROCK => 3,
                Move::PAPER => 0,
                Move::SCISORS => 6,
            },
            Move::PAPER => match against {
                Move::ROCK => 6,
                Move::PAPER => 3,
                Move::SCISORS => 0,
            },
            Move::SCISORS => match against {
                Move::ROCK => 0,
                Move::PAPER => 6,
                Move::SCISORS => 3,
            },
        }
    }

    fn for_ending(&self, ending: Ending) -> Self {
        match self {
            Move::ROCK => match ending {
                Ending::WIN=> Move::PAPER,
                Ending::DRAW => Move::ROCK,
                Ending::LOSE => Move::SCISORS,
            },
            Move::PAPER => match ending {
                Ending::WIN => Move::SCISORS,
                Ending::DRAW => Move::PAPER,
                Ending::LOSE => Move::ROCK,
            },
            Move::SCISORS => match ending {
                Ending::WIN=> Move::ROCK,
                Ending::DRAW => Move::SCISORS,
                Ending::LOSE=> Move::PAPER,
            },
        }
    }
}

fn part1(input_data: String) -> i32 {
    input_data
        .lines()
        .into_iter()
        .map(|line| line.chars())
        .map(|mut chars| {
            let he = chars.nth(0).unwrap();
            let me = chars.nth(1).unwrap();
            (
                Move::from(he),
                Move::from(me),
            )
        })
        .map(|(he, me)| me.pick_score() + me.match_score(he))
        .sum()
}

fn part2(input_data: String) -> i32 {
    input_data
        .lines()
        .into_iter()
        .map(|line| line.chars())
        .map(|mut chars| {
            let he = chars.nth(0).unwrap();
            let target = chars.nth(1).unwrap();
            (
                Move::from(he),
                Ending::from(target),
            )
        })
        .map(|(he, target)| (he, he.for_ending(target)))
        .map(|(he, me)| me.pick_score() + me.match_score(he))
        .map(|score| {println!("score {:}", score); score})
        .sum()
}

#[cfg(test)]
mod tests {
    use crate::day2::{part1, part2};
    use crate::test_lib::tests;

    tests! {
        part1_real: part1 -> (include_str!("input"), 12276),
        part2_real: part2 -> (include_str!("input"), 9975),
    }
}
