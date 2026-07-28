from client import ProactiveECommerceTeamAgentClient

def main():
    client = ProactiveECommerceTeamAgentClient()
    res = client.execute_store_goal({"daily_sales_usd": 4500, "abandoned_carts": 34})
    print(f"Projected Boost: +{res['projected_mrr_boost_pct']}%")
    print("Team Action Plan:")
    for act in res["team_actions"]:
        print(f"  - {act}")

if __name__ == "__main__":
    main()
