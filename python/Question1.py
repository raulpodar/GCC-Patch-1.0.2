# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    deposit=0.1*initialLevelOfDebt
    answer=deposit
    initialDebt=initialLevelOfDebt
    count=0
    while(initialLevelOfDebt>=50):
        if(initialLevelOfDebt<50) :monthlyRepayment=initialLevelOfDebt
        else: monthlyRepayment=initialDebt*(repaymentPercentage/100)
        count+=1
        debtAfterinterestPercentage=initialLevelOfDebt*(interestPercentage/100)+initialLevelOfDebt
        initialLevelOfDebt=debtAfterinterestPercentage-monthlyRepayment
        answer+=monthlyRepayment
    answer=initialLevelOfDebt+answer
    return answer
