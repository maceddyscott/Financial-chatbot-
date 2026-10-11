import pandas as pd

# Financial data from your analysis
financial_data = {
    'Microsoft': {
        'Total Revenue 2025': 281724,
        'Total Revenue 2024': 245122,
        'Net Income 2025': 101832,
        'Net Income 2024': 88136,
        'Total Assets 2025': 619003,
        'Cash Flow 2025': 136162,
        'Revenue Growth 2025 vs 2024': 14.9,
        'Net Income Growth 2025 vs 2024': 15.6
    },
    'Tesla': {
        'Total Revenue 2025': 94827,
        'Total Revenue 2024': 97690,
        'Net Income 2025': 3855,
        'Net Income 2024': 7153,
        'Total Assets 2025': 137806,
        'Cash Flow 2025': 14747,
        'Revenue Growth 2025 vs 2024': -3.0,
        'Net Income Growth 2025 vs 2024': -46.1
    },
    'Apple': {
        'Total Revenue 2025': 416161,
        'Total Revenue 2024': 391035,
        'Net Income 2025': 112010,
        'Net Income 2024': 93736,
        'Total Assets 2025': 359241,
        'Cash Flow 2025': 111482,
        'Revenue Growth 2025 vs 2024': 6.4,
        'Net Income Growth 2025 vs 2024': 19.5
    }
}

def simple_chatbot(user_query):
    query = user_query.lower().strip()
    
    if "total revenue" in query and "microsoft" in query:
        return f"Microsoft's total revenue in 2025 is $281,724 million, representing a 14.9% increase from 2024."
    
    elif "total revenue" in query and "tesla" in query:
        return f"Tesla's total revenue in 2025 is $94,827 million, representing a 3.0% decrease from 2024."
    
    elif "total revenue" in query and "apple" in query:
        return f"Apple's total revenue in 2025 is $416,161 million, representing a 6.4% increase from 2024."
    
    elif "net income" in query and "microsoft" in query:
        return f"Microsoft's net income in 2025 is $101,832 million, up 15.6% from 2024. This demonstrates strong profitability and expanding margins."
    
    elif "net income" in query and "tesla" in query:
        return f"Tesla's net income in 2025 is $3,855 million, down 46.1% from 2024. This represents a critical profitability decline."
    
    elif "net income" in query and "apple" in query:
        return f"Apple's net income in 2025 is $112,010 million, up 19.5% from 2024. Strong recovery from prior-year challenges."
    
    elif "compare" in query and "revenue" in query:
        return "Revenue comparison: Apple leads at $416.2B, Microsoft is second at $281.7B, Tesla third at $94.8B. Apple and Microsoft grew; Tesla declined."
    
    elif "compare" in query and "profitability" in query:
        return "Profitability comparison: Microsoft shows strongest margins (36.1%), Apple solid (26.9%), Tesla concerning (4.1%). Microsoft excels in profit growth."
    
    elif "cash flow" in query:
        return "Cash flow from operations 2025: Microsoft $136.2B (strongest), Apple $111.5B (stable), Tesla $14.7B (weakest). Microsoft's cash generation is exceptional."
    
    elif "best performer" in query:
        return "Microsoft is the strongest performer across all metrics. Revenue +14.9%, net income +15.6%, expanding margins, exceptional cash flow of $136.2B."
    
    elif "worst performer" in query:
        return "Tesla faces significant challenges. Revenue -3.0%, net income -46.1%, profit margins collapsed to 4.1%. Requires urgent strategic intervention."
    
    elif "recommendation" in query or "invest" in query:
        return "Investment recommendation: Microsoft (strong buy) for growth, Apple (hold) for stability, Tesla (sell/avoid) until profitability stabilizes."
    
    else:
        return "I can answer questions about revenue, net income, cash flow, comparisons between Microsoft, Tesla, and Apple, or investment recommendations based on 2025 financial data."

def main():
    print("=" * 70)
    print("FINANCIAL CHATBOT - Microsoft, Tesla, Apple Analysis")
    print("=" * 70)
    print("Ask questions about:")
    print("- Total revenue (specific company or comparisons)")
    print("- Net income (specific company or comparisons)")
    print("- Cash flow")
    print("- Best/worst performer")
    print("- Investment recommendations")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Chatbot: Thank you for using the Financial Analysis Chatbot. Goodbye!")
            break
        
        if not user_input:
            print("Chatbot: Please enter a question.\n")
            continue
        
        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    main()