import tokenizer
import stores

tknzr1 = tokenizer.Tokenizer()

tokens = tknzr1.tokenizeStatement(['LSL', 'V1'], 20)


store1 = stores.SymbolStore()
store2 = stores.LabelStore()

store1.setSymbol("V1", 30, 50)
store2.setLabel("LOOP", 10)

[[print(t, end=" ") for t in tokens[i]] for i in range(2)]