def calc_EER(age: float, height: float, weight: float, gender: str, activity_level: str) -> float:
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

    """
    Generate a nutritional outline for Vitamin A with recommended intake, lower limit, and upper limit.

    Args:
        age (float, optional): Age in years (default: None, uses adult average)
        gender (str, optional): 'M' for male, 'F' for female (default: None, uses male)
        activity_level (str, optional): Not used for Vitamin A, included for consistency
        eer (float, optional): Estimated Energy Requirement in kcal/day (default: None, not used)

    Returns:
        dict: Dictionary with keysrecommended_intake, lower_limit, upper_limit (in µg RAE)
    """
    # Default values if arguments are not provided
    # Use adult male (19-30 years) as default for broadest applicability
    if age is None:
        age = 25  # Midpoint of 19-30 years, common adult range
    if gender is None:
        gender = 'M'  # Male as default, aligns with higher nutrient needs

    # Determine age group for DRI lookup
    # Based on IOM age categories for Vitamin A
    if age <= 3:
        age_group = '1-3'
        eff_gender = 'both'
    elif age <= 8:
        age_group = '4-8'
        eff_gender = 'both'
    elif age <= 13:
        age_group = '9-13'
        eff_gender = gender
    elif age <= 18:
        age_group = '14-18'
        eff_gender = gender
    elif age <= 30:
        age_group = '19-30'
        eff_gender = gender
    elif age <= 50:
        age_group = '31-50'
        eff_gender = gender
    elif age <= 70:
        age_group = '51-70'
        eff_gender = gender
    else:
        age_group = '>70'
        eff_gender = gender

    # Vitamin A data (µg RAE) from IOM DRI tables
    # RDA: Recommended intake for 97-98% of healthy individuals
    # EAR: Meets needs of 50% of individuals, used as lower limit
    # UL: Maximum safe intake to avoid toxicity
    vitamin_a_data = {
        ('1-3', 'both'): {'RDA': 300, 'EAR': 210, 'UL': 600},
        ('4-8', 'both'): {'RDA': 400, 'EAR': 275, 'UL': 900},
        ('9-13', 'M'): {'RDA': 600, 'EAR': 445, 'UL': 1700},
        ('9-13', 'F'): {'RDA': 600, 'EAR': 420, 'UL': 1700},
        ('14-18', 'M'): {'RDA': 900, 'EAR': 630, 'UL': 2800},
        ('14-18', 'F'): {'RDA': 700, 'EAR': 485, 'UL': 2800},
        ('19-30', 'M'): {'RDA': 900, 'EAR': 625, 'UL': 3000},
        ('19-30', 'F'): {'RDA': 700, 'EAR': 500, 'UL': 3000},
        ('31-50', 'M'): {'RDA': 900, 'EAR': 625, 'UL': 3000},
        ('31-50', 'F'): {'RDA': 700, 'EAR': 500, 'UL': 3000},
        ('51-70', 'M'): {'RDA': 900, 'EAR': 625, 'UL': 3000},
        ('51-70', 'F'): {'RDA': 700, 'EAR': 500, 'UL': 3000},
        ('>70', 'M'): {'RDA': 900, 'EAR': 625, 'UL': 3000},
        ('>70', 'F'): {'RDA': 700, 'EAR': 500, 'UL': 3000}
    }

    # Retrieve Vitamin A values for the age group and gender
    # If age/gender combo not found, default to adult male (19-30)
    try:
        data = vitamin_a_data[(age_group, eff_gender)]
    except KeyError:
        data = vitamin_a_data[('19-30', 'M')]

    # Assign values
    recommended_intake = data['RDA']  # RDA for optimal health
    lower_limit = data['EAR']  # EAR to avoid inadequacy
    upper_limit = data['UL']   # UL to prevent toxicity

    # Activity level and EER not used for Vitamin A
    # IOM DRIs for Vitamin A are based solely on age and gender, as needs
    # (e.g., for vision, immunity) are not energy-dependent

    return {
        'recommended_intake': float(recommended_intake),
        'lower_limit': float(lower_limit),
        'upper_limit': float(upper_limit)
    }


def generate_carbohydrates_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a carbohydrates intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, and upper limit in grams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store carbohydrate recommendations
    carbs_outline = {
        'recommended_intake': round(.55 * eer / 4),
        'lower_limit': round(.45 * eer / 4),
        'upper_limit': round(.65 * eer / 4),
        'units': 'g'
    }

    return carbs_outline


def generate_fiber_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a fiber intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, and upper limit in grams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store fiber recommendations
    fiber_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'g'
    }

    # Base fiber requirements using Adequate Intake (AI)
    # Source: National Academies of Sciences, Dietary Reference Intakes for Energy, Carbohydrate, Fiber, Fat, Fatty Acids, Cholesterol, Protein, and Amino Acids
    # AI based on age and gender, set to promote heart health and digestive function
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            fiber_outline['recommended_intake'] = 38
            # ~80% of AI, minimum for health benefits
            fiber_outline['lower_limit'] = 30
        else:  # Female
            # AI for females 14-18 years
            fiber_outline['recommended_intake'] = 26
            fiber_outline['lower_limit'] = 21        # ~80% of AI
    else:  # Age 19+
        if gender == 'M':
            # AI for males 19-50 years, reduced to 21 for 51+
            fiber_outline['recommended_intake'] = 30
            fiber_outline['lower_limit'] = 24        # ~80% of AI
            if age > 50:
                fiber_outline['recommended_intake'] = 21
                fiber_outline['lower_limit'] = 17
        else:  # Female
            # AI for females 19-50 years, reduced to 14 for 51+
            fiber_outline['recommended_intake'] = 21
            fiber_outline['lower_limit'] = 17        # ~80% of AI
            if age > 50:
                fiber_outline['recommended_intake'] = 14
                fiber_outline['lower_limit'] = 11

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase gut motility and energy needs, slightly increasing fiber needs
    # Adjustments are modest to avoid digestive discomfort
    activity_multipliers = {
        'inactive': 0.95,
        'low_active': 1.0,
        'active': 1.1,
        'very_active': 1.2
    }
    fiber_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Further adjust based on EER using guideline of 14 g fiber per 1000 kcal
    # Rationale: Fiber needs correlate with energy intake for balanced digestion
    eer_based_fiber = (eer / 1000) * 14
    fiber_outline['recommended_intake'] = max(
        fiber_outline['recommended_intake'], eer_based_fiber)

    # Round recommended intake to nearest integer for practicality
    fiber_outline['recommended_intake'] = round(
        fiber_outline['recommended_intake'])

    # Set upper limit
    # Rationale: No formal UL exists for fiber, but excessive intake may cause digestive issues
    # Set at 1.5x recommended intake to allow flexibility while preventing discomfort
    fiber_outline['upper_limit'] = round(
        1.5 * fiber_outline['recommended_intake'])

    return fiber_outline


