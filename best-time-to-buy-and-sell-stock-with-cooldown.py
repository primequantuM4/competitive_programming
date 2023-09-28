                skipped_point = dp(index + 1, False)
                return max(buy_point, skipped_point)
                buy_point = -prices[index] + dp(index + 1, True)
            if not used:
                return 0
            else:
                sell_point = prices[index] + dp(index + 2, False)
                skipped_point = dp(index + 1, True)
                return max(skipped_point, sell_point)
        