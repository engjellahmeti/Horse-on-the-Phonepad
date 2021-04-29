# @task Horse on the Phonepad
# @author Engjëll Ahmeti
# @date 4/29/2021

import unittest
from horse_on_the_phonepad import HorseOnPhonepad

class TestHorseOnPhonepad(unittest.TestCase):
    def test_horse_on_phonepad_start_position_0(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:6,4:12,5:32}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 0)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_1(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:5,4:10,5:26}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 1)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_2(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:4,4:10,5:20}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 2)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_3(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:5,4:10,5:26}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 3)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_4(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:3,3:6,4:16,5:32}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 4)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_5(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:0,3:0,4:0,5:0}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 5)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_6(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:3,3:6,4:16,5:32}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 6)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_7(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:5,4:10,5:26}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 7)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_8(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:4,4:10,5:20}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 8)

            self.assertEqual(distinct_numbers, results[N])

    def test_horse_on_phonepad_start_position_9(self):
        horse = HorseOnPhonepad()
        results = {1:1,2:2,3:5,4:10,5:26}
        for N in range(1, 6):
            distinct_numbers = horse.horse_on_phonepad(N, 9)

            self.assertEqual(distinct_numbers, results[N])

if __name__ == '__main__':
    unittest.main()