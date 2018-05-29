from core import Constants
from perimeter.curves import PerimeterCurveMale, PerimeterCurveFemale


class PerimeterCurve(object):
    """
    Growth curve based on the cephalic perimeter of the child with Down Syndrome.
    """

    ALL = 0
    AGES = 1
    PERCENTIS_3 = 2
    PERCENTIS_10 = 3
    PERCENTIS_25 = 4
    PERCENTIS_50 = 5
    PERCENTIS_75 = 6
    PERCENTIS_90 = 7
    PERCENTIS_97 = 8
    TITLE = 9

    def __init__(self, gender=Constants.MALE):
        """
        Redirects to chart type according to past parameters, MALE or FEMALE
        genre
        """

        self.graphic = {}

        if gender == Constants.MALE:
            self.curve = PerimeterCurveMale()
        else:
            self.curve = PerimeterCurveFemale()

        self.graphic = self.curve.make()

    def make(self, axis=0):
        """
        Return a graphic
        """

        result = []

        if axis == self.ALL:
            result = self.graphic
        elif axis == self.AGES:
            result = self.curve.ages
        elif axis == self.PERCENTIS_3:
            result = self.curve.percentis_3
        elif axis == self.PERCENTIS_10:
            result = self.curve.percentis_10
        elif axis == self.PERCENTIS_25:
            result = self.curve.percentis_25
        elif axis == self.PERCENTIS_50:
            result = self.curve.percentis_50
        elif axis == self.PERCENTIS_75:
            result = self.curve.percentis_75
        elif axis == self.PERCENTIS_90:
            result = self.curve.percentis_90
        elif axis == self.PERCENTIS_97:
            result = self.curve.percentis_97
        else:
            result = self.curve.title

        return result

    def make_charts(self):
        """
        Function to create percentis curves to plot in google charts.
        """

        array_data_table = [['Ages', '3%', '10%', '25%', '50%', '75%', '90%', '97%', "Patient"]]

        ages = self.make(PerimeterCurve.AGES)
        percentis_3 = self.make(PerimeterCurve.PERCENTIS_3)
        percentis_10 = self.make(PerimeterCurve.PERCENTIS_10)
        percentis_25 = self.make(PerimeterCurve.PERCENTIS_25)
        percentis_50 = self.make(PerimeterCurve.PERCENTIS_50)
        percentis_75 = self.make(PerimeterCurve.PERCENTIS_75)
        percentis_90 = self.make(PerimeterCurve.PERCENTIS_90)
        percentis_97 = self.make(PerimeterCurve.PERCENTIS_97)

        for age in ages:
            array_data_table.append([
                ages[age],
                percentis_3[age],
                percentis_10[age],
                percentis_25[age],
                percentis_50[age],
                percentis_75[age],
                percentis_90[age],
                percentis_97[age],
            ])

        for i in range(len(array_data_table)):
            if i == 0:
                continue
            array_data_table[i].append(0.0)

        return array_data_table

    def result(self, perimeter, age):
        """
        Check the chart if the child is above, below or at the mean cephalic perimeter.
        """

        success = True
        result = 0

        if age < 0 or age > 24:
            success = False

        if not success:
            result = "Invalid age"
            return result

        if perimeter < self.curve.percentis_3[age]:
            result = -1

        if perimeter > self.curve.percentis_97[age]:
            result = 1

        return result
