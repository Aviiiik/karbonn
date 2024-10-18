from rules import latest_financial_index, iscr_flag, total_revenue_5cr_flag, borrowing_to_revenue_flag

def probe_model_5l_profit(data):
    """
    Evaluate financial flags for the latest financial entry.
    """
    index = latest_financial_index(data)

    return {
        "flags": {
            "TOTAL_REVENUE_5CR_FLAG": total_revenue_5cr_flag(data, index),
            "BORROWING_TO_REVENUE_FLAG": borrowing_to_revenue_flag(data, index),
            "ISCR_FLAG": iscr_flag(data, index),
        }
    }
