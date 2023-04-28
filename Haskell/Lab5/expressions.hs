data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1 :: Expr -> Int
eval1 (Val a) = a 
eval1 (Add exp1 exp2) = (eval1 exp1) + (eval1 exp2)
eval1 (Sub exp1 exp2) = (eval1 exp1) - (eval1 exp2)
eval1 (Mul exp1 exp2) = (eval1 exp1) * (eval1 exp2)
eval1 (Div exp1 exp2) = (eval1 exp1) `div` (eval1 exp2)

eval2 :: Expr -> Maybe Int
eval2 (Val a) = Just a 
eval2 (Add exp1 exp2) = do
    a <- (eval2 exp1) -- amb la fletxa es retorna el valor sense encapsular
    b <- (eval2 exp2)
    return (a + b)   -- es retorna el valor encapsulat (Just en maybe)
eval2 (Sub exp1 exp2) = do
    a <- (eval2 exp1) 
    b <- (eval2 exp2)
    return (a - b)
eval2 (Mul exp1 exp2) = do
    a <- (eval2 exp1) 
    b <- (eval2 exp2)
    return (a*b)
eval2 (Div exp1 exp2) =  do
    a <- (eval2 exp1) 
    b <- (eval2 exp2)
    if (b == 0) then Nothing
    else return (a `div` b)

eval3 :: Expr -> Either String Int
eval3 (Val a) = Right a 
eval3 (Add exp1 exp2) = do
    a <- (eval3 exp1) -- amb la fletxa es retorna el valor sense encapsular
    b <- (eval3 exp2)
    return (a + b)   -- es retorna el valor encapsulat (Right en maybe)
eval3 (Sub exp1 exp2) = do
    a <- (eval3 exp1) 
    b <- (eval3 exp2)
    return (a - b)
eval3 (Mul exp1 exp2) = do
    a <- (eval3 exp1) 
    b <- (eval3 exp2)
    return (a*b)
eval3 (Div exp1 exp2) =  do
    a <- (eval3 exp1) 
    b <- (eval3 exp2)
    if (b == 0) then Left "div0"
    else return (a `div` b)