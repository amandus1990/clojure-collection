(* Differential and integral operation trainer *)
ListRandomPlus[SeedList_] := 
 Module[{pick = {1, 2}, resoperate = {}, reslist = {}, 
   numberstringlength = 7, numberrange = 1000}, 
  If[Length[SeedList] > 1, 
   pick = RandomSample[Range[Length[SeedList]], 2];
   resoperate = Plus[SeedList[[pick[[1]]]], SeedList[[pick[[2]]]]];
   resoperate = Simplify[resoperate];
   If[NumberQ[resoperate] && 
     StringLength[ToString[resoperate]] > numberstringlength, 
    resoperate = RandomInteger[{-numberrange, numberrange}]];
   reslist = Delete[SeedList, {{pick[[1]]}, {pick[[2]]}}];
   AppendTo[reslist, resoperate], SeedList]]
ListRandomSubtract[SeedList_] := 
 Module[{pick = {1, 2}, resoperate = {}, reslist = {}, 
   numberstringlength = 7, numberrange = 1000}, 
  If[Length[SeedList] > 1, 
   pick = RandomSample[Range[Length[SeedList]], 2];
   resoperate = Subtract[SeedList[[pick[[1]]]], SeedList[[pick[[2]]]]];
   resoperate = Simplify[resoperate];
   If[NumberQ[resoperate] && 
     StringLength[ToString[resoperate]] > numberstringlength, 
    resoperate = RandomInteger[{-numberrange, numberrange}]];
   reslist = Delete[SeedList, {{pick[[1]]}, {pick[[2]]}}];
   AppendTo[reslist, resoperate], SeedList]]
ListRandomTimes[SeedList_] := 
 Module[{pick = {1, 2}, resoperate = {}, reslist = {}, 
   numberstringlength = 7, numberrange = 1000}, 
  If[Length[SeedList] > 1, 
   pick = RandomSample[Range[Length[SeedList]], 2];
   resoperate = Times[SeedList[[pick[[1]]]], SeedList[[pick[[2]]]]];
   resoperate = Simplify[resoperate];
   If[NumberQ[resoperate] && 
     StringLength[ToString[resoperate]] > numberstringlength, 
    resoperate = RandomInteger[{-numberrange, numberrange}]];
   reslist = Delete[SeedList, {{pick[[1]]}, {pick[[2]]}}];
   AppendTo[reslist, resoperate], SeedList]]
ListRandomDivide[SeedList_] := 
 Module[{pick = {1, 2}, resoperate = {}, reslist = {}, 
   numberstringlength = 7, numberrange = 1000}, 
  If[Length[SeedList] > 1, 
   pick = RandomSample[Range[Length[SeedList]], 2];
   If[NumberQ[SeedList[[pick[[2]]]]], 
    If[SeedList[[pick[[2]]]] == 0, Return[SeedList]]];
   resoperate = Divide[SeedList[[pick[[1]]]], SeedList[[pick[[2]]]]];
   resoperate = Simplify[resoperate];
   If[NumberQ[resoperate] && 
     StringLength[ToString[resoperate]] > numberstringlength, 
    resoperate = RandomInteger[{-numberrange, numberrange}]];
   reslist = Delete[SeedList, {{pick[[1]]}, {pick[[2]]}}];
   AppendTo[reslist, resoperate], SeedList]]
ListRandomPower[SeedList_] := 
 Module[{pick = {1, 2}, resoperate = {}, reslist = {}, 
   numberstringlength = 7, numberrange = 1000}, 
  If[Length[SeedList] > 1, 
   pick = RandomSample[Range[Length[SeedList]], 2];
   If[(NumberQ[SeedList[[pick[[1]]]]] && 
       SeedList[[pick[[1]]]] <= 0) || (NumberQ[
        SeedList[[pick[[2]]]]] && SeedList[[pick[[2]]]] > 3), 
    Return[SeedList]];
   resoperate = Power[SeedList[[pick[[1]]]], SeedList[[pick[[2]]]]];
   resoperate = Simplify[resoperate];
   If[NumberQ[resoperate] && 
     StringLength[ToString[resoperate]] > numberstringlength, 
    resoperate = RandomInteger[{-numberrange, numberrange}]];
   reslist = Delete[SeedList, {{pick[[1]]}, {pick[[2]]}}];
   AppendTo[reslist, resoperate], Return[SeedList]]]