def generate_protein_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a protein intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, and upper limit in grams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store protein recommendations
    protein_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'g'
    }

    # Base protein requirements using RDA (Recommended Dietary Allowance)
    # Source: National Academies of Sciences, Dietary Reference Intakes for Protein
    # RDA is 0.8 g/kg body weight for adults, higher for adolescents
    # Lower limit uses Estimated Average Requirement (EAR), upper limit based on safe intake ranges
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            protein_outline['recommended_intake'] = 52
            # EAR for males 14-18 years
            protein_outline['lower_limit'] = 43
        else:  # Female
            # RDA for females 14-18 years
            protein_outline['recommended_intake'] = 46
            # EAR for females 14-18 years
            protein_outline['lower_limit'] = 38
    else:  # Age 19+
        if gender == 'M':
            # RDA for males 19+ years
            protein_outline['recommended_intake'] = 56
            # EAR for males 19+ years
            protein_outline['lower_limit'] = 46
        else:  # Female
            # RDA for females 19+ years
            protein_outline['recommended_intake'] = 46
            # EAR for females 19+ years
            protein_outline['lower_limit'] = 38

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels, especially 'active' and 'very_active', increase protein needs
    # for muscle repair and maintenance. Adjustments follow sports nutrition guidelines (1.2-2.0 g/kg).
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.1,
        'active': 1.3,
        'very_active': 1.5
    }
    protein_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Further adjust based on EER to account for higher energy needs
    # Rationale: Individuals with higher EER may require more protein to support energy expenditure
    # Reference EER: 2500 kcal for males, 2000 kcal for females
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.2, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-120%
    protein_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    protein_outline['recommended_intake'] = round(
        protein_outline['recommended_intake'])

    # Set upper limit based on safe intake levels
    # Rationale: Upper limit is set at 2.0 g/kg body weight or 35% of energy intake to prevent
    # potential health risks (e.g., kidney strain, nutrient imbalance)
    # Since weight is not provided, use a conservative estimate based on age and gender
    estimated_weight = 70 if gender == 'M' else 57  # Average weights for adults
    if 14 <= age <= 18:
        estimated_weight = 60 if gender == 'M' else 50  # Average weights for adolescents
    protein_outline['upper_limit'] = round(2.0 * estimated_weight)

    # Ensure upper limit is at least 2x recommended intake for safety
    protein_outline['upper_limit'] = max(protein_outline['upper_limit'],
                                         2 * protein_outline['recommended_intake'])

    return protein_outline


def generate_fat_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a fat intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, and upper limit in grams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store fat recommendations
    fat_outline = {
        'recommended_intake': round(.275 * eer / 9),
        'lower_limit': round(.2 * eer / 9),
        'upper_limit': round(.35 * eer / 9),
        'units': 'g'
    }

    return fat_outline


def generate_vitamin_a_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin A intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, and upper limit in micrograms RAE (Retinol Activity Equivalents) per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin A recommendations
    vitamin_a_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Vitamin A Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            vitamin_a_outline['recommended_intake'] = 900
            # Estimated Average Requirement (EAR), ~70% of RDA
            vitamin_a_outline['lower_limit'] = 630
        else:  # Female
            # RDA for females 14-18 years
            vitamin_a_outline['recommended_intake'] = 700
            vitamin_a_outline['lower_limit'] = 485       # EAR, ~70% of RDA
    else:  # Age 19+
        if gender == 'M':
            # RDA for males 19+ years
            vitamin_a_outline['recommended_intake'] = 900
            vitamin_a_outline['lower_limit'] = 625       # EAR, ~70% of RDA
        else:  # Female
            # RDA for females 19+ years
            vitamin_a_outline['recommended_intake'] = 700
            vitamin_a_outline['lower_limit'] = 500       # EAR, ~70% of RDA

    # Adjust recommended intake slightly based on activity level and EER
    # Rationale: Higher energy expenditure may increase oxidative stress, potentially increasing Vitamin A needs
    # Adjustment is conservative (up to 10% increase) to avoid toxicity risks
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.06,
        'very_active': 1.1
    }
    vitamin_a_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Further adjust based on EER relative to a reference (2000 kcal for females, 2500 kcal for males)
    # This accounts for higher needs in individuals with significantly higher energy expenditure
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.15, max(0.85, eer / reference_eer)
                         )  # Cap adjustment between 85-115%
    vitamin_a_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    vitamin_a_outline['recommended_intake'] = round(
        vitamin_a_outline['recommended_intake'])

    # Set lower limit as EAR (already set above), no further adjustment needed
    # Lower limit represents minimum to prevent deficiency in most individuals

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # UL is the same for both genders and not adjusted by activity or EER to prevent toxicity
    if 14 <= age <= 18:
        vitamin_a_outline['upper_limit'] = 2800  # UL for 14-18 years
    else:
        vitamin_a_outline['upper_limit'] = 3000  # UL for 19+ years

    # Round limits to nearest integer for practicality
    vitamin_a_outline['recommended_intake'] = round(
        vitamin_a_outline['recommended_intake'])
    vitamin_a_outline['lower_limit'] = round(
        vitamin_a_outline['lower_limit'])
    vitamin_a_outline['upper_limit'] = round(
        vitamin_a_outline['upper_limit'])

    return vitamin_a_outline


