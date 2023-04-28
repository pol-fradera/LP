main :: IO ()

main = do
    contents <- getContents
    let nums = words contents
    let sum = foldl (\x y -> x + read(y):: Int) 0 nums
    print sum
    return()