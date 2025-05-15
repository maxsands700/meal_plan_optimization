def calc_EER(age, height, weight, gender, activity_level):
    """
    Calculate Estimated Energy Requirements (EER) based on age, height, weight, gender, and activity level, for humans 14 years and older.
    This function is based off - National Academies of Sciences, Engineering, and Medicine. 2023. Dietary Reference Intakes for Energy. Washington, DC: The National Academies Press.
    https://doi.org/10.17226/26818.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    height : float
        Height in centimeters
    weight : float
        Weight in kilograms
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'

    Returns:
    --------
    float : Estimated Energy Requirements in kcal/day
    """
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")

    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")

    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")

    # Adolescents (14-18.99 years)
    if 14 <= age < 19:
        # Male Equations
        if gender == 'M':
            if activity_level == 'inactive':
                return -447.51 + (3.68 * age) + (13.01 * height) + (13.15 * weight) + 20
            elif activity_level == 'low_active':
                return 19.12 + (3.68 * age) + (8.62 * height) + (20.28 * weight) + 20
            elif activity_level == 'active':
                return -388.19 + (3.68 * age) + (12.66 * height) + (20.46 * weight) + 20
            elif activity_level == 'very_active':
                return -671.75 + (3.68 * age) + (15.38 * height) + (23.25 * weight) + 20

        # Female Equations
        elif gender == 'F':
            if activity_level == 'inactive':
                return 55.59 - (22.25 * age) + (8.43 * height) + (17.07 * weight) + 20
            elif activity_level == 'low_active':
                return -297.54 - (22.25 * age) + (12.77 * height) + (14.73 * weight) + 20
            elif activity_level == 'active':
                return -189.55 - (22.25 * age) + (11.74 * height) + (18.34 * weight) + 20
            elif activity_level == 'very_active':
                return -709.59 - (22.25 * age) + (18.22 * height) + (14.25 * weight) + 20

    # Adults (19+ years)
    else:
        # Male Equations
        if gender == 'M':
            if activity_level == 'inactive':
                return 753.07 - (10.83 * age) + (6.50 * height) + (14.10 * weight)
            elif activity_level == 'low_active':
                return 581.47 - (10.83 * age) + (8.30 * height) + (14.94 * weight)
            elif activity_level == 'active':
                return 1004.82 - (10.83 * age) + (6.52 * height) + (15.91 * weight)
            elif activity_level == 'very_active':
                return -517.88 - (10.83 * age) + (15.61 * height) + (19.11 * weight)

        # Female Equations
        elif gender == 'F':
            if activity_level == 'inactive':
                return 584.90 - (7.01 * age) + (5.72 * height) + (11.71 * weight)
            elif activity_level == 'low_active':
                return 575.77 - (7.01 * age) + (6.60 * height) + (12.14 * weight)
            elif activity_level == 'active':
                return 710.25 - (7.01 * age) + (6.54 * height) + (12.34 * weight)
            elif activity_level == 'very_active':
                return 511.83 - (7.01 * age) + (9.07 * height) + (12.56 * weight)