def generate_vitamin_c_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin C intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin C recommendations
    vitamin_c_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Vitamin C Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin C
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            vitamin_c_outline['recommended_intake'] = 75
            vitamin_c_outline['lower_limit'] = 63         # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 14-18 years
            vitamin_c_outline['recommended_intake'] = 65
            vitamin_c_outline['lower_limit'] = 56         # EAR, ~85% of RDA
    else:  # Age 19+
        if gender == 'M':
            # RDA for males 19+ years
            vitamin_c_outline['recommended_intake'] = 90
            vitamin_c_outline['lower_limit'] = 75         # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 19+ years
            vitamin_c_outline['recommended_intake'] = 75
            vitamin_c_outline['lower_limit'] = 60         # EAR, ~85% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase oxidative stress, potentially increasing Vitamin C needs
    # Adjustments are conservative (up to 15% increase) to stay within safe limits
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    vitamin_c_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Further adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased antioxidant needs
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.1, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-110%
    vitamin_c_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    vitamin_c_outline['recommended_intake'] = round(
        vitamin_c_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders and not adjusted to prevent adverse effects (e.g., diarrhea)
    if 14 <= age <= 18:
        vitamin_c_outline['upper_limit'] = 1800  # UL for 14-18 years
    else:
        vitamin_c_outline['upper_limit'] = 2000  # UL for 19+ years

    return vitamin_c_outline


def generate_vitamin_d_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin D intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin D recommendations
    vitamin_d_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Vitamin D Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Calcium and Vitamin D
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    # RDA is 15 µg/day (600 IU) for ages 14-70, 20 µg/day (800 IU) for 71+
    if 14 <= age <= 70:
        vitamin_d_outline['recommended_intake'] = 15  # RDA for ages 14-70
        vitamin_d_outline['lower_limit'] = 10        # EAR, ~67% of RDA
    else:  # Age 71+
        vitamin_d_outline['recommended_intake'] = 20  # RDA for ages 71+
        # EAR, remains at 10 µg/day
        vitamin_d_outline['lower_limit'] = 10

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels, especially outdoor activities, may increase sun exposure,
    # potentially reducing dietary Vitamin D needs, but conservative increase applied for safety
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    vitamin_d_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased metabolic needs,
    # but Vitamin D needs are less directly tied to EER, so adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.1, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-110%
    vitamin_d_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    vitamin_d_outline['recommended_intake'] = round(
        vitamin_d_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders and not adjusted to prevent toxicity (e.g., hypercalcemia)
    if 14 <= age <= 18:
        vitamin_d_outline['upper_limit'] = 100  # UL for 14-18 years
    else:
        vitamin_d_outline['upper_limit'] = 100  # UL for 19+ years

    return vitamin_d_outline


def generate_vitamin_b6_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin B6 intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin B6 recommendations
    vitamin_b6_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Vitamin B6 Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            vitamin_b6_outline['recommended_intake'] = 1.3
            vitamin_b6_outline['lower_limit'] = 1.1        # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 14-18 years
            vitamin_b6_outline['recommended_intake'] = 1.2
            vitamin_b6_outline['lower_limit'] = 1.0        # EAR, ~85% of RDA
    elif 19 <= age <= 50:
        if gender == 'M':
            # RDA for males 19-50 years
            vitamin_b6_outline['recommended_intake'] = 1.3
            vitamin_b6_outline['lower_limit'] = 1.1        # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 19-50 years
            vitamin_b6_outline['recommended_intake'] = 1.3
            vitamin_b6_outline['lower_limit'] = 1.1        # EAR, ~85% of RDA
    else:  # Age 51+
        if gender == 'M':
            # RDA for males 51+ years
            vitamin_b6_outline['recommended_intake'] = 1.7
            vitamin_b6_outline['lower_limit'] = 1.4        # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 51+ years
            vitamin_b6_outline['recommended_intake'] = 1.5
            vitamin_b6_outline['lower_limit'] = 1.3        # EAR, ~85% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase protein metabolism, slightly increasing Vitamin B6 needs
    # Adjustments are conservative (up to 10% increase) to stay within safe limits
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    vitamin_b6_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may increase metabolic demands, but B6 needs are less directly tied to EER
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    vitamin_b6_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    vitamin_b6_outline['recommended_intake'] = round(
        vitamin_b6_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders and not adjusted to prevent adverse effects (e.g., neuropathy)
    # UL for ages 19+ (also applied to 14-18 for simplicity)
    vitamin_b6_outline['upper_limit'] = 100

    return vitamin_b6_outline


def generate_vitamin_e_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin E intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams per day.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin E recommendations
    vitamin_e_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Vitamin E Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin C, Vitamin E, Selenium, and Carotenoids
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        vitamin_e_outline['recommended_intake'] = 15  # RDA for ages 14-18
        vitamin_e_outline['lower_limit'] = 12        # EAR, ~80% of RDA
    else:  # Age 19+
        vitamin_e_outline['recommended_intake'] = 15  # RDA for ages 19+
        vitamin_e_outline['lower_limit'] = 12        # EAR, ~80% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase oxidative stress, potentially increasing Vitamin E needs
    # Adjustments are conservative (up to 10% increase) to stay within safe limits
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    vitamin_e_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may increase antioxidant needs, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    vitamin_e_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    vitamin_e_outline['recommended_intake'] = round(
        vitamin_e_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders and not adjusted to prevent adverse effects (e.g., bleeding risk)
    # UL for ages 19+ (applied to 14-18 for consistency)
    vitamin_e_outline['upper_limit'] = 1000

    return vitamin_e_outline


def generate_vitamin_k_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin K intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin K recommendations
    vitamin_k_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Vitamin K Adequate Intake (AI) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            vitamin_k_outline['recommended_intake'] = 75
            # ~80% of AI, estimated minimum
            vitamin_k_outline['lower_limit'] = 60
        else:  # Female
            # AI for females 14-18 years
            vitamin_k_outline['recommended_intake'] = 75
            vitamin_k_outline['lower_limit'] = 60        # ~80% of AI
    else:  # Age 19+
        if gender == 'M':
            # AI for males 19+ years
            vitamin_k_outline['recommended_intake'] = 120
            vitamin_k_outline['lower_limit'] = 96         # ~80% of AI
        else:  # Female
            # AI for females 19+ years
            vitamin_k_outline['recommended_intake'] = 90
            vitamin_k_outline['lower_limit'] = 72         # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase minor injury risk, slightly increasing Vitamin K needs for clotting
    # Adjustments are minimal (up to 5% increase) as needs are relatively stable
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    vitamin_k_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Vitamin K needs are not strongly tied to energy intake, but slight adjustment for consistency
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    vitamin_k_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    vitamin_k_outline['recommended_intake'] = round(
        vitamin_k_outline['recommended_intake'])

    # Set upper limit
    # Rationale: No UL established for Vitamin K due to low toxicity risk; set at 3x recommended intake for safety
    vitamin_k_outline['upper_limit'] = 3 * \
        vitamin_k_outline['recommended_intake']

    return vitamin_k_outline


def generate_thiamin_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Thiamin intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Thiamin recommendations
    thiamin_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Thiamin Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            thiamin_outline['recommended_intake'] = 1.2
            thiamin_outline['lower_limit'] = 1.0        # EAR, ~83% of RDA
        else:  # Female
            # RDA for females 14-18 years
            thiamin_outline['recommended_intake'] = 1.0
            thiamin_outline['lower_limit'] = 0.9        # EAR, ~90% of RDA
    else:  # Age 19+
        if gender == 'M':
            # RDA for males 19+ years
            thiamin_outline['recommended_intake'] = 1.2
            thiamin_outline['lower_limit'] = 1.0        # EAR, ~83% of RDA
        else:  # Female
            # RDA for females 19+ years
            thiamin_outline['recommended_intake'] = 1.1
            thiamin_outline['lower_limit'] = 0.9        # EAR, ~82% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase carbohydrate metabolism, slightly increasing thiamin needs
    # Adjustments are conservative (up to 15% increase) as thiamin needs are closely tied to energy intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    thiamin_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Thiamin needs are proportional to energy intake, especially carbohydrate metabolism
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.2, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-120%
    thiamin_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    thiamin_outline['recommended_intake'] = round(
        thiamin_outline['recommended_intake'], 1)

    # Set upper limit
    # Rationale: No UL established for thiamin due to low toxicity risk; set at 5x recommended intake for safety
    thiamin_outline['upper_limit'] = round(
        5 * thiamin_outline['recommended_intake'], 1)

    return thiamin_outline


def generate_vitamin_b12_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Vitamin B12 intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Vitamin B12 recommendations
    vitamin_b12_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Vitamin B12 Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    vitamin_b12_outline['recommended_intake'] = 2.4  # RDA for ages 14+
    vitamin_b12_outline['lower_limit'] = 2.0        # EAR, ~83% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels may slightly increase metabolic demands, but B12 needs are stable
    # Adjustments are minimal (up to 5% increase) as requirements are not strongly tied to activity
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    vitamin_b12_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: B12 needs are not directly tied to energy intake, but slight adjustment for consistency
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    vitamin_b12_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    vitamin_b12_outline['recommended_intake'] = round(
        vitamin_b12_outline['recommended_intake'], 1)

    # Set upper limit
    # Rationale: No UL established for Vitamin B12 due to low toxicity risk; set at 10x recommended intake for safety
    vitamin_b12_outline['upper_limit'] = round(
        10 * vitamin_b12_outline['recommended_intake'], 1)

    return vitamin_b12_outline


def generate_riboflavin_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Riboflavin intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Riboflavin recommendations
    riboflavin_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Riboflavin Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            riboflavin_outline['recommended_intake'] = 1.3
            riboflavin_outline['lower_limit'] = 1.1        # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 14-18 years
            riboflavin_outline['recommended_intake'] = 1.0
            riboflavin_outline['lower_limit'] = 0.9        # EAR, ~90% of RDA
    else:  # Age 19+
        if gender == 'M':
            # RDA for males 19+ years
            riboflavin_outline['recommended_intake'] = 1.3
            riboflavin_outline['lower_limit'] = 1.1        # EAR, ~85% of RDA
        else:  # Female
            # RDA for females 19+ years
            riboflavin_outline['recommended_intake'] = 1.1
            riboflavin_outline['lower_limit'] = 0.9        # EAR, ~82% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase energy metabolism, slightly increasing riboflavin needs
    # Adjustments are conservative (up to 15% increase) as needs are tied to energy expenditure
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    riboflavin_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Riboflavin needs are proportional to energy metabolism, especially in active individuals
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.2, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-120%
    riboflavin_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    riboflavin_outline['recommended_intake'] = round(
        riboflavin_outline['recommended_intake'], 1)

    # Set upper limit
    # Rationale: No UL established for riboflavin due to low toxicity risk; set at 5x recommended intake for safety
    riboflavin_outline['upper_limit'] = round(
        5 * riboflavin_outline['recommended_intake'], 1)

    return riboflavin_outline


def generate_folate_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Folate intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Folate recommendations
    folate_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Folate Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # RDA values are set to meet the needs of 97-98% of healthy individuals, in Dietary Folate Equivalents (DFE)
    if 14 <= age <= 18:
        # RDA for males and females 14-18 years
        folate_outline['recommended_intake'] = 400
        folate_outline['lower_limit'] = 320        # EAR, ~80% of RDA
    else:  # Age 19+
        # RDA for males and females 19+ years
        folate_outline['recommended_intake'] = 400
        folate_outline['lower_limit'] = 320        # EAR, ~80% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase cell turnover and DNA synthesis, slightly increasing folate needs
    # Adjustments are conservative (up to 10% increase) to stay within safe limits
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    folate_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may increase metabolic demands, but folate needs are less directly tied to EER
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    folate_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    folate_outline['recommended_intake'] = round(
        folate_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent masking B12 deficiency or neurological issues
    if 14 <= age <= 18:
        folate_outline['upper_limit'] = 800  # UL for 14-18 years
    else:
        folate_outline['upper_limit'] = 1000  # UL for 19+ years

    return folate_outline


def generate_niacin_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Niacin intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Niacin recommendations
    niacin_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Niacin Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # RDA values are set to meet the needs of 97-98% of healthy individuals, in Niacin Equivalents (NE)
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            niacin_outline['recommended_intake'] = 16
            niacin_outline['lower_limit'] = 12        # EAR, ~75% of RDA
        else:  # Female
            # RDA for females 14-18 years
            niacin_outline['recommended_intake'] = 14
            niacin_outline['lower_limit'] = 11        # EAR, ~79% of RDA
    else:  # Age 19+
        if gender == 'M':
            # RDA for males 19+ years
            niacin_outline['recommended_intake'] = 16
            niacin_outline['lower_limit'] = 12        # EAR, ~75% of RDA
        else:  # Female
            # RDA for females 19+ years
            niacin_outline['recommended_intake'] = 14
            niacin_outline['lower_limit'] = 11        # EAR, ~79% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase energy metabolism, slightly increasing niacin needs
    # Adjustments are conservative (up to 15% increase) as needs are tied to energy expenditure
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    niacin_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Niacin needs are proportional to energy metabolism, especially in active individuals
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.2, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-120%
    niacin_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    niacin_outline['recommended_intake'] = round(
        niacin_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., flushing)
    if 14 <= age <= 18:
        niacin_outline['upper_limit'] = 30  # UL for 14-18 years
    else:
        niacin_outline['upper_limit'] = 35  # UL for 19+ years

    return niacin_outline


def generate_choline_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Choline intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Choline recommendations
    choline_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Choline Adequate Intake (AI) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            choline_outline['recommended_intake'] = 550
            # ~80% of AI, estimated minimum
            choline_outline['lower_limit'] = 440
        else:  # Female
            # AI for females 14-18 years
            choline_outline['recommended_intake'] = 400
            choline_outline['lower_limit'] = 320        # ~80% of AI
    else:  # Age 19+
        if gender == 'M':
            # AI for males 19+ years
            choline_outline['recommended_intake'] = 550
            choline_outline['lower_limit'] = 440        # ~80% of AI
        else:  # Female
            # AI for females 19+ years
            choline_outline['recommended_intake'] = 425
            choline_outline['lower_limit'] = 340        # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase muscle and liver metabolism, slightly increasing choline needs
    # Adjustments are conservative (up to 10% increase) to stay within safe limits
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    choline_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may increase metabolic demands, but choline needs are less directly tied to EER
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    choline_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    choline_outline['recommended_intake'] = round(
        choline_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., hypotension, fishy odor)
    if 14 <= age <= 18:
        choline_outline['upper_limit'] = 3000  # UL for 14-18 years
    else:
        choline_outline['upper_limit'] = 3500  # UL for 19+ years

    return choline_outline


def generate_pantothenic_acid_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Pantothenic Acid intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Pantothenic Acid recommendations
    pantothenic_acid_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Pantothenic Acid Adequate Intake (AI) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals, same for both genders
    pantothenic_acid_outline['recommended_intake'] = 5  # AI for ages 14+
    # ~80% of AI, estimated minimum
    pantothenic_acid_outline['lower_limit'] = 4

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase energy metabolism, slightly increasing pantothenic acid needs
    # Adjustments are minimal (up to 10% increase) as needs are not strongly tied to activity
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    pantothenic_acid_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Pantothenic acid needs may scale slightly with energy metabolism, but adjustment is conservative
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    pantothenic_acid_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    pantothenic_acid_outline['recommended_intake'] = round(
        pantothenic_acid_outline['recommended_intake'], 1)

    # Set upper limit
    # Rationale: No UL established for pantothenic acid due to low toxicity risk; set at 5x recommended intake for safety
    pantothenic_acid_outline['upper_limit'] = round(
        5 * pantothenic_acid_outline['recommended_intake'], 1)

    return pantothenic_acid_outline


def generate_biotin_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Biotin intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Biotin recommendations
    biotin_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Biotin Adequate Intake (AI) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals, same for both genders
    if 14 <= age <= 18:
        biotin_outline['recommended_intake'] = 25  # AI for ages 14-18
        # ~80% of AI, estimated minimum
        biotin_outline['lower_limit'] = 20
    else:  # Age 19+
        biotin_outline['recommended_intake'] = 30  # AI for ages 19+
        biotin_outline['lower_limit'] = 24        # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may slightly increase metabolic demands, but biotin needs are relatively stable
    # Adjustments are minimal (up to 5% increase) as requirements are not strongly tied to activity
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    biotin_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Biotin needs are not directly tied to energy intake, but slight adjustment for consistency
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    biotin_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    biotin_outline['recommended_intake'] = round(
        biotin_outline['recommended_intake'])

    # Set upper limit
    # Rationale: No UL established for biotin due to low toxicity risk; set at 10x recommended intake for safety
    biotin_outline['upper_limit'] = 10 * biotin_outline['recommended_intake']

    return biotin_outline


def generate_calcium_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Calcium intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Calcium recommendations
    calcium_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Calcium Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Calcium and Vitamin D
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        calcium_outline['recommended_intake'] = 1300  # RDA for ages 14-18
        calcium_outline['lower_limit'] = 1000        # EAR, ~77% of RDA
    elif 19 <= age <= 50:
        calcium_outline['recommended_intake'] = 1000  # RDA for ages 19-50
        calcium_outline['lower_limit'] = 800         # EAR, ~80% of RDA
    else:  # Age 51+
        if gender == 'M' and age <= 70:
            calcium_outline['recommended_intake'] = 1000  # RDA for males 51-70
            calcium_outline['lower_limit'] = 800         # EAR, ~80% of RDA
        else:  # Females 51+ and males 71+
            # RDA for females 51+ and males 71+
            calcium_outline['recommended_intake'] = 1200
            calcium_outline['lower_limit'] = 1000        # EAR, ~83% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity, especially weight-bearing exercise, may increase bone stress, slightly increasing calcium needs
    # Adjustments are conservative (up to 10% increase) to avoid excessive intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    calcium_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased bone turnover, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    calcium_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    calcium_outline['recommended_intake'] = round(
        calcium_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., kidney stones, hypercalcemia)
    if 14 <= age <= 18:
        calcium_outline['upper_limit'] = 3000  # UL for 14-18 years
    elif 19 <= age <= 50:
        calcium_outline['upper_limit'] = 2500  # UL for 19-50 years
    else:
        calcium_outline['upper_limit'] = 2000  # UL for 51+ years

    return calcium_outline


def generate_chloride_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Chloride intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Chloride recommendations
    chloride_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Chloride Adequate Intake (AI) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Water, Potassium, Sodium, Chloride, and Sulfate
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals, same for both genders
    if 14 <= age <= 18:
        chloride_outline['recommended_intake'] = 2300  # AI for ages 14-18
        # ~78% of AI, estimated minimum
        chloride_outline['lower_limit'] = 1800
    elif 19 <= age <= 50:
        chloride_outline['recommended_intake'] = 2300  # AI for ages 19-50
        chloride_outline['lower_limit'] = 1800        # ~78% of AI
    else:  # Age 51+
        chloride_outline['recommended_intake'] = 2000  # AI for ages 51+
        chloride_outline['lower_limit'] = 1500        # ~75% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity levels increase sweat loss, potentially increasing chloride needs
    # Adjustments are moderate (up to 15% increase) to account for electrolyte loss
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    chloride_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased fluid and electrolyte needs
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.1, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-110%
    chloride_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    chloride_outline['recommended_intake'] = round(
        chloride_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., hypertension)
    chloride_outline['upper_limit'] = 3600  # UL for ages 14+

    return chloride_outline


def generate_chromium_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Chromium intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Chromium recommendations
    chromium_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Chromium Adequate Intake (AI) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            chromium_outline['recommended_intake'] = 35
            # ~80% of AI, estimated minimum
            chromium_outline['lower_limit'] = 28
        else:  # Female
            # AI for females 14-18 years
            chromium_outline['recommended_intake'] = 24
            chromium_outline['lower_limit'] = 19        # ~80% of AI
    elif 19 <= age <= 50:
        if gender == 'M':
            # AI for males 19-50 years
            chromium_outline['recommended_intake'] = 35
            chromium_outline['lower_limit'] = 28        # ~80% of AI
        else:  # Female
            # AI for females 19-50 years
            chromium_outline['recommended_intake'] = 25
            chromium_outline['lower_limit'] = 20        # ~80% of AI
    else:  # Age 51+
        if gender == 'M':
            # AI for males 51+ years
            chromium_outline['recommended_intake'] = 30
            chromium_outline['lower_limit'] = 24        # ~80% of AI
        else:  # Female
            # AI for females 51+ years
            chromium_outline['recommended_intake'] = 20
            chromium_outline['lower_limit'] = 16        # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may enhance glucose metabolism, slightly increasing chromium needs
    # Adjustments are minimal (up to 10% increase) as requirements are not strongly tied to activity
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    chromium_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Chromium needs may correlate with energy intake due to its role in insulin function, but adjustment is conservative
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    chromium_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    chromium_outline['recommended_intake'] = round(
        chromium_outline['recommended_intake'])

    # Set upper limit
    # Rationale: No UL established for chromium due to low toxicity risk; set at 10x recommended intake for safety
    chromium_outline['upper_limit'] = 10 * \
        chromium_outline['recommended_intake']

    return chromium_outline


def generate_copper_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Copper intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Copper recommendations
    copper_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Copper Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        copper_outline['recommended_intake'] = 890  # RDA for ages 14-18
        copper_outline['lower_limit'] = 700        # EAR, ~79% of RDA
    else:  # Age 19+
        copper_outline['recommended_intake'] = 900  # RDA for ages 19+
        copper_outline['lower_limit'] = 700        # EAR, ~78% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase oxidative stress, slightly increasing copper needs for enzyme function
    # Adjustments are conservative (up to 10% increase) to avoid excessive intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    copper_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Copper needs may correlate with energy metabolism, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    copper_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    copper_outline['recommended_intake'] = round(
        copper_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., liver damage)
    if 14 <= age <= 18:
        copper_outline['upper_limit'] = 8000  # UL for 14-18 years
    else:
        copper_outline['upper_limit'] = 10000  # UL for 19+ years

    return copper_outline


def generate_fluoride_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Fluoride intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Fluoride recommendations
    fluoride_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Fluoride Adequate Intake (AI) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Calcium, Phosphorus, Magnesium, Vitamin D, and Fluoride
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            fluoride_outline['recommended_intake'] = 3.0
            # ~80% of AI, estimated minimum
            fluoride_outline['lower_limit'] = 2.4
        else:  # Female
            # AI for females 14-18 years
            fluoride_outline['recommended_intake'] = 3.0
            fluoride_outline['lower_limit'] = 2.4        # ~80% of AI
    else:  # Age 19+
        if gender == 'M':
            # AI for males 19+ years
            fluoride_outline['recommended_intake'] = 4.0
            fluoride_outline['lower_limit'] = 3.2        # ~80% of AI
        else:  # Female
            # AI for females 19+ years
            fluoride_outline['recommended_intake'] = 3.0
            fluoride_outline['lower_limit'] = 2.4        # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase fluid intake, potentially affecting fluoride exposure, but impact is minimal
    # Adjustments are slight (up to 5% increase) as fluoride needs are primarily tied to dental health
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    fluoride_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Fluoride needs are not directly tied to energy intake, but slight adjustment for consistency
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    fluoride_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    fluoride_outline['recommended_intake'] = round(
        fluoride_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., fluorosis)
    fluoride_outline['upper_limit'] = 10.0  # UL for ages 14+

    return fluoride_outline


def generate_iodine_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate an Iodine intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Iodine recommendations
    iodine_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Iodine Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        iodine_outline['recommended_intake'] = 150  # RDA for ages 14-18
        iodine_outline['lower_limit'] = 95         # EAR, ~63% of RDA
    else:  # Age 19+
        iodine_outline['recommended_intake'] = 150  # RDA for ages 19+
        iodine_outline['lower_limit'] = 95         # EAR, ~63% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase thyroid hormone production, slightly increasing iodine needs
    # Adjustments are minimal (up to 5% increase) as iodine requirements are primarily tied to thyroid function
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    iodine_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Iodine needs are not strongly tied to energy intake, but slight adjustment for metabolic rate
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    iodine_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    iodine_outline['recommended_intake'] = round(
        iodine_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., thyroid dysfunction)
    if 14 <= age <= 18:
        iodine_outline['upper_limit'] = 900  # UL for 14-18 years
    else:
        iodine_outline['upper_limit'] = 1100  # UL for 19+ years

    return iodine_outline


def generate_iron_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate an Iron intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Iron recommendations
    iron_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Iron Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            iron_outline['recommended_intake'] = 11
            iron_outline['lower_limit'] = 7.7       # EAR, ~70% of RDA
        else:  # Female
            # RDA for females 14-18 years
            iron_outline['recommended_intake'] = 15
            iron_outline['lower_limit'] = 7.9       # EAR, ~53% of RDA
    elif 19 <= age <= 50:
        if gender == 'M':
            # RDA for males 19-50 years
            iron_outline['recommended_intake'] = 8
            iron_outline['lower_limit'] = 6         # EAR, ~75% of RDA
        else:  # Female
            # RDA for females 19-50 years
            iron_outline['recommended_intake'] = 18
            iron_outline['lower_limit'] = 8.1       # EAR, ~45% of RDA
    else:  # Age 51+
        # RDA for males and females 51+ years
        iron_outline['recommended_intake'] = 8
        iron_outline['lower_limit'] = 6         # EAR, ~75% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase red blood cell turnover, slightly increasing iron needs, especially in females
    # Adjustments are conservative (up to 10% increase) to avoid excessive intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    iron_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased metabolic demands, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    iron_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    iron_outline['recommended_intake'] = round(
        iron_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., gastrointestinal distress)
    iron_outline['upper_limit'] = 45  # UL for ages 14+

    return iron_outline


def generate_magnesium_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Magnesium intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Magnesium recommendations
    magnesium_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Magnesium Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Calcium, Phosphorus, Magnesium, Vitamin D, and Fluoride
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            magnesium_outline['recommended_intake'] = 410
            magnesium_outline['lower_limit'] = 360       # EAR, ~88% of RDA
        else:  # Female
            # RDA for females 14-18 years
            magnesium_outline['recommended_intake'] = 360
            magnesium_outline['lower_limit'] = 300       # EAR, ~83% of RDA
    elif 19 <= age <= 30:
        if gender == 'M':
            # RDA for males 19-30 years
            magnesium_outline['recommended_intake'] = 400
            magnesium_outline['lower_limit'] = 330       # EAR, ~83% of RDA
        else:  # Female
            # RDA for females 19-30 years
            magnesium_outline['recommended_intake'] = 310
            magnesium_outline['lower_limit'] = 255       # EAR, ~82% of RDA
    else:  # Age 31+
        if gender == 'M':
            # RDA for males 31+ years
            magnesium_outline['recommended_intake'] = 420
            magnesium_outline['lower_limit'] = 350       # EAR, ~83% of RDA
        else:  # Female
            # RDA for females 31+ years
            magnesium_outline['recommended_intake'] = 320
            magnesium_outline['lower_limit'] = 265       # EAR, ~83% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase muscle contraction and energy metabolism, slightly increasing magnesium needs
    # Adjustments are conservative (up to 10% increase) to avoid excessive intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    magnesium_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased metabolic demands, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    magnesium_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    magnesium_outline['recommended_intake'] = round(
        magnesium_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL applies only to supplemental magnesium, set to prevent adverse effects (e.g., diarrhea)
    # UL is the same for both genders and all ages 14+
    # UL for ages 14+ (from supplements) = 350, but we will set to 600 and meal plan generation will make maxxium of 350 from supplements
    magnesium_outline['upper_limit'] = 600

    return magnesium_outline


def generate_manganese_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Manganese intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Manganese recommendations
    manganese_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Manganese Adequate Intake (AI) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            manganese_outline['recommended_intake'] = 2.2
            # ~82% of AI, estimated minimum
            manganese_outline['lower_limit'] = 1.8
        else:  # Female
            # AI for females 14-18 years
            manganese_outline['recommended_intake'] = 1.6
            manganese_outline['lower_limit'] = 1.3       # ~81% of AI
    else:  # Age 19+
        if gender == 'M':
            # AI for males 19+ years
            manganese_outline['recommended_intake'] = 2.3
            manganese_outline['lower_limit'] = 1.9       # ~83% of AI
        else:  # Female
            # AI for females 19+ years
            manganese_outline['recommended_intake'] = 1.8
            manganese_outline['lower_limit'] = 1.5       # ~83% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase oxidative stress, slightly increasing manganese needs for enzyme function
    # Adjustments are minimal (up to 5% increase) as requirements are not strongly tied to activity
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    manganese_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Manganese needs may correlate with energy metabolism, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    manganese_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    manganese_outline['recommended_intake'] = round(
        manganese_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., neurological issues)
    if 14 <= age <= 18:
        manganese_outline['upper_limit'] = 9.0  # UL for 14-18 years
    else:
        manganese_outline['upper_limit'] = 11.0  # UL for 19+ years

    return manganese_outline


def generate_molybdenum_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Molybdenum intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Molybdenum recommendations
    molybdenum_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Molybdenum Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        molybdenum_outline['recommended_intake'] = 43  # RDA for ages 14-18
        molybdenum_outline['lower_limit'] = 34        # EAR, ~79% of RDA
    else:  # Age 19+
        molybdenum_outline['recommended_intake'] = 45  # RDA for ages 19+
        molybdenum_outline['lower_limit'] = 34        # EAR, ~76% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Molybdenum is involved in enzyme function, but needs are minimally affected by activity
    # Adjustments are slight (up to 5% increase) as requirements are primarily tied to metabolic baseline
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    molybdenum_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Molybdenum needs are not strongly tied to energy intake, but slight adjustment for metabolic rate
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    molybdenum_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    molybdenum_outline['recommended_intake'] = round(
        molybdenum_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., reproductive issues in animals)
    if 14 <= age <= 18:
        molybdenum_outline['upper_limit'] = 1700  # UL for 14-18 years
    else:
        molybdenum_outline['upper_limit'] = 2000  # UL for 19+ years

    return molybdenum_outline


def generate_phosphorus_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Phosphorus intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Phosphorus recommendations
    phosphorus_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Phosphorus Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Calcium, Phosphorus, Magnesium, Vitamin D, and Fluoride
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        phosphorus_outline['recommended_intake'] = 1250  # RDA for ages 14-18
        phosphorus_outline['lower_limit'] = 1055        # EAR, ~84% of RDA
    else:  # Age 19+
        phosphorus_outline['recommended_intake'] = 700  # RDA for ages 19+
        phosphorus_outline['lower_limit'] = 580        # EAR, ~83% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase bone and muscle turnover, slightly increasing phosphorus needs
    # Adjustments are conservative (up to 10% increase) to avoid excessive intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    phosphorus_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased metabolic demands, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    phosphorus_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    phosphorus_outline['recommended_intake'] = round(
        phosphorus_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., kidney issues)
    if 14 <= age <= 18:
        phosphorus_outline['upper_limit'] = 4000  # UL for 14-18 years
    else:
        # UL for 19-70 years, 3000 for 71+
        phosphorus_outline['upper_limit'] = 4000 if age <= 70 else 3000

    return phosphorus_outline


def generate_potassium_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Potassium intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Potassium recommendations
    potassium_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Potassium Adequate Intake (AI) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Water, Potassium, Sodium, Chloride, and Sulfate
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # AI for males 14-18 years
            potassium_outline['recommended_intake'] = 3000
            # ~80% of AI, estimated minimum
            potassium_outline['lower_limit'] = 2400
        else:  # Female
            # AI for females 14-18 years
            potassium_outline['recommended_intake'] = 2300
            potassium_outline['lower_limit'] = 1840        # ~80% of AI
    else:  # Age 19+
        if gender == 'M':
            # AI for males 19+ years
            potassium_outline['recommended_intake'] = 3400
            potassium_outline['lower_limit'] = 2720        # ~80% of AI
        else:  # Female
            # AI for females 19+ years
            potassium_outline['recommended_intake'] = 2600
            potassium_outline['lower_limit'] = 2080        # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity increases sweat loss and muscle activity, increasing potassium needs
    # Adjustments are moderate (up to 15% increase) to account for electrolyte loss
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.1,
        'very_active': 1.15
    }
    potassium_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure correlates with increased fluid and electrolyte needs
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.1, max(0.9, eer / reference_eer)
                         )  # Cap adjustment between 90-110%
    potassium_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    potassium_outline['recommended_intake'] = round(
        potassium_outline['recommended_intake'])

    # Set upper limit
    # Rationale: No UL established for potassium from food due to low toxicity risk; set at 2x recommended intake for safety
    potassium_outline['upper_limit'] = 2 * \
        potassium_outline['recommended_intake']

    return potassium_outline


