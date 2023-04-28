myMap :: (a -> b) -> [a] -> [b]
myMap f xs = [q | x <- xs, let q = f x]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f xs = [x | x <- xs, f x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = [q | (x,y) <- zip xs ys, let q = f x y]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify xs ys = [(x,y) | x <- xs, y <- ys, x `mod` y == 0]

factors :: Int -> [Int]
factors y = [x | x <- [1..y], y `mod` x == 0]