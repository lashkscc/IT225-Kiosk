import py_compile
import unittest
from kiosk import Kiosk
from item import Item
import mock



class TestKiosk(unittest.TestCase):
    def setUp(self):
        self.kiosk = Kiosk(1)

    def test_getKioskID(self):
        self.assertEqual(self.kiosk.getKioskID(), 1)
    
    def test_getCurrentCustomer(self):
        self.assertEqual(self.kiosk.getCurrentCustomer(), 0)
   
    def test_scanBarcode(self):
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(self.kiosk.scanBarcode(), 1)

    def test_getWeight(self):
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(self.kiosk.getWeight(), 1)

    def test_lockStatus(self):
        self.assertEqual(self.kiosk.lockStatus(), False)

    def test_set_lock_false(self):
        self.kiosk.setLock(True)
        self.assertEqual(self.kiosk.lockStatus(), True)

    def test_resetKiosk(self):
        self.kiosk.resetKiosk()
        self.assertEqual(self.kiosk.getCurrentCustomer(), 0)
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(self.kiosk.scanBarcode(), 1)
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(self.kiosk.getWeight(), 1)
        self.assertEqual(self.kiosk.lockStatus(), False)

    # def test_kiosk_init(self):
    #     self.assertEqual(self.kiosk.getKioskID(), 1)
    #     self.assertEqual(self.kiosk.getCurrentCustomer(), 0)
    #     self.assertEqual(self.kiosk.getScan(), 0)
    #     self.assertEqual(self.kiosk.getScale(), 0)
    #     self.assertEqual(self.kiosk.getLock(), False)
    
    def test_str(self):
        self.assertEqual(str(self.kiosk), "1 0 False")

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item(123, "Fremont Golden Pilsner", 0.5, 5.00, "alcohol", "recall")

    def test_getName(self):
        self.assertEqual(self.item.getName(), "Fremont Golden Pilsner")

    def test_getPricePerUnit(self):
        self.assertEqual(self.item.getPricePerUnit(), 5.00)

    def test_isPricedByWeight(self):
        self.assertEqual(self.item.isPricedByWeight(), False)

    def test_getAlerts(self):
        self.assertEqual(self.item.getAlerts(), ["alcohol", "recall"])

    def test_addAlert(self):
        self.item.addAlert("test")
        self.assertEqual(self.item.getAlerts(), ["alcohol", "recall", "test"])
    
    def test_removeAlert(self):
        self.item.removeAlert("recall")
        self.assertEqual(self.item.getAlerts(), ["alcohol"])
    
    def test_str(self):
        self.assertEqual(str(self.item), "123 Fremont Golden Pilsner False 5.0 alcohol recall")