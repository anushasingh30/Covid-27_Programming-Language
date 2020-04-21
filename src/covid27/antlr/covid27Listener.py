# Generated from covid27.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .covid27Parser import covid27Parser
else:
    from covid27Parser import covid27Parser

# This class defines a complete listener for a parse tree produced by covid27Parser.
class covid27Listener(ParseTreeListener):

    # Enter a parse tree produced by covid27Parser#program.
    def enterProgram(self, ctx:covid27Parser.ProgramContext):
        pass

    # Exit a parse tree produced by covid27Parser#program.
    def exitProgram(self, ctx:covid27Parser.ProgramContext):
        pass


    # Enter a parse tree produced by covid27Parser#block.
    def enterBlock(self, ctx:covid27Parser.BlockContext):
        pass

    # Exit a parse tree produced by covid27Parser#block.
    def exitBlock(self, ctx:covid27Parser.BlockContext):
        pass


    # Enter a parse tree produced by covid27Parser#idDeclaration.
    def enterIdDeclaration(self, ctx:covid27Parser.IdDeclarationContext):
        pass

    # Exit a parse tree produced by covid27Parser#idDeclaration.
    def exitIdDeclaration(self, ctx:covid27Parser.IdDeclarationContext):
        pass


    # Enter a parse tree produced by covid27Parser#listIdDeclaration.
    def enterListIdDeclaration(self, ctx:covid27Parser.ListIdDeclarationContext):
        pass

    # Exit a parse tree produced by covid27Parser#listIdDeclaration.
    def exitListIdDeclaration(self, ctx:covid27Parser.ListIdDeclarationContext):
        pass


    # Enter a parse tree produced by covid27Parser#idDeclarationAssign.
    def enterIdDeclarationAssign(self, ctx:covid27Parser.IdDeclarationAssignContext):
        pass

    # Exit a parse tree produced by covid27Parser#idDeclarationAssign.
    def exitIdDeclarationAssign(self, ctx:covid27Parser.IdDeclarationAssignContext):
        pass


    # Enter a parse tree produced by covid27Parser#idExpressionDeclaration.
    def enterIdExpressionDeclaration(self, ctx:covid27Parser.IdExpressionDeclarationContext):
        pass

    # Exit a parse tree produced by covid27Parser#idExpressionDeclaration.
    def exitIdExpressionDeclaration(self, ctx:covid27Parser.IdExpressionDeclarationContext):
        pass


    # Enter a parse tree produced by covid27Parser#notDeclaration.
    def enterNotDeclaration(self, ctx:covid27Parser.NotDeclarationContext):
        pass

    # Exit a parse tree produced by covid27Parser#notDeclaration.
    def exitNotDeclaration(self, ctx:covid27Parser.NotDeclarationContext):
        pass


    # Enter a parse tree produced by covid27Parser#statement_list.
    def enterStatement_list(self, ctx:covid27Parser.Statement_listContext):
        pass

    # Exit a parse tree produced by covid27Parser#statement_list.
    def exitStatement_list(self, ctx:covid27Parser.Statement_listContext):
        pass


    # Enter a parse tree produced by covid27Parser#statement.
    def enterStatement(self, ctx:covid27Parser.StatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#statement.
    def exitStatement(self, ctx:covid27Parser.StatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#identifierElement.
    def enterIdentifierElement(self, ctx:covid27Parser.IdentifierElementContext):
        pass

    # Exit a parse tree produced by covid27Parser#identifierElement.
    def exitIdentifierElement(self, ctx:covid27Parser.IdentifierElementContext):
        pass


    # Enter a parse tree produced by covid27Parser#identifierExpr.
    def enterIdentifierExpr(self, ctx:covid27Parser.IdentifierExprContext):
        pass

    # Exit a parse tree produced by covid27Parser#identifierExpr.
    def exitIdentifierExpr(self, ctx:covid27Parser.IdentifierExprContext):
        pass


    # Enter a parse tree produced by covid27Parser#stdIfStatement.
    def enterStdIfStatement(self, ctx:covid27Parser.StdIfStatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#stdIfStatement.
    def exitStdIfStatement(self, ctx:covid27Parser.StdIfStatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#ifElseStatement.
    def enterIfElseStatement(self, ctx:covid27Parser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#ifElseStatement.
    def exitIfElseStatement(self, ctx:covid27Parser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#ifElseIfStatement.
    def enterIfElseIfStatement(self, ctx:covid27Parser.IfElseIfStatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#ifElseIfStatement.
    def exitIfElseIfStatement(self, ctx:covid27Parser.IfElseIfStatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#elseStatement.
    def enterElseStatement(self, ctx:covid27Parser.ElseStatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#elseStatement.
    def exitElseStatement(self, ctx:covid27Parser.ElseStatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#condition.
    def enterCondition(self, ctx:covid27Parser.ConditionContext):
        pass

    # Exit a parse tree produced by covid27Parser#condition.
    def exitCondition(self, ctx:covid27Parser.ConditionContext):
        pass


    # Enter a parse tree produced by covid27Parser#whileLoop.
    def enterWhileLoop(self, ctx:covid27Parser.WhileLoopContext):
        pass

    # Exit a parse tree produced by covid27Parser#whileLoop.
    def exitWhileLoop(self, ctx:covid27Parser.WhileLoopContext):
        pass


    # Enter a parse tree produced by covid27Parser#while_condition.
    def enterWhile_condition(self, ctx:covid27Parser.While_conditionContext):
        pass

    # Exit a parse tree produced by covid27Parser#while_condition.
    def exitWhile_condition(self, ctx:covid27Parser.While_conditionContext):
        pass


    # Enter a parse tree produced by covid27Parser#forLoop.
    def enterForLoop(self, ctx:covid27Parser.ForLoopContext):
        pass

    # Exit a parse tree produced by covid27Parser#forLoop.
    def exitForLoop(self, ctx:covid27Parser.ForLoopContext):
        pass


    # Enter a parse tree produced by covid27Parser#for_var.
    def enterFor_var(self, ctx:covid27Parser.For_varContext):
        pass

    # Exit a parse tree produced by covid27Parser#for_var.
    def exitFor_var(self, ctx:covid27Parser.For_varContext):
        pass


    # Enter a parse tree produced by covid27Parser#printString.
    def enterPrintString(self, ctx:covid27Parser.PrintStringContext):
        pass

    # Exit a parse tree produced by covid27Parser#printString.
    def exitPrintString(self, ctx:covid27Parser.PrintStringContext):
        pass


    # Enter a parse tree produced by covid27Parser#printIdentifier.
    def enterPrintIdentifier(self, ctx:covid27Parser.PrintIdentifierContext):
        pass

    # Exit a parse tree produced by covid27Parser#printIdentifier.
    def exitPrintIdentifier(self, ctx:covid27Parser.PrintIdentifierContext):
        pass


    # Enter a parse tree produced by covid27Parser#relBoolStatement.
    def enterRelBoolStatement(self, ctx:covid27Parser.RelBoolStatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#relBoolStatement.
    def exitRelBoolStatement(self, ctx:covid27Parser.RelBoolStatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#logicBoolStatement.
    def enterLogicBoolStatement(self, ctx:covid27Parser.LogicBoolStatementContext):
        pass

    # Exit a parse tree produced by covid27Parser#logicBoolStatement.
    def exitLogicBoolStatement(self, ctx:covid27Parser.LogicBoolStatementContext):
        pass


    # Enter a parse tree produced by covid27Parser#booleanVal.
    def enterBooleanVal(self, ctx:covid27Parser.BooleanValContext):
        pass

    # Exit a parse tree produced by covid27Parser#booleanVal.
    def exitBooleanVal(self, ctx:covid27Parser.BooleanValContext):
        pass


    # Enter a parse tree produced by covid27Parser#EqualRelExpression.
    def enterEqualRelExpression(self, ctx:covid27Parser.EqualRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#EqualRelExpression.
    def exitEqualRelExpression(self, ctx:covid27Parser.EqualRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#greaterRelExpression.
    def enterGreaterRelExpression(self, ctx:covid27Parser.GreaterRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#greaterRelExpression.
    def exitGreaterRelExpression(self, ctx:covid27Parser.GreaterRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#greaterEqualRelExpression.
    def enterGreaterEqualRelExpression(self, ctx:covid27Parser.GreaterEqualRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#greaterEqualRelExpression.
    def exitGreaterEqualRelExpression(self, ctx:covid27Parser.GreaterEqualRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#lessEqualRelExpression.
    def enterLessEqualRelExpression(self, ctx:covid27Parser.LessEqualRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#lessEqualRelExpression.
    def exitLessEqualRelExpression(self, ctx:covid27Parser.LessEqualRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#lessRelExpression.
    def enterLessRelExpression(self, ctx:covid27Parser.LessRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#lessRelExpression.
    def exitLessRelExpression(self, ctx:covid27Parser.LessRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#NotEqualsRelExpression.
    def enterNotEqualsRelExpression(self, ctx:covid27Parser.NotEqualsRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#NotEqualsRelExpression.
    def exitNotEqualsRelExpression(self, ctx:covid27Parser.NotEqualsRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#idEqualsBoolExpression.
    def enterIdEqualsBoolExpression(self, ctx:covid27Parser.IdEqualsBoolExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#idEqualsBoolExpression.
    def exitIdEqualsBoolExpression(self, ctx:covid27Parser.IdEqualsBoolExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#idNotEqualsBoolExpression.
    def enterIdNotEqualsBoolExpression(self, ctx:covid27Parser.IdNotEqualsBoolExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#idNotEqualsBoolExpression.
    def exitIdNotEqualsBoolExpression(self, ctx:covid27Parser.IdNotEqualsBoolExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#andLogicRelExpression.
    def enterAndLogicRelExpression(self, ctx:covid27Parser.AndLogicRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#andLogicRelExpression.
    def exitAndLogicRelExpression(self, ctx:covid27Parser.AndLogicRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#orLogicRelExpression.
    def enterOrLogicRelExpression(self, ctx:covid27Parser.OrLogicRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#orLogicRelExpression.
    def exitOrLogicRelExpression(self, ctx:covid27Parser.OrLogicRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#andRelLogicExpression.
    def enterAndRelLogicExpression(self, ctx:covid27Parser.AndRelLogicExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#andRelLogicExpression.
    def exitAndRelLogicExpression(self, ctx:covid27Parser.AndRelLogicExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#orRelLogicExpression.
    def enterOrRelLogicExpression(self, ctx:covid27Parser.OrRelLogicExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#orRelLogicExpression.
    def exitOrRelLogicExpression(self, ctx:covid27Parser.OrRelLogicExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#NotRelExpression.
    def enterNotRelExpression(self, ctx:covid27Parser.NotRelExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#NotRelExpression.
    def exitNotRelExpression(self, ctx:covid27Parser.NotRelExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#noLogicExpression.
    def enterNoLogicExpression(self, ctx:covid27Parser.NoLogicExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#noLogicExpression.
    def exitNoLogicExpression(self, ctx:covid27Parser.NoLogicExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#additionExpression.
    def enterAdditionExpression(self, ctx:covid27Parser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#additionExpression.
    def exitAdditionExpression(self, ctx:covid27Parser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#subtractionExpression.
    def enterSubtractionExpression(self, ctx:covid27Parser.SubtractionExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#subtractionExpression.
    def exitSubtractionExpression(self, ctx:covid27Parser.SubtractionExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#terminology.
    def enterTerminology(self, ctx:covid27Parser.TerminologyContext):
        pass

    # Exit a parse tree produced by covid27Parser#terminology.
    def exitTerminology(self, ctx:covid27Parser.TerminologyContext):
        pass


    # Enter a parse tree produced by covid27Parser#mullExpression.
    def enterMullExpression(self, ctx:covid27Parser.MullExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#mullExpression.
    def exitMullExpression(self, ctx:covid27Parser.MullExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#divisionExpression.
    def enterDivisionExpression(self, ctx:covid27Parser.DivisionExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#divisionExpression.
    def exitDivisionExpression(self, ctx:covid27Parser.DivisionExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#modExpression.
    def enterModExpression(self, ctx:covid27Parser.ModExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#modExpression.
    def exitModExpression(self, ctx:covid27Parser.ModExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#fact.
    def enterFact(self, ctx:covid27Parser.FactContext):
        pass

    # Exit a parse tree produced by covid27Parser#fact.
    def exitFact(self, ctx:covid27Parser.FactContext):
        pass


    # Enter a parse tree produced by covid27Parser#bracketExpression.
    def enterBracketExpression(self, ctx:covid27Parser.BracketExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#bracketExpression.
    def exitBracketExpression(self, ctx:covid27Parser.BracketExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#identifierExpression.
    def enterIdentifierExpression(self, ctx:covid27Parser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#identifierExpression.
    def exitIdentifierExpression(self, ctx:covid27Parser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#numExpression.
    def enterNumExpression(self, ctx:covid27Parser.NumExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#numExpression.
    def exitNumExpression(self, ctx:covid27Parser.NumExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#multipleElementList.
    def enterMultipleElementList(self, ctx:covid27Parser.MultipleElementListContext):
        pass

    # Exit a parse tree produced by covid27Parser#multipleElementList.
    def exitMultipleElementList(self, ctx:covid27Parser.MultipleElementListContext):
        pass


    # Enter a parse tree produced by covid27Parser#oneElementList.
    def enterOneElementList(self, ctx:covid27Parser.OneElementListContext):
        pass

    # Exit a parse tree produced by covid27Parser#oneElementList.
    def exitOneElementList(self, ctx:covid27Parser.OneElementListContext):
        pass


    # Enter a parse tree produced by covid27Parser#idAddListExpression.
    def enterIdAddListExpression(self, ctx:covid27Parser.IdAddListExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#idAddListExpression.
    def exitIdAddListExpression(self, ctx:covid27Parser.IdAddListExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#listIdExpression.
    def enterListIdExpression(self, ctx:covid27Parser.ListIdExpressionContext):
        pass

    # Exit a parse tree produced by covid27Parser#listIdExpression.
    def exitListIdExpression(self, ctx:covid27Parser.ListIdExpressionContext):
        pass


    # Enter a parse tree produced by covid27Parser#dtype.
    def enterDtype(self, ctx:covid27Parser.DtypeContext):
        pass

    # Exit a parse tree produced by covid27Parser#dtype.
    def exitDtype(self, ctx:covid27Parser.DtypeContext):
        pass


    # Enter a parse tree produced by covid27Parser#identifier.
    def enterIdentifier(self, ctx:covid27Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by covid27Parser#identifier.
    def exitIdentifier(self, ctx:covid27Parser.IdentifierContext):
        pass


    # Enter a parse tree produced by covid27Parser#element.
    def enterElement(self, ctx:covid27Parser.ElementContext):
        pass

    # Exit a parse tree produced by covid27Parser#element.
    def exitElement(self, ctx:covid27Parser.ElementContext):
        pass


    # Enter a parse tree produced by covid27Parser#curlyBraceOpen.
    def enterCurlyBraceOpen(self, ctx:covid27Parser.CurlyBraceOpenContext):
        pass

    # Exit a parse tree produced by covid27Parser#curlyBraceOpen.
    def exitCurlyBraceOpen(self, ctx:covid27Parser.CurlyBraceOpenContext):
        pass


    # Enter a parse tree produced by covid27Parser#curlyBraceClose.
    def enterCurlyBraceClose(self, ctx:covid27Parser.CurlyBraceCloseContext):
        pass

    # Exit a parse tree produced by covid27Parser#curlyBraceClose.
    def exitCurlyBraceClose(self, ctx:covid27Parser.CurlyBraceCloseContext):
        pass


    # Enter a parse tree produced by covid27Parser#simpleBraceOpen.
    def enterSimpleBraceOpen(self, ctx:covid27Parser.SimpleBraceOpenContext):
        pass

    # Exit a parse tree produced by covid27Parser#simpleBraceOpen.
    def exitSimpleBraceOpen(self, ctx:covid27Parser.SimpleBraceOpenContext):
        pass


    # Enter a parse tree produced by covid27Parser#simpleBraceClose.
    def enterSimpleBraceClose(self, ctx:covid27Parser.SimpleBraceCloseContext):
        pass

    # Exit a parse tree produced by covid27Parser#simpleBraceClose.
    def exitSimpleBraceClose(self, ctx:covid27Parser.SimpleBraceCloseContext):
        pass


    # Enter a parse tree produced by covid27Parser#squareBraceOpen.
    def enterSquareBraceOpen(self, ctx:covid27Parser.SquareBraceOpenContext):
        pass

    # Exit a parse tree produced by covid27Parser#squareBraceOpen.
    def exitSquareBraceOpen(self, ctx:covid27Parser.SquareBraceOpenContext):
        pass


    # Enter a parse tree produced by covid27Parser#squareBraceClose.
    def enterSquareBraceClose(self, ctx:covid27Parser.SquareBraceCloseContext):
        pass

    # Exit a parse tree produced by covid27Parser#squareBraceClose.
    def exitSquareBraceClose(self, ctx:covid27Parser.SquareBraceCloseContext):
        pass



del covid27Parser