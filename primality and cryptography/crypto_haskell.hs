--THIS IS A WORK IN PROGRESS
chars = ' ':['A'..'Z']++['a'..'z'] ++ ['.',',','!','?']
digits = [1..length chars]
codeMap = zip chars digits --(char,number)

getNum c = snd ([(a,b) | (a,b) <- codeMap, a == c] !! 0)
getLet n = fst ([(a,b) | (a,b) <- codeMap, b == n] !! 0)

encode :: String -> [Int]
encode [] = []
encode (x:rest) = (getNum x): (encode rest)

encrypt :: (Integral a) => [a] -> a -> a -> [a]
encrypt [] e n = []
encrypt (x:rest) e n = (x^e `mod` n):(encrypt rest e n)

                 



