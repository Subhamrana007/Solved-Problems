class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        res = r

        def canShip(mid):
            ship, cap = 1, mid

            for w in weights:
                if cap - w < 0:
                    ship += 1
                    cap = mid

                cap -= w

            return ship <= days

        while l <= r:
            mid = (l + r) // 2

            if canShip(mid):
                res = min(mid, res)
                r = mid - 1

            else:
                l = mid + 1

        return res

