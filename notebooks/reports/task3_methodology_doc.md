# Task 3: Event Impact Modeling Methodology & Validation

## 1. Functional Form & Lag Specifications
Event impacts are modeled using a non-linear S-curve (logistic adoption decay) defined as:
$$I(t) = \frac{M}{1 + e^{-k(t - t_0)}}$$
where $M$ is the maximum structural magnitude, $k$ is the adoption velocity, and $t_0$ represents the lag onset period (typically 6-12 months post-launch).

## 2. Association Matrix
The impact matrix maps macro structural policy shifts (Fayda ID, Telebirr, FX Reform) to World Bank Findex indicators (`ACC_OWNERSHIP`, `ACC_MM_ACCOUNT`, `USG_DIGITAL_PAYMENT`).

## 3. Validation & Uncertainty
* **Telebirr Historical Benchmark:** Mobile money accounts grew from 4.7% in 2021 to 9.45% in 2024 (+4.75%). The model predicted +4.75% impact, achieving high alignment with empirical data.
* **Key Limitations:** Compounding multi-event interactions (e.g., Fayda rollout occurring simultaneously with M-Pesa entry) introduce collinearity risks that require ongoing observation.
