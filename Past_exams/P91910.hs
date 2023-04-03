multEq :: Int -> Int -> [Int]
multEq x y = iterate ((*x) . (*y)) 1

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
  