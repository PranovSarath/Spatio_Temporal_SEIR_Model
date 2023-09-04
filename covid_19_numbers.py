from requests import get
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def fn_get_COVID19_London_data(url):
    response = get(url, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()["data"]



def fn_generateSEIRHD_data(data, N=9213021, p=5, recovery_duration = 14):

    sorted_data = sorted(data, key=lambda x: x['date'])
    dates = [entry["date"] for entry in sorted_data]
    new_infections = [entry.get("newCases", 0) or 0  for entry in sorted_data]
    cumulative_infections = [entry.get("cumulativeCases", 0) or 0 for entry in sorted_data]
    cumulative_deaths = [entry.get("cumulativeDeaths", 0) or 0 for entry in sorted_data]
    new_deaths = [entry.get("newDeaths", 0) or 0 for entry in sorted_data]
    icu_hospitalised = [entry.get("dailyHospitalised", 0) or 0 for entry in sorted_data]

    

    # Calculate E, I, D
    I_cumulative = [cases for cases in cumulative_infections]
    I_daily = [cases for cases in new_infections]
    D_cumulative = cumulative_deaths.copy()
    D_daily = [case for case in new_deaths]
    E = [p * new_case for new_case in new_infections]
    H = icu_hospitalised.copy()

    # Estimate Recovered based on past new cases (barring deaths)
    cumulative_recovered = [0] * len(dates)
    new_recovered = [0] * len(dates)
    for i in range(len(dates)):
        if i >= recovery_duration:
            new_recovered[i] = new_infections[i - recovery_duration] - sum(D_daily[i-recovery_duration:i])
            cumulative_recovered[i] = cumulative_recovered[i - 1] + new_recovered[i]
        else:
            cumulative_recovered[i] = 0
            new_recovered[i] = 0
    #Calculate R
    R = new_recovered.copy()
    #R = cumulative_recovered.copy()

    #Calculate S
    S = [N - (inf + exp + recov + dead + hosp) for exp, inf, recov, dead, hosp in zip(E,I_daily, R, D_daily, H )]
    return dates, S, E, I_cumulative, I_daily, R, H, D_cumulative, D_daily

