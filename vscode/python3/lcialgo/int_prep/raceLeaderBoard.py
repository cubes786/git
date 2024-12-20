import unittest as ut 

def update_leaderboard(data):
    #mile_mark, playerid
    ranks={}
    for mile,player in data:
        ranks[player]=mile
    rank_list=sorted(ranks.keys(), key=lambda x:-ranks[x])
    return rank_list
    

class TestLeaderBoard(ut.TestCase):
    def test1_leaderboard(self):
        data=[(1,1),(3,1),(1,2),(2,4)]
        expected=[1,4,2]
        result=update_leaderboard(data)
        self.assertEqual(result, expected)

    def test2_leaderboard(self):
        data=[(6,7),(5,2),(5,1),(4,4)]
        expected=[7,2,1,4]
        result=update_leaderboard(data)
        self.assertEqual(expected, result)

if __name__=='__main__':
    ut.main()

