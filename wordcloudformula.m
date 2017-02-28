(* 生成一个包含许多物理化学经济学公式的词云 *)
eqn = Flatten[FormulaData /@ (FormulaData[][[10 ;; 18]])];
eqn = DeleteCases[eqn /. QuantityVariable[a_, _] -> a, False];
input = N@Sqrt@LeafCount[#] -> # & /@ eqn;
WordCloud[input, WordSpacings -> {40, 15}, 
 WordOrientation -> "Horizontal"]
