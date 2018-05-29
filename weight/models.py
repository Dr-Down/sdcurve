from core import Constants
from weight.curves import (
    WeightCurveMaleYears, WeightCurveMaleMonths,
    WeightCurveFemaleYears, WeightCurveFemaleMonths
)


class WeightCurve(object):
    """
    Growth curve based on the weight of the child with Down Syndrome.
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

    def __init__(self, gender=Constants.MALE, age=Constants.YEARS):
        """
        Redirects to chart type according to past parameters, MALE or FEMALE
        genre, and age MONTHS or YEARS
        """

        self.graphic = {}

        if gender == Constants.MALE and age == Constants.YEARS:
            self.curve = WeightCurveMaleYears()
        elif gender == Constants.MALE and age == Constants.MONTHS:
            self.curve = WeightCurveMaleMonths()
        elif gender == Constants.FEMALE and age == Constants.YEARS:
            self.curve = WeightCurveFemaleYears()
        else:
            self.curve = WeightCurveFemaleMonths()

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

    def make_charts(self, years=False):
        """
        Function to create percentis curves to plot in google charts.
        """

        array_data_table = [['Ages', '3%', '10%', '25%', '50%', '75%', '90%', '97%', "Patient"]]

        ages = self.make(WeightCurve.AGES)
        percentis_3 = self.make(WeightCurve.PERCENTIS_3)
        percentis_10 = self.make(WeightCurve.PERCENTIS_10)
        percentis_25 = self.make(WeightCurve.PERCENTIS_25)
        percentis_50 = self.make(WeightCurve.PERCENTIS_50)
        percentis_75 = self.make(WeightCurve.PERCENTIS_75)
        percentis_90 = self.make(WeightCurve.PERCENTIS_90)
        percentis_97 = self.make(WeightCurve.PERCENTIS_97)

        for age in ages:
            if years:
                age -= 3

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

    def result(self, weight, age):
        """
        Check the chart if the child is above, below or at the mean weight.
        """

        success = False
        result = 0
        count = 0

        for curve_age in self.curve.ages:
            if age == curve_age:
                success = True
                break

            count += 1

        if not success:
            result = "Invalid age"
            return result

        if weight < self.curve.percentis_3[count]:
            result = -1

        if weight > self.curve.percentis_97[count]:
            result = 1

        return result
