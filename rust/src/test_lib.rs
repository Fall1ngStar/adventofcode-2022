#[cfg(test)]
macro_rules! tests {
    ($($name:ident: $func:tt -> $value:expr,)*) => {
    $(
        #[test]
        fn $name() {
            let (input, expected) = $value;
            assert_eq!(expected, $func(String::from(input)));
        }
    )*
    }
}

#[cfg(test)]
pub(crate) use tests;
