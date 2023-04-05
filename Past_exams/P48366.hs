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
         
fsmap :: a -> [a -> a] -> a
fsmap x [] = x
fsmap x (f:fs) = fsmap (f x) fs

-- data Racional = (Integer "/" Integer) deriving (Show) deriving (Eq)

-- racional :: Integer -> Integer -> Racional
-- racional num den = show num ++ "/" ++ show den 


-- numerador :: Racional -> Integer
-- denominador :: Racional -> Integer