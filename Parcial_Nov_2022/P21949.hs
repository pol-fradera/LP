hanoi :: Int -> String -> String -> String -> IO()
hanoi 0 _ _ _ = do
    --putStrLn (ori ++ " -> " ++ dest)
    return()
hanoi n ori dest aux = do
    hanoi (n-1) ori aux dest
    putStrLn (ori ++ " -> " ++ dest)
    hanoi (n-1) aux dest ori


main :: IO ()
main = do
    line <- getLine
    let paraules = words line
    let nombre = read(head paraules) :: Int
    let origen = paraules !! 1
    let desti = paraules !! 2
    let auxiliar = paraules !! 3
    hanoi nombre origen desti auxiliar