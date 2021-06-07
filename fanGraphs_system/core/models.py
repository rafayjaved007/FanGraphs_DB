from django.db import models


class Team(models.Model):
    class LEAGUE(models.TextChoices):
        NATIONAL = 'National'
        AMERICAN = 'American'

    class DIVISION(models.TextChoices):
        EAST = 'East'
        CENTRAL = 'Central'
        WEST = 'West'

    name = models.CharField(max_length=50)
    league = models.CharField(max_length=10, choices=LEAGUE.choices, blank=True)
    division = models.CharField(max_length=10, choices=DIVISION.choices, blank=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    class W_OR_L(models.TextChoices):
        W = 'W'
        L = 'L'

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    team_win_prob = models.CharField(max_length=50, blank=True, null=True)
    w_or_l = models.CharField(max_length=10, choices=W_OR_L.choices, blank=True, null=True)
    team_runs = models.IntegerField(blank=True, null=True)
    opp_runs = models.IntegerField(blank=True, null=True)
    team_starter = models.CharField(max_length=100, blank=True, null=True)
    opp_starter = models.CharField(max_length=100, blank=True, null=True)


class Pitcher(models.Model):
    class Role(models.TextChoices):
        Bull_Pen = 'bullpen'
        Starting_Rotation = 'starting_rotation'

    role = models.CharField(max_length=150, choices=Role.choices, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    pos = models.CharField(max_length=50, blank=True, null=True)
    player = models.CharField(max_length=150, blank=True, null=True)
    thr = models.CharField(max_length=50, blank=True, null=True)
    ovr = models.CharField(max_length=50, blank=True, null=True)
    last_14_days = models.CharField(max_length=50, blank=True, null=True)
    day1 = models.CharField(max_length=50, blank=True, null=True)
    day2 = models.CharField(max_length=50, blank=True, null=True)
    day3 = models.CharField(max_length=50, blank=True, null=True)
    day4 = models.CharField(max_length=50, blank=True, null=True)
    day5 = models.CharField(max_length=50, blank=True, null=True)
    day6 = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.player


class PitchersStandard(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    gs = models.CharField(max_length=50, blank=True, null=True)
    w = models.CharField(max_length=50, blank=True, null=True)
    l = models.CharField(max_length=50, blank=True, null=True)
    era = models.CharField(max_length=50, blank=True, null=True)
    g = models.CharField(max_length=50, blank=True, null=True)
    cg = models.CharField(max_length=50, blank=True, null=True)
    sho = models.CharField(max_length=50, blank=True, null=True)
    sv = models.CharField(max_length=50, blank=True, null=True)
    hld = models.CharField(max_length=50, blank=True, null=True)
    bs = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    tbf = models.CharField(max_length=50, blank=True, null=True)
    h = models.CharField(max_length=50, blank=True, null=True)
    r = models.CharField(max_length=50, blank=True, null=True)
    er = models.CharField(max_length=50, blank=True, null=True)
    hr = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    ibb = models.CharField(max_length=50, blank=True, null=True)
    hbp = models.CharField(max_length=50, blank=True, null=True)
    wp = models.CharField(max_length=50, blank=True, null=True)
    bk = models.CharField(max_length=50, blank=True, null=True)
    so = models.CharField(max_length=50, blank=True, null=True)
    gsv2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class PitchersAdvanced(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    gs = models.CharField(max_length=50, blank=True, null=True)
    k_9 = models.CharField(max_length=50, blank=True, null=True)
    bb_9 = models.CharField(max_length=50, blank=True, null=True)
    k_bb = models.CharField(max_length=50, blank=True, null=True)
    hr_9 = models.CharField(max_length=50, blank=True, null=True)
    k_percentage = models.CharField(max_length=50, blank=True, null=True)
    bb_percentage = models.CharField(max_length=50, blank=True, null=True)
    k_bb_percentage = models.CharField(max_length=50, blank=True, null=True)
    avg = models.CharField(max_length=50, blank=True, null=True)
    whip = models.CharField(max_length=50, blank=True, null=True)
    babip = models.CharField(max_length=50, blank=True, null=True)
    lob_percentage = models.CharField(max_length=50, blank=True, null=True)
    era_dash = models.CharField(max_length=50, blank=True, null=True)
    fip_dash = models.CharField(max_length=50, blank=True, null=True)
    fip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class PitchersWinProbability(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    gs = models.CharField(max_length=50, blank=True, null=True)
    wpa = models.CharField(max_length=50, blank=True, null=True)
    minus_wpa = models.CharField(max_length=50, blank=True, null=True)
    plus_wpa = models.CharField(max_length=50, blank=True, null=True)
    re24 = models.CharField(max_length=50, blank=True, null=True)
    rew = models.CharField(max_length=50, blank=True, null=True)
    pli = models.CharField(max_length=50, blank=True, null=True)
    inli = models.CharField(max_length=50, blank=True, null=True)
    gmli = models.CharField(max_length=50, blank=True, null=True)
    exli = models.CharField(max_length=50, blank=True, null=True)
    pulls = models.CharField(max_length=50, blank=True, null=True)
    wpa_li = models.CharField(max_length=50, blank=True, null=True)
    clutch = models.CharField(max_length=50, blank=True, null=True)
    sd = models.CharField(max_length=50, blank=True, null=True)
    md = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class PitchersPlateDiscipline(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    gs = models.CharField(max_length=50, blank=True, null=True)
    o_swing_percent = models.CharField(max_length=50, blank=True, null=True)
    z_swing_percentage = models.CharField(max_length=50, blank=True, null=True)
    swing_percentage = models.CharField(max_length=50, blank=True, null=True)
    o_contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    z_contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    zone_percentage = models.CharField(max_length=50, blank=True, null=True)
    f_strike_percentage = models.CharField(max_length=50, blank=True, null=True)
    swstr_percentage = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class Hitter(models.Model):
    class Role(models.TextChoices):
        Bench = 'bench'
        Starting_Lineup = 'starting_lineup'

    role = models.CharField(max_length=150, choices=Role.choices, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    pos = models.CharField(max_length=50, blank=True, null=True)
    player = models.CharField(max_length=150, blank=True, null=True)
    bats = models.CharField(max_length=50, blank=True, null=True)
    ovr = models.CharField(max_length=50, blank=True, null=True)
    last_7_days = models.CharField(max_length=50, blank=True, null=True)
    lineup1 = models.CharField(max_length=50, blank=True, null=True)
    lineup2 = models.CharField(max_length=50, blank=True, null=True)
    lineup3 = models.CharField(max_length=50, blank=True, null=True)
    lineup4 = models.CharField(max_length=50, blank=True, null=True)
    lineup5 = models.CharField(max_length=50, blank=True, null=True)
    lineup6 = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.player


class HittersStandard(models.Model):
    player = models.ForeignKey(Hitter, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    g = models.CharField(max_length=50, blank=True, null=True)
    ab = models.CharField(max_length=50, blank=True, null=True)
    pa = models.CharField(max_length=50, blank=True, null=True)
    h = models.CharField(max_length=50, blank=True, null=True)
    one_b = models.CharField(max_length=50, blank=True, null=True)
    two_b = models.CharField(max_length=50, blank=True, null=True)
    three_b = models.CharField(max_length=50, blank=True, null=True)
    hr = models.CharField(max_length=50, blank=True, null=True)
    r = models.CharField(max_length=50, blank=True, null=True)
    rbi = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    ibb = models.CharField(max_length=50, blank=True, null=True)
    so = models.CharField(max_length=50, blank=True, null=True)
    hbp = models.CharField(max_length=50, blank=True, null=True)
    sf = models.CharField(max_length=50, blank=True, null=True)
    sh = models.CharField(max_length=50, blank=True, null=True)
    gdp = models.CharField(max_length=50, blank=True, null=True)
    sb = models.CharField(max_length=50, blank=True, null=True)
    cs = models.CharField(max_length=50, blank=True, null=True)
    avg = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class HittersAdvanced(models.Model):
    player = models.ForeignKey(Hitter, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    bb_percentage = models.CharField(max_length=50, blank=True, null=True)
    k_percentage = models.CharField(max_length=50, blank=True, null=True)
    bb_k = models.CharField(max_length=50, blank=True, null=True)
    avg = models.CharField(max_length=50, blank=True, null=True)
    obp = models.CharField(max_length=50, blank=True, null=True)
    slg = models.CharField(max_length=50, blank=True, null=True)
    ops = models.CharField(max_length=50, blank=True, null=True)
    iso = models.CharField(max_length=50, blank=True, null=True)
    spd = models.CharField(max_length=50, blank=True, null=True)
    babip = models.CharField(max_length=50, blank=True, null=True)
    wrc = models.CharField(max_length=50, blank=True, null=True)
    wraa = models.CharField(max_length=50, blank=True, null=True)
    woba = models.CharField(max_length=50, blank=True, null=True)
    wrc_plus = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class HittersPlateDiscipline(models.Model):
    player = models.ForeignKey(Hitter, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    o_swing_percent = models.CharField(max_length=50, blank=True, null=True)
    z_swing_percentage = models.CharField(max_length=50, blank=True, null=True)
    swing_percentage = models.CharField(max_length=50, blank=True, null=True)
    o_contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    z_contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    zone_percentage = models.CharField(max_length=50, blank=True, null=True)
    f_strike_percentage = models.CharField(max_length=50, blank=True, null=True)
    swstr_percentage = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class DualHittersStandard(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    g = models.CharField(max_length=50, blank=True, null=True)
    ab = models.CharField(max_length=50, blank=True, null=True)
    pa = models.CharField(max_length=50, blank=True, null=True)
    h = models.CharField(max_length=50, blank=True, null=True)
    one_b = models.CharField(max_length=50, blank=True, null=True)
    two_b = models.CharField(max_length=50, blank=True, null=True)
    three_b = models.CharField(max_length=50, blank=True, null=True)
    hr = models.CharField(max_length=50, blank=True, null=True)
    r = models.CharField(max_length=50, blank=True, null=True)
    rbi = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    ibb = models.CharField(max_length=50, blank=True, null=True)
    so = models.CharField(max_length=50, blank=True, null=True)
    hbp = models.CharField(max_length=50, blank=True, null=True)
    sf = models.CharField(max_length=50, blank=True, null=True)
    sh = models.CharField(max_length=50, blank=True, null=True)
    gdp = models.CharField(max_length=50, blank=True, null=True)
    sb = models.CharField(max_length=50, blank=True, null=True)
    cs = models.CharField(max_length=50, blank=True, null=True)
    avg = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class DualHittersAdvanced(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    bb_percentage = models.CharField(max_length=50, blank=True, null=True)
    k_percentage = models.CharField(max_length=50, blank=True, null=True)
    bb_k = models.CharField(max_length=50, blank=True, null=True)
    avg = models.CharField(max_length=50, blank=True, null=True)
    obp = models.CharField(max_length=50, blank=True, null=True)
    slg = models.CharField(max_length=50, blank=True, null=True)
    ops = models.CharField(max_length=50, blank=True, null=True)
    iso = models.CharField(max_length=50, blank=True, null=True)
    spd = models.CharField(max_length=50, blank=True, null=True)
    babip = models.CharField(max_length=50, blank=True, null=True)
    wrc = models.CharField(max_length=50, blank=True, null=True)
    wraa = models.CharField(max_length=50, blank=True, null=True)
    woba = models.CharField(max_length=50, blank=True, null=True)
    wrc_plus = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class DualHittersPlateDiscipline(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    o_swing_percent = models.CharField(max_length=50, blank=True, null=True)
    z_swing_percentage = models.CharField(max_length=50, blank=True, null=True)
    swing_percentage = models.CharField(max_length=50, blank=True, null=True)
    o_contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    z_contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    contact_percentage = models.CharField(max_length=50, blank=True, null=True)
    zone_percentage = models.CharField(max_length=50, blank=True, null=True)
    f_strike_percentage = models.CharField(max_length=50, blank=True, null=True)
    swstr_percentage = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date


class DualHittersWinProbability(models.Model):
    player = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    pos = models.CharField(max_length=50, blank=True, null=True)
    wpa = models.CharField(max_length=50, blank=True, null=True)
    minus_wpa = models.CharField(max_length=50, blank=True, null=True)
    plus_wpa = models.CharField(max_length=50, blank=True, null=True)
    re24 = models.CharField(max_length=50, blank=True, null=True)
    rew = models.CharField(max_length=50, blank=True, null=True)
    pli = models.CharField(max_length=50, blank=True, null=True)
    phli = models.CharField(max_length=50, blank=True, null=True)
    wpa_li = models.CharField(max_length=50, blank=True, null=True)
    clutch = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.date