def generate_selenium_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Selenium intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in micrograms.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Selenium recommendations
    selenium_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mcg'
    }

    # Selenium Recommended Dietary Allowances (RDA) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin C, Vitamin E, Selenium, and Carotenoids
    # RDA values are set to meet the needs of 97-98% of healthy individuals, same for both genders
    if 14 <= age <= 18:
        selenium_outline['recommended_intake'] = 55  # RDA for ages 14-18
        selenium_outline['lower_limit'] = 45        # EAR, ~82% of RDA
    else:  # Age 19+
        selenium_outline['recommended_intake'] = 55  # RDA for ages 19+
        selenium_outline['lower_limit'] = 45        # EAR, ~82% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase oxidative stress, slightly increasing selenium needs for antioxidant function
    # Adjustments are minimal (up to 5% increase) as requirements are primarily tied to baseline metabolism
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.02,
        'active': 1.04,
        'very_active': 1.05
    }
    selenium_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Selenium needs are not strongly tied to energy intake, but slight adjustment for metabolic rate
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.03, max(0.97, eer / reference_eer)
                         )  # Cap adjustment between 97-103%
    selenium_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    selenium_outline['recommended_intake'] = round(
        selenium_outline['recommended_intake'])

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., selenosis)
    selenium_outline['upper_limit'] = 400  # UL for ages 14+

    return selenium_outline


