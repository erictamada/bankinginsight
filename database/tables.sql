CREATE TABLE IF NOT EXISTS customers(
	id UUID PRIMARY KEY,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	telefone TEXT NOT NULL,
	age INT NOT NULL,
	monthly_income FLOAT NOT NULL,
	monthly_expense FLOAT NOT NULL,
	risk_taken TEXT NOT NULL,
	investment_duration TEXT NOT NULL,
	financial_goal TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS investments (
	id TEXT PRIMARY KEY,
	name TEXT NOT NULL,
	type TEXT NOT NULL,
	risk_level TEXT NOT NULL,
	expected_return FLOAT NOT NULL,
	duration TEXT NOT NULL
);

