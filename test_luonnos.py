import unittest
from luonnos040521 import *

class MyTestCase(unittest.TestCase):


    def test_openfile(self):
        openfile("aa")
        self.assertTrue(stats.filenotfound)
        openfile("")
        self.assertFalse(stats.filenotfound)

    def test_searchUndefined(self):
        stats.defined = []
        stats.lowerlist = {"Eka":-69,"Toka":-1337,"Kolmas":+666}
        self.assertEqual(len(searchUndefined()), 3)


    def test_addthistoUpper(self):
        # 1 because it includes what is added in test_addinfotostatsUpper
        self.assertEqual(len(stats.lowerlist), 1)
        self.assertEqual(len(stats.upperlist), 1)

        stats.lowerlist["lower"] = ["value"]
        addthistoUpper("lower", "upper")

        # test lowergroup in stats.defined
        self.assertIn("lower" , stats.defined)

        # test uppergroup in stats.upperlist
        self.assertIn("upper" , stats.upperlist)

        # test stats.upperlist[uppergroup] = [lowergroup]
        self.assertEqual(stats.upperlist["upper"], [["value"]])
        addthistoUpper("lower", "upper")
        self.assertEqual(stats.upperlist["upper"],  [['value'], ['value']])

    def test_addinfotostatsUPPER(self):
        self.assertIn("HOAS", stats.keywordlist)


        self.assertEqual(len(stats.lowerlist), 1)

        addinfotostatsUPPER()
        self.assertIn("HOAS", stats.defined)
        self.assertEqual(stats.upperlist["Asuminen"], [1337])
        addinfotostatsUPPER()
        self.assertEqual(stats.upperlist["Asuminen"], [1337])

    def test_addinfotostatsLOWER(self):
        addinfotostatsLOWER("HOAS", 1337,"ei tili siirto")

    def test_handleline(self):

        line = r'08.02.2021;08.02.2021;-310,"00;""106"";TILISIIRTO;""Hoas"";FI63 8000 1270 1634 14 / DABAFIHH;""00000000000003424405"";    ;20210108/593619/0C9535'
        handleline(line)


#self.assertEqual(weekdays( datetime.date(2021,2,1), datetime.date(2021,2,5)), weekdays(datetime.date(2021,2,1), datetime.date(2021,2,6)), "Saturday is not 'arkipaiva'")
if __name__ == '__main__':

    unittest.main()