def generate_sodium_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Sodium intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Sodium recommendations
    sodium_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Sodium Adequate Intake (AI) based on age
    # Source: National Academies of Sciences, Dietary Reference Intakes for Water, Potassium, Sodium, Chloride, and Sulfate
    # AI values are set as no RDA exists; based on observed intakes for healthy individuals, same for both genders
    if 14 <= age <= 50:
        sodium_outline['recommended_intake'] = 1500  # AI for ages 14-50
        # ~80% of AI, estimated minimum
        sodium_outline['lower_limit'] = 1200
    elif 51 <= age <= 70:
        sodium_outline['recommended_intake'] = 1300  # AI for ages 51-70
        sodium_outline['lower_limit'] = 1040        # ~80% of AI
    else:  # Age 71+
        sodium_outline['recommended_intake'] = 1200  # AI for ages 71+
        sodium_outline['lower_limit'] = 960         # ~80% of AI

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity increases sweat loss, significantly increasing sodium needs
    # Adjustments are notable (up to 20% increase) to account for electrolyte loss
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.05,
        'active': 1.15,
        'very_active': 1.2
    }
    sodium_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure correlates with increased fluid and electrolyte needs
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.15, max(0.85, eer / reference_eer)
                         )  # Cap adjustment between 85-115%
    sodium_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to nearest integer for practicality
    sodium_outline['recommended_intake'] = round(
        sodium_outline['recommended_intake'])

    # Set upper limit (Chronic Disease Risk Reduction Intake, CDRR)
    # Rationale: CDRR is used instead of UL to reduce risk of chronic disease (e.g., hypertension)
    sodium_outline['upper_limit'] = 2300  # CDRR for ages 14+

    return sodium_outline


