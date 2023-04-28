main :: IO ()

imc :: Float -> Float -> Float
imc m h = m / d
    where d = h*h

main = do
    line <- getLine
    if line /= "*" then do
        let paraules = words line
        let nom = head paraules
        let m = read $ head $ tail paraules :: Float
        let h = read $ last paraules :: Float
        let r = imc m h
        putStr $ nom ++ ": "
        if r < 18 then do
            putStrLn "magror"
        else if r < 25 then do
            putStrLn "corpulencia normal"
        else if r < 30 then do
            putStrLn "sobrepes"
        else if r < 40 then do
            putStrLn "obesitat"
        else putStrLn "obesitat morbida"
        main
    else 
        return ()