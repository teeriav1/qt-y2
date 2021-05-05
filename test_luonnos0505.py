import unittest
from luonnos050521 import *



class MyTestCase(unittest.TestCase):
    # API TESTS
    def test_api_self_colorsamount(self):
        self.assertEqual(len(ex.colors),10)
    def test_api_groupnames_8(self):
        self.assertEqual(len(ex.groupnames),8)
    def test_api_all_total(self):
        total = 0
        for nominal in ex.groupnominals:
            total += nominal
        self.assertEqual(total, -384998)
    def test_api_group_percents_round_to_100(self):
        total = 0
        for percentvalue in ex.grouppercents:
            total += percentvalue
        self.assertEqual(total,100)
    def test_manual_adding_of_lines(self):
        #First add
        ex.qLineEdit.setText("Paavon Pesupaja")
        ex.qLineEdit3.setText("66666")
        ex.manual_adding_of_lines_add_a_line()
        total = 0
        for nominal in ex.groupnominals:
            total += nominal
        self.assertEqual(total, -451664)

        #  THen remove
        ex.qLineEdit.setText("Paavon Pesupaja")
        ex.qLineEdit3.setText("-66666")
        ex.manual_adding_of_lines_add_a_line()
        total = 0
        for nominal in ex.groupnominals:
            total += nominal
        self.assertEqual(total, -384998)

        # Check that there is a group added
        self.assertEqual(len(ex.groupnames),9)
        ex.groupnames.remove("Paavon Pesupaja")
        self.assertEqual(len(ex.groupnames),8)
    def test_savings_program(self):
        # This is supposed to save 300€ which is 30000 in this program
        # It is supposed not to save them from group[4567]
        # And supposed to save less from 1,2
        # And append a group called Saved amount which is the size of amount saved

        vertauslista = []   # Vertauslista is values before saving
                            # Vertauslista will have one value less, Saved amount will be missing
        for nominal in ex.groupnominals:
            vertauslista.append(nominal)
        ex.start_saving_program_step1()
        for name in ex.groupnames:
            #print(name)
            pass
        self.assertEqual(len(ex.groupnames), 10)
        difference = 0
        for i in range(len(vertauslista)):
            difference += vertauslista[i] - ex.groupnominals[i]
        self.assertEqual(difference,-30000)
        self.assertEqual(ex.groupnominals[-1],difference)
        for i in range(len(vertauslista)):
            reducement = 0
            if i in [1,2]:
                reducement = -5000
            if i in [0,3]:
                reducement = - 10000
            self.assertEqual(vertauslista[i]-ex.groupnominals[i], reducement)







    # ENGINE TESTS
    def test_openfile(self):

        openfile("aaa")
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
    app = QApplication(sys.argv)
    ex = Example(False)  # With False-text program will perform preset run and api will be barely seen
    unittest.main()
