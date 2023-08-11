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
        label='Category',
        choices=(
            ('0', "Gen"),
            ('1', "ST"),
            ('0', "To track daily expenses"),
            ('0', "I don't know :("),
        )
    )
    q6 = forms.ChoiceField(
        label='Category',
        choices=(
            ('0', "Gen"),
            ('1', "ST"),
            ('0', "To track daily expenses"),
            ('0', "I don't know :("),
        )
    )
    q7 = forms.ChoiceField(
        label='Category',
        choices=(
            ('0', "Gen"),
            ('1', "ST"),
            ('0', "To track daily expenses"),
            ('0', "I don't know :("),
        )
    )
    q8 = forms.ChoiceField(
        label='Category',
        choices=(
            ('0', "Gen"),
            ('1', "ST"),
            ('0', "To track daily expenses"),
            ('0', "I don't know :("),
        )
    )
    q9 = forms.ChoiceField(
        label='Category',
        choices=(
            ('0', "Gen"),
            ('1', "ST"),
            ('0', "To track daily expenses"),
            ('0', "I don't know :("),
        )
    )