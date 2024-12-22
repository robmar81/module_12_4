import rt_with_exceptions as rwe
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")

class RunerTest(unittest.TestCase):
    def test_walk(self):
        try:
            wlk = rwe.Runner('гуляка', -5)
            for i in range(10):
                wlk.walk()
            self.assertEqual(wlk.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)



    def test_run(self):
        try:
            rnr = rwe.Runner(1001)
            for i in range(10):
                rnr.run()
            self.assertEqual(rnr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        wlk = rwe.Runner('гуляка')
        rnr = rwe.Runner('беглец')
        for i in range(10):
            wlk.walk()
            rnr.run()
        self.assertNotEqual(wlk.distance, rnr.distance)


if __name__ == "__main__":
    unittest.main()