def generate_zinc_outline(age: float, gender: str, activity_level: str, eer: float) -> dict:
    """
    Generate a Zinc intake outline based on age, gender, activity_level, and EER.
    Returns a dictionary with recommended intake, lower limit, upper limit, and units in milligrams.
    Recommendations are based on Dietary Reference Intakes (DRIs) from the National Academies of Sciences,
    prioritizing health as a dietitian would. All arguments are required.

    Parameters:
    -----------
    age : float
        Age in years (14+)
    gender : str
        'M' for male or 'F' for female
    activity_level : str
        One of 'inactive', 'low_active', 'active', or 'very_active'
    eer : float
        Estimated Energy Requirement in kcal/day

    Returns:
    --------
    dict : Dictionary with keys 'recommended_intake', 'lower_limit', 'upper_limit', and 'units'
    """
    # Input validation
    if not (age >= 14):
        raise ValueError("Age must be at least 14 years")
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    if activity_level not in ['inactive', 'low_active', 'active', 'very_active']:
        raise ValueError(
            "Activity level must be one of: 'inactive', 'low_active', 'active', 'very_active'")
    if not (eer > 0):
        raise ValueError("EER must be a positive value")

    # Initialize dictionary to store Zinc recommendations
    zinc_outline = {
        'recommended_intake': 0,
        'lower_limit': 0,
        'upper_limit': 0,
        'units': 'mg'
    }

    # Zinc Recommended Dietary Allowances (RDA) based on age and gender
    # Source: National Academies of Sciences, Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc
    # RDA values are set to meet the needs of 97-98% of healthy individuals
    if 14 <= age <= 18:
        if gender == 'M':
            # RDA for males 14-18 years
            zinc_outline['recommended_intake'] = 11
            zinc_outline['lower_limit'] = 8.5      # EAR, ~77% of RDA
        else:  # Female
            # RDA for females 14-18 years
            zinc_outline['recommended_intake'] = 9
            zinc_outline['lower_limit'] = 7.3      # EAR, ~81% of RDA
    else:  # Age 19+
        if gender == 'M':
            zinc_outline['recommended_intake'] = 11  # RDA for males 19+ years
            zinc_outline['lower_limit'] = 9.4       # EAR, ~85% of RDA
        else:  # Female
            zinc_outline['recommended_intake'] = 8  # RDA for females 19+ years
            zinc_outline['lower_limit'] = 6.8      # EAR, ~85% of RDA

    # Adjust recommended intake based on activity level
    # Rationale: Higher activity may increase zinc losses through sweat and support immune and muscle function
    # Adjustments are conservative (up to 10% increase) to avoid excessive intake
    activity_multipliers = {
        'inactive': 1.0,
        'low_active': 1.03,
        'active': 1.07,
        'very_active': 1.1
    }
    zinc_outline['recommended_intake'] *= activity_multipliers[activity_level]

    # Adjust based on EER relative to reference (2500 kcal for males, 2000 kcal for females)
    # Rationale: Higher energy expenditure may correlate with increased metabolic demands, but adjustment is minimal
    reference_eer = 2500 if gender == 'M' else 2000
    eer_adjustment = min(1.05, max(0.95, eer / reference_eer)
                         )  # Cap adjustment between 95-105%
    zinc_outline['recommended_intake'] *= eer_adjustment

    # Round recommended intake to one decimal place for practicality
    zinc_outline['recommended_intake'] = round(
        zinc_outline['recommended_intake'], 1)

    # Set upper limit (Tolerable Upper Intake Level, UL) based on age
    # Rationale: UL is the same for both genders, set to prevent adverse effects (e.g., impaired copper absorption)
    if 14 <= age <= 18:
        zinc_outline['upper_limit'] = 34  # UL for 14-18 years
    else:
        zinc_outline['upper_limit'] = 40  # UL for 19+ years

    return zinc_outline


