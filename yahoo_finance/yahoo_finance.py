import yfinance as yf
import matplotlib

def yahoo_finance():
    petr4 = yf.Ticker("PETR4.SA")
    #Dividendos
    print(petr4.dividends)
    #Print do momento da ação
    print(petr4.info)

    #Dados de dividendos e splits
    print(petr4.actions)

    #Dados financeiros
    print(petr4.financials)
    print(petr4.quarterly_financials)

    #Dados de maiores acionistas
    print(petr4.major_holders)

    #Dados de fluxo de caixa
    print(petr4.cashflow)

    #Dados de balanço
    print(petr4.balance_sheet)

    #Histórico dos dados financeiros (possuem problemas segundo professor)
    print(petr4.history(period="max"))
    
yahoo_finance()