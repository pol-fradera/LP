main :: IO ()

main = do
    nom <- getLine
    let x = last nom
    if (x == 'a' || x == 'A') then do
        putStrLn "Hola maca!"
    else
        putStrLn "Hola maco!"
    