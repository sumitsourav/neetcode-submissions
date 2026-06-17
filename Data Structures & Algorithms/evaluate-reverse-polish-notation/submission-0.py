class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp_stack = []

        for char in tokens:
            if char == '-' or char == '*' or char == '+' or char == '/':
                ele1 = exp_stack.pop()
                ele2 = exp_stack.pop()
                match char:
                    case '+':
                        result = (ele2 + ele1)
                        exp_stack.append(int(result))
                    case '-':
                        result = (ele2 - ele1)
                        exp_stack.append(int(result))
                    case '*':
                        result = (ele2 * ele1)
                        exp_stack.append(int(result))
                    case '/':
                        result = int(ele2 / ele1)
                        exp_stack.append(int(result))
            else:
                exp_stack.append(int(char))
        return exp_stack.pop()
