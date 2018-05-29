from core import Constants
from imc.curves import IMCCurveMale, IMCCurveFemale


class IMCCurve(object):
    """
    Growth curve based on the IMC of the child with Down Syndrome.
    """

    ALL = 0
    AGES = 1
    PERCENTIS_5 = 2
    PERCENTIS_10 = 3
    PERCENTIS_25 = 4
    PERCENTIS_50 = 5
    PERCENTIS_75 = 6
    PERCENTIS_85 = 7
    PERCENTIS_90 = 8
    PERCENTIS_95 = 9
    TITLE = 10

    def __init__(self, gender=Constants.MALE):
        """
        Redirects to chart type according to past parameters, MALE or FEMALE
        genre
        """

        self.graphic = {}

        if gender == Constants.MALE:
            self.curve = IMCCurveMale()
        else:
            self.curve = IMCCurveFemale()

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
        elif axis == self.PERCENTIS_5:
            result = self.curve.percentis_5
        elif axis == self.PERCENTIS_10:
            result = self.curve.percentis_10
        elif axis == self.PERCENTIS_25:
            result = self.curve.percentis_25
        elif axis == self.PERCENTIS_50:
            result = self.curve.percentis_50
        elif axis == self.PERCENTIS_75:
            result = self.curve.percentis_75
        elif axis == self.PERCENTIS_85:
            result = self.curve.percentis_85
        elif axis == self.PERCENTIS_90:
            result = self.curve.percentis_90
        elif axis == self.PERCENTIS_95:
            result = self.curve.percentis_95
        else:
            result = self.curve.title

        return result

    def make_charts(self):
        """
        Function to create percentis curves to plot in google charts.
        """

        array_data_table = [['Ages', '5%', '10%', '25%', '50%', '75%', '85%', '90%', '95%', "Patient"]]

        ages = self.make(IMCCurve.AGES)
        percentis_5 = self.make(IMCCurve.PERCENTIS_5)
        percentis_10 = self.make(IMCCurve.PERCENTIS_10)
        percentis_25 = self.make(IMCCurve.PERCENTIS_25)
        percentis_50 = self.make(IMCCurve.PERCENTIS_50)
        percentis_75 = self.make(IMCCurve.PERCENTIS_75)
        percentis_85 = self.make(IMCCurve.PERCENTIS_85)
        percentis_90 = self.make(IMCCurve.PERCENTIS_90)
        percentis_95 = self.make(IMCCurve.PERCENTIS_95)

        for age in ages:
            age -= 2

            array_data_table.append([
                ages[age],
                percentis_5[age],
                percentis_10[age],
                percentis_25[age],
                percentis_50[age],
                percentis_75[age],
                percentis_85[age],
                percentis_90[age],
                percentis_95[age],
            ])

        for i in range(len(array_data_table)):
            if i == 0:
                continue
            array_data_table[i].append(0.0)

        return array_data_table

    def result(self, imc, age):
        """
        Check the chart if the child is above, below or at the mean IMC.
        """

        success = True
        result = 0

        if age < 2 or age > 18:
            success = False

        if not success:
            result = "Invalid age"
            return result

        if imc < self.curve.percentis_5[age - 2]:
            result = -1

        if imc > self.curve.percentis_95[age - 2]:
            result = 1

        return result