ListRandomLog[SeedList_] := 
 Module[{pick = {1, 2}, resoperate = {}, reslist = {}, 
   numberstringlength = 7, numberrange = 1000}, 
  If[Length[SeedList] > 1, 
   pick = RandomSample[Range[Length[SeedList]], 2];
   If[(NumberQ[SeedList[[pick[[1]]]]] && 
       SeedList[[pick[[1]]]] <= 0) || (NumberQ[
        SeedList[[pick[[2]]]]] && SeedList[[pick[[2]]]] <= 0), 
    Return[SeedList]];
   resoperate = Log[SeedList[[pick[[1]]]], SeedList[[pick[[2]]]]];
   resoperate = Simplify[resoperate];
   reslist = Delete[SeedList, {{pick[[1]]}, {pick[[2]]}}];
   AppendTo[reslist, resoperate], SeedList]]
ListRandomSin[SeedList_] := 
 Module[{pick = {1}, resoperate = {}, reslist = {}}, 
  If[Length[SeedList] > 0, 
   pick = RandomSample[Range[Length[SeedList]], 1];
   resoperate = Sin[SeedList[[pick[[1]]]]];
   resoperate = Simplify[resoperate];
   reslist = Delete[SeedList, pick[[1]]];
   AppendTo[reslist, resoperate], SeedList]]
ListRandomCos[SeedList_] := 
 Module[{pick = {1}, resoperate = {}, reslist = {}}, 
  If[Length[SeedList] > 0, 
   pick = RandomSample[Range[Length[SeedList]], 1];
   resoperate = Cos[SeedList[[pick[[1]]]]];
   resoperate = Simplify[resoperate];
   reslist = Delete[SeedList, pick[[1]]];
   AppendTo[reslist, resoperate], SeedList]]
   
   
PrimitiveAndDerivativeGenerator[] := 
  Module[{SeedLength = 0, SeedList = {}, primitive = 12, 
    derivative = 12}, SeedLength = RandomInteger[{4, 7}];
   SeedList = 
    Table[RandomChoice[{8, 30, 1, 1} -> {x, 
        RandomInteger[{-300, 300}], Pi, E}], {SeedLength}];
   AppendTo[SeedList, x];
   While[Length[SeedList] > 1, 
    SeedList = 
     RandomChoice[{10, 10, 10, 10, 10, 10, 2, 2} -> {ListRandomPlus, 
         ListRandomSubtract, ListRandomTimes, ListRandomDivide, 
         ListRandomPower, ListRandomLog, ListRandomSin, 
         ListRandomCos}] @@ {SeedList}];
   primitive = Simplify[SeedList[[1]]];
   derivative = Simplify[D[primitive, x]];
   Return[{primitive, StringLength[ToString[primitive]], derivative, 
     StringLength[ToString[derivative]]}]
   ];
FindAProperQuestion[] := 
 Module[{primitive = 12, derivative = 12, primitivelength = 1000, 
   derivativelength = 1000},
  While[primitivelength > 100 || primitivelength < 20 || 
    derivativelength > 100 || 
    derivativelength < 20, {primitive, primitivelength, derivative, 
     derivativelength} = PrimitiveAndDerivativeGenerator[]];
  Return[{primitive, primitivelength, derivative, derivativelength}]
  ]
  

questions = {FindAProperQuestion[], FindAProperQuestion[], 
   FindAProperQuestion[], FindAProperQuestion[], 
   FindAProperQuestion[], FindAProperQuestion[], 
   FindAProperQuestion[], FindAProperQuestion[], 
   FindAProperQuestion[], FindAProperQuestion[]};
questionsandanswersstring = "";
Do[questionsandanswersstring = 
  StringJoin[questionsandanswersstring, "Find the derivative for:", 
   "\\begin{equation}", ToString[TeXForm[questions[[i]][[1]]]], 
   "\\end{equation}"], {i, 1, Length[questions] - 4}]
Do[questionsandanswersstring = 
  StringJoin[questionsandanswersstring, "Find the integral for:", 
   "\\begin{equation}", ToString[TeXForm[questions[[i]][[3]]]], 
   "\\end{equation}"], {i, Length[questions] - 3, Length[questions]}]
questionsandanswersstring = 
  StringJoin[questionsandanswersstring, "\n\n\n"];
Do[questionsandanswersstring = 
  StringJoin[questionsandanswersstring, "For the function:", 
   "\\begin{equation}", ToString[TeXForm[questions[[i]][[1]]]], 
   "\\end{equation}", "the derivative should be:", "$$", 
   ToString[TeXForm[questions[[i]][[3]]]], "$$"], {i, 1, 
  Length[questions] - 4}]
Do[questionsandanswersstring = 
  StringJoin[questionsandanswersstring, "For the function:", 
   "\\begin{equation}", ToString[TeXForm[questions[[i]][[3]]]], 
   "\\end{equation}", "the integral should be:", "$$", 
   ToString[TeXForm[questions[[i]][[1]]]], "$$"], {i, 
  Length[questions] - 3, Length[questions]}]
  
    
Export["D:\\questionsandanswersstring.txt", questionsandanswersstring]