def generate_nutritional_guideline(age: float, height: float, weight: float, gender: str, activity_level: str) -> dict:
    """
    Generate nutritional guideline based on age, height, weight, gender, and activity level.

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
    dict : Nutritional guidelines
    """
    eer = calc_EER(age, height, weight, gender, activity_level)

    # -------- Macronutrients ---------
    # Carbohydrates (in grams)
    carbohydrate_outline = generate_carbohydrates_outline(
        age, gender, activity_level, eer)
    # Fiber (in grams)
    fiber_outline = generate_fiber_outline(
        age, gender, activity_level, eer)
    # Protein (in grams)
    protein_outline = generate_protein_outline(
        age, gender, activity_level, eer)
    # Fat (in grams)
    fat_outline = generate_fat_outline(
        age, gender, activity_level, eer)

    # --------- Vitamins -----------
    # Vitamin A (in micrograms)
    vitamin_a_outline = generate_vitamin_a_outline(
        age, gender, activity_level, eer)
    # Vitamin C (in milligrams)
    vitamin_c_outline = generate_vitamin_c_outline(
        age, gender, activity_level, eer)
    # Vitamin D (in micrograms)
    vitamin_d_outline = generate_vitamin_d_outline(
        age, gender, activity_level, eer)
    # Vitamin B6 (in milligrams)
    vitamin_b6_outline = generate_vitamin_b6_outline(
        age, gender, activity_level, eer)
    # Vitamin E (in milligrams)
    vitamin_e_outline = generate_vitamin_e_outline(
        age, gender, activity_level, eer)
    # Vitamin K (in micrograms)
    vitamin_k_outline = generate_vitamin_k_outline(
        age, gender, activity_level, eer)
    # Thiamin (in milligrams)
    thiamin_outline = generate_thiamin_outline(
        age, gender, activity_level, eer)
    # Vitamin B12 (in micrograms)
    vitamin_b12_outline = generate_vitamin_b12_outline(
        age, gender, activity_level, eer)
    # Riboflavin (in milligrams)
    riboflavin_outline = generate_riboflavin_outline(
        age, gender, activity_level, eer)
    # Folate (in micrograms)
    folate_outline = generate_folate_outline(
        age, gender, activity_level, eer)
    # Niacin (in milligrams)
    niacin_outline = generate_niacin_outline(
        age, gender, activity_level, eer)
    # Choline (in milligrams)
    choline_outline = generate_choline_outline(
        age, gender, activity_level, eer)
    # Pantothenic Acid (in milligrams)
    pantothenic_acid_outline = generate_pantothenic_acid_outline(
        age, gender, activity_level, eer)
    # Biotin (in micrograms)
    biotin_outline = generate_biotin_outline(
        age, gender, activity_level, eer)

    # --------- Minerals ------------
    # Calcium (in milligrams)
    calcium_outline = generate_calcium_outline(
        age, gender, activity_level, eer)
    # Chloride (in milligrams)
    chloride_outline = generate_chloride_outline(
        age, gender, activity_level, eer)
    # Chromium (in micrograms)
    chromium_outline = generate_chromium_outline(
        age, gender, activity_level, eer)
    # Copper (in micrograms)
    copper_outline = generate_copper_outline(
        age, gender, activity_level, eer)
    # Fluoride (in milligrams)
    fluoride_outline = generate_fluoride_outline(
        age, gender, activity_level, eer)
    # Iodine (in micrograms)
    iodine_outline = generate_iodine_outline(
        age, gender, activity_level, eer)
    # Iron (in milligrams)
    iron_outline = generate_iron_outline(
        age, gender, activity_level, eer)
    # Magnesium (in milligrams)
    magnesium_outline = generate_magnesium_outline(
        age, gender, activity_level, eer)
    # Manganese (in milligrams)
    manganese_outline = generate_manganese_outline(
        age, gender, activity_level, eer)
    # Molybdenum (in micrograms)
    molybdenum_outline = generate_molybdenum_outline(
        age, gender, activity_level, eer)
    # Phosphorus (in milligrams)
    phosphorus_outline = generate_phosphorus_outline(
        age, gender, activity_level, eer)
    # Potassium (in milligrams)
    potassium_outline = generate_potassium_outline(
        age, gender, activity_level, eer)
    # Selenium (in micrograms)
    selenium_outline = generate_selenium_outline(
        age, gender, activity_level, eer)
    # Sodium (in milligrams)
    sodium_outline = generate_sodium_outline(
        age, gender, activity_level, eer)
    # Zinc (in milligrams)
    zinc_outline = generate_zinc_outline(
        age, gender, activity_level, eer)

    # Output
    nutritional_guideline = {
        "macronutrients": {
            "carbohydrates": carbohydrate_outline,
            "fiber": fiber_outline,
            "protein": protein_outline,
            "fat": fat_outline
        },
        "vitamins": {
            "vitamin_a": vitamin_a_outline,
            "vitamin_c": vitamin_c_outline,
            "vitamin_d": vitamin_d_outline,
            "vitamin_b6": vitamin_b6_outline,
            "vitamin_e": vitamin_e_outline,
            "vitamin_k": vitamin_k_outline,
            "thiamin": thiamin_outline,
            "vitamin_b12": vitamin_b12_outline,
            "riboflavin": riboflavin_outline,
            "folate": folate_outline,
            "niacin": niacin_outline,
            "choline": choline_outline,
            "pantothenic_acid": pantothenic_acid_outline,
            "biotin": biotin_outline
        },
        "minerals": {
            "calcium": calcium_outline,
            "chloride": chloride_outline,
            "chromium": chromium_outline,
            "copper": copper_outline,
            "fluoride": fluoride_outline,
            "iodine": iodine_outline,
            "iron": iron_outline,
            "magnesium": magnesium_outline,
            "manganese": manganese_outline,
            "molybdenum": molybdenum_outline,
            "phosphorus": phosphorus_outline,
            "potassium": potassium_outline,
            "selenium": selenium_outline,
            "sodium": sodium_outline,
            "zinc": zinc_outline
        }
    }
    return nutritional_guideline
