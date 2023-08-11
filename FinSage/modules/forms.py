from django import forms


class QuestionsForm(forms.Form):
    q0 = forms.ChoiceField(
        label='Q1 What is the primary purpose of budgeting?',
        choices=(
            ('1', "To plan and manage finances"),
            ('0', "To restrict financial freedom"),
            ('0', "To track daily expenses"),
            ('0', "I don't know :("),
        )
    )
    q1 = forms.ChoiceField(
        label='Q2 Which of the following best describes a "fixed expense" in a budget?',
        choices=(
            ('0', "An expense that can be easily cut from the budget"),
            ('1', "An expense that remains relatively constant each month"),
            ('0', "An expense that varies from month to month"),
            ('0', "I don't know :("),
        )
    )
    q2 = forms.ChoiceField(
        label='Q3 What does a budget deficit occur when:',
        choices=(
            ('0', " Income equals expenses"),
            ('1', "Expenses exceed income"),
            ('0', "Income exceeds expenses"),
            ('0', "I don't know :("),
        )
    )
    q3 = forms.ChoiceField(
        label='Q4 Which of the following is a key advantage of digital payments?',
        choices=(
            ('0', "Limited accessibility"),
            ('0', "Requirement of physical presence"),
            ('1', "Convenience and speed"),
            ('0', "I don't know :("),
        )
    )
    q4 = forms.ChoiceField(
        label='Q5  What is the primary function of a mobile wallet in digital payments?',
        choices=(
            ('0', "Storing digital photos"),
            ('1', "Storing and managing payment information"),
            ('0', "Sending text messages"),
            ('0', "I don't know :("),
        )
    )
    q5 = forms.ChoiceField(
        label='Q6 Which type of digital payment involves scanning a Quick Response (QR) code to initiate a transaction?',
        choices=(
            ('0', "Online banking"),
            ('0', "Mobile banking"),
            ('1', "Contactless payment"),
            ('0', "I don't know :("),
        )
    )
    q6 = forms.ChoiceField(
        label='Q7 What is the primary purpose of setting financial goals?',
        choices=(
            ('1', "To have a clear direction for managing finances"),
            ('0', "To compare with others' goals"),
            ('0', "To predict future economic trends"),
            ('0', "I don't know :("),
        )
    )
    q7 = forms.ChoiceField(
        label='Q8. Which of the following is a characteristic of a well-defined financial goal?',
        choices=(
            ('0', "Unrealistic and unattainable target"),
            ('1', "Specific, measurable, and time-bound"),
            ('0', "Ignoring current financial situation"),
            ('0', "I don't know :("),
        )
    )
    q8 = forms.ChoiceField(
        label='Q9 What is an "emergency fund" in the context of financial goal setting?',
        choices=(
            ('1', "Reserve funds for unexpected expenses"),
            ('0', "Money set aside for vacation expenses"),
            ('0', "Savings earmarked for retirement"),
            ('0', "I don't know :("),
        )
    )
    q9 = forms.ChoiceField(
        label='Q10 What is a mutual fund?',
        choices=(
            ('0', "A type of bank account"),
            ('1', "A pool of funds from multiple investors to invest in various securities"),
            ('0', "A government savings bond"),
            ('0', "I don't know :("),
        )
    )
    q10 = forms.ChoiceField(
        label='Q11 How are mutual fund returns generated?',
        choices=(
            ('0', "By offering fixed interest rates"),
            ('1', "Through a combination of capital gains, dividends, and interest earned by the fund"),
            ('0', "Through speculation on individual stocks"),
            ('0', "I don't know :("),
        )
    )
    q11 = forms.ChoiceField(
        label='Q12 What is a "net asset value" (NAV) of a mutual fund?',
        choices=(
            ('0', "The fund manager's salary"),
            ('0', "Through a combination of capital gains, dividends, and interest earned by the fund"),
            ('1', "The number of investors in the fund"),
            ('0', "I don't know :("),
        )
    )
    q12 = forms.ChoiceField(
        label='Q13 What does the term "stock" represent in the stock market?',
        choices=(
            ('0', "A type of bond issued by a corporation"),
            ('0', "Physical assets owned by investors"),
            ('0', "I dont know"),
            ('1', "Ownership interest in a company"),
        )
    )
    q13 = forms.ChoiceField(
        label='Q14 What is the primary function of a stock exchange?',
        choices=(
            ('1', "Facilitating trading of stocks and other securities"),
            ('0', "Providing loans to businesses"),
            ('0', "I dont know"),
            ('0', "Offering insurance services"),
        )
    )
    q14 = forms.ChoiceField(
        label='Q15 What is the significance of a stocks "ticker symbol"?',
        choices=(
            ('0', "It indicates the stock's face value"),
            ('1', " It uniquely identifies a specific stock for trading purposes"),
            ('0', "I dont know"),
            ('0', "It represents the stock's historical performance"),
        )
    )
    q15 = forms.ChoiceField(
        label='Q16 What is the purpose of retirement planning?',
        choices=(
            ('0', "To spend all savings before retirement"),
            ('1', " To ensure a steady income during retirement years"),
            ('0', "I dont know"),
            ('0', "To avoid financial planning altogether"),
        )
    )
    q16 = forms.ChoiceField(
        label='Q17 What is a 401(k) plan?',
        choices=(
            ('1', "A retirement savings plan offered by employers"),
            ('0', " A form of real estate investment"),
            ('0', "I dont know"),
            ('0', "A type of credit card for retirees"),
        )
    )
    q17 = forms.ChoiceField(
        label='Q18 What is the "retirement age" in most Western countries?',
        choices=(
            ('0', "I dont know"),
            ('0', " 50"),
            ('0', "55"),
            ('1', "65"),
        )
    )

    