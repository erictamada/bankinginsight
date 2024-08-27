import pandas as pd

def generate_investments():
    investments = [
        {'id': 'PETR4', 'name': 'Petrobras PN', 'type': 'Ações', 'risk_level': 'High', 'expected_return': 0.12, 'duration': 'Long Term'},
        {'id': 'VALE3', 'name': 'Vale ON', 'type': 'Ações', 'risk_level': 'High', 'expected_return': 0.15, 'duration': 'Long Term'},
        {'id': 'ITUB4', 'name': 'Itaú Unibanco PN', 'type': 'Ações', 'risk_level': 'Medium', 'expected_return': 0.10, 'duration': 'Long Term'},
        {'id': 'XPML11', 'name': 'XP Malls FII', 'type': 'Fundo Imobiliário', 'risk_level': 'Medium', 'expected_return': 0.08, 'duration': 'Medium Term'},
        {'id': 'HGLG11', 'name': 'CSHG Logística FII', 'type': 'Fundo Imobiliário', 'risk_level': 'Medium', 'expected_return': 0.07, 'duration': 'Medium Term'},
        {'id': 'CDB_1', 'name': 'CDB Banco ABC', 'type': 'CDB', 'risk_level': 'Low', 'expected_return': 0.05, 'duration': 'Short Term'},
        {'id': 'CDB_2', 'name': 'CDB Banco Inter', 'type': 'CDB', 'risk_level': 'Low', 'expected_return': 0.06, 'duration': 'Short Term'},
        {'id': 'TESOURO_SELIC', 'name': 'Tesouro Selic 2025', 'type': 'Government Bond', 'risk_level': 'Low', 'expected_return': 0.045, 'duration': 'Short Term'},
        {'id': 'TESOURO_IPCA', 'name': 'Tesouro IPCA+ 2035', 'type': 'Government Bond', 'risk_level': 'Low', 'expected_return': 0.05, 'duration': 'Long Term'},
        {'id': 'LCI_1', 'name': 'LCI Banco do Brasil', 'type': 'LCI', 'risk_level': 'Low', 'expected_return': 0.04, 'duration': 'Medium Term'},
    ]
    return pd.DataFrame(investments)

if __name__ == "__main__":
    investments_df = generate_investments()
    investments_df.to_csv('data/investments.csv', index=False)