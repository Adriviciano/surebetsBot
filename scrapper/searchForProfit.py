def getProfit(sportium_str, juegging_str, sportium_dob_str, juegging_dob_str):
    # Parsing of the strings
    sportium_odds = {}
    juegging_odds = {}
    sportium_dob_odds = {}
    juegging_dob_odds = {}
    for key, value in [s.split(":") for s in sportium_str.split("/")]:
        sportium_odds[key] = float(value)
    for key, value in [s.split(":") for s in juegging_str.split("/")]:
        juegging_odds[key] = float(value)
    for key, value in [s.split(":") for s in sportium_dob_str.split("/")]:
        sportium_dob_odds[key] = float(value)
    for key, value in [s.split(":") for s in juegging_dob_str.split("/")]:
        juegging_dob_odds[key] = float(value)

    # Calculation of surebets
    surebets = {}
    for option in [("1", "X2"), ("X", "12"), ("2", "1X")]:
        op1, op2 = option
        if op1 in sportium_odds and op2 in juegging_odds:
            surebet_odds = 1/sportium_odds[op1] + 1/juegging_odds[op2]
            surebets[op1 + "-" + op2] = surebet_odds

    # Calculation of profits
    max_bet = 15
    best_profit = 0
    best_bet = ""
    for bet, odds in surebets.items():
        op1, op2 = bet.split("-")
        if op1 in sportium_dob_odds and op2 in juegging_dob_odds:
            odd1 = sportium_dob_odds[op1]
            odd2 = juegging_dob_odds[op2]
            bet1 = (max_bet * odd2) / (odd1 + odd2)
            bet2 = max_bet - bet1
            profit1 = bet1 * odd1 - max_bet
            profit2 = bet2 * odd2 - max_bet
            if 0 < profit1 and 0 < profit2 and bet1 <= max_bet and bet2 <= max_bet:
                if profit1 > best_profit:
                    best_profit = profit1
                    best_bet = f"Apuesta {bet} en Sportium: {bet1:.2f} € y en Juegging: {bet2:.2f} €"
                if profit2 > best_profit:
                    best_profit = profit2
                    best_bet = f"Apuesta {bet} en Juegging: {bet1:.2f} € y en Sportium: {bet2:.2f} €"

    # Return of the result
    if best_profit < 1:
        return "No se ha encontrado una surebet rentable"
    else:
        return best_bet
