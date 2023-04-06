multEq :: Int -> Int -> [Int]
multEq x y = iterate ((*x) . (*y)) 1

-- selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
-- selectFirst [] _ _ = []
-- selectFirst _ [] _ = []

myIterate :: (a -> a) -> a -> [a]
myIterate f n = scanl (\x _ -> f x)  n [1..]  -- x es el que es el valor intermig 
                                              -- _ es el valor de la llista [1..]
