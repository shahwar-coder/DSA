'''
✅ 4. Parse Logical Pattern String
Problem:
Given a string pattern like "True AND False OR True", evaluate the boolean result (with correct operator precedence: AND before OR).

Input:
"True AND False OR True"
Output:
True
'''

def parse_expression(expression: str) -> bool:
    final_expression = []
    expression_list = expression.split()
    for exp_part in expression_list:
        lowered_exp_part = exp_part.strip().lower()
        if lowered_exp_part == "true":
            final_expression.append("True")
        elif lowered_exp_part == "false":
            final_expression.append("False")
        elif lowered_exp_part == "and":
            final_expression.append("and")
        elif lowered_exp_part == "or":
            final_expression.append("or")
        else:
            raise ValueError(f"Unsupported token: {exp_part}")

    final_expression_str = " ".join(final_expression)
    print(f"Final Exp (list) : {final_expression} , Final Exp (str) : {final_expression_str}")
    return eval(final_expression_str)  # literal_eval from ast to be aboided beacuse does not support "expressions"

def main():
    expression = "True AND False OR True"
    print(parse_expression(expression)) 

if __name__ == "__main__":
    main()
