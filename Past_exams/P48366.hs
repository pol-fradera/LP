eval1 :: String -> Int
eval1 l = eval1' (words l) []

eval1' :: [String] -> [Int] -> Int
eval1' [] (y:p) = y
eval1' ("+":l) (e1:e2:pila) = eval1' l ((e2+e1):pila)
eval1' ("-":l) (e1:e2:pila) = eval1' l ((e2-e1):pila)
eval1' ("*":l) (e1:e2:pila) = eval1' l ((e2*e1):pila)
eval1' ("/":l) (e1:e2:pila) = eval1' l ((div e2 e1):pila)
eval1' (x:l) pila = eval1' l (z:pila)
        where 
            z = read (x):: Int
         

eval2 :: String -> Int
eval2 str                               = head (foldl res [] (words str))
    where
        res :: [Int] -> String -> [Int]
        res (x1:x2:next) "+"            = (x2+x1):next
        res (x1:x2:next) "-"            = (x2-x1):next
        res (x1:x2:next) "*"            = (x2*x1):next
        res (x1:x2:next) "/"            = (div x2 x1):next
        res next x                      = (read x):next


fsmap :: a -> [a -> a] -> a
fsmap x [] = x
fsmap x (f:fs) = fsmap (f x) fs


-- divideNconquer :: (a -> Maybe b) -> (a -> (a, a)) -> (a -> (a, a) -> (b, b) -> b) -> a -> b
-- divideNconquer base divide conquer x

-- base :: (a -> Maybe b) 
-- base


data Racional = Racional Integer Integer

racional :: Integer -> Integer -> Racional
racional num den = Racional (div num mcd) (div den mcd)
    where
        mcd = gcd num den

numerador :: Racional -> Integer
numerador (Racional num den) = div num mcd
    where
        mcd = gcd num den

denominador :: Racional -> Integer
denominador (Racional num den) = div den mcd
    where
        mcd = gcd num den

instance Show Racional
    where
        show (Racional num dev) = show num ++ "/" ++ show dev

instance Eq Racional
    where
        (Racional num1 dev1) == (Racional num2 dev2) = (num1 == num2) && (dev1 == dev2)