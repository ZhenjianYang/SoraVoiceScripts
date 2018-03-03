from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1600   ._SN',
        MapName             = 'Bose',
        Location            = 'C1600.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60125",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Cryon Bit',                            # 9
        'Master Cryon',                         # 10
        'Rocco',                                # 11
        'Target Camera',                        # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH12450 ._CH',             # 00
        'ED6_DT29/CH12451 ._CH',             # 01
        'ED6_DT09/CH10840 ._CH',             # 02
        'ED6_DT09/CH10841 ._CH',             # 03
        'ED6_DT29/CH12460 ._CH',             # 04
        'ED6_DT29/CH12461 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
        'ED6_DT29/CH12501 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT29/CH12561 ._CH',             # 0B
        'ED6_DT07/CH02530 ._CH',             # 0C
        'ED6_DT07/CH00450 ._CH',             # 0D
        'ED6_DT07/CH00460 ._CH',             # 0E
        'ED6_DT07/CH00470 ._CH',             # 0F
        'ED6_DT07/CH00454 ._CH',             # 10
        'ED6_DT07/CH00464 ._CH',             # 11
        'ED6_DT07/CH00474 ._CH',             # 12
        'ED6_DT07/CH00451 ._CH',             # 13
        'ED6_DT07/CH00461 ._CH',             # 14
        'ED6_DT07/CH00471 ._CH',             # 15
        'ED6_DT07/CH00462 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT29/CH12450P._CP',             # 00
        'ED6_DT29/CH12451P._CP',             # 01
        'ED6_DT09/CH10840P._CP',             # 02
        'ED6_DT09/CH10841P._CP',             # 03
        'ED6_DT29/CH12460P._CP',             # 04
        'ED6_DT29/CH12461P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
        'ED6_DT29/CH12501P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT29/CH12561P._CP',             # 0B
        'ED6_DT07/CH02530P._CP',             # 0C
        'ED6_DT07/CH00450P._CP',             # 0D
        'ED6_DT07/CH00460P._CP',             # 0E
        'ED6_DT07/CH00470P._CP',             # 0F
        'ED6_DT07/CH00454P._CP',             # 10
        'ED6_DT07/CH00464P._CP',             # 11
        'ED6_DT07/CH00474P._CP',             # 12
        'ED6_DT07/CH00451P._CP',             # 13
        'ED6_DT07/CH00461P._CP',             # 14
        'ED6_DT07/CH00471P._CP',             # 15
        'ED6_DT07/CH00462P._CP',             # 16
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5230,
        Z                   = 4000,
        Y                   = -12590,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28010,
        Z                   = 6000,
        Y                   = -9400,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21830,
        Z                   = 6560,
        Y                   = -1430,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35520,
        Z                   = 16000,
        Y                   = 14970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8390,
        Z                   = 16000,
        Y                   = -3360,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25620,
        Z                   = 22000,
        Y                   = 15270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -11880,
        Y                   = 4000,
        Z                   = -6460,
        Range               = -10050,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0xFFFFC7A2,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = 18300,
        Y                   = 17460,
        Z                   = 8020,
        Range               = 21370,
        Unknown_10          = 0x57BC,
        Unknown_14          = 0x6AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_2CA",          # 00, 0
        "Function_1_313",          # 01, 1
        "Function_2_362",          # 02, 2
        "Function_3_378",          # 03, 3
        "Function_4_624",          # 04, 4
        "Function_5_B78",          # 05, 5
        "Function_6_12E2",         # 06, 6
    )


    def Function_0_2CA(): pass

    label("Function_0_2CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3")
    SetChrFlags(0x19, 0x80)

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306")
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5030, 4000, -13130, 270)

    label("loc_306")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")

    label("loc_312")

    Return()

    # Function_0_2CA end

    def Function_1_313(): pass

    label("Function_1_313")

    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 7)), scpexpr(EXPR_END)), "loc_355")
    OP_B2(0x0, 0x1, 0x80)

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 4)), scpexpr(EXPR_END)), "loc_361")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_361")

    Return()

    # Function_1_313 end

    def Function_2_362(): pass

    label("Function_2_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_362")

    label("loc_377")

    Return()

    # Function_2_362 end

    def Function_3_378(): pass

    label("Function_3_378")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1500)
    OP_6D(-11540, 4000, -8180, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_3AE():
        OP_6D(-9000, 4000, -10140, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3AE)

    def lambda_3C6():
        OP_6C(330000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3C6)

    def lambda_3D6():
        OP_67(0, 5860, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3D6)

    def lambda_3EE():
        OP_6B(3420, 2500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_3EE)
    OP_11(0xFF, 0xFF, 0xFF, 0x878C, 0xFF78, 0x0)
    SetChrPos(0x111, -11540, 4000, -11370, 124)
    SetChrPos(0x113, -10550, 4000, -9690, 124)
    SetChrPos(0x112, -10570, 4000, -11060, 124)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #0
        0x113,
        "#1765F#5PHmph. Here's our next one, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x112,
        "#1756F#5PThere's no way we'll struggle against this guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x111,
        (
            "#1744F#5PDon't be so sure. After the other fights here, \x01",
            "there's no way I'm letting my guard down this\x01",
            "time.\x02\x03",

            "#1742FStay cautious, guys.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x113, 0x1000)
    SetChrFlags(0x111, 0x1000)
    SetChrFlags(0x112, 0x1000)

    def lambda_553():
        OP_6D(-7000, 3500, -10140, 1000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_553)

    def lambda_56B():
        OP_6B(2920, 1000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_56B)
    SetChrChipByIndex(0x112, 20)
    SetChrSubChip(0x112, 0)

    def lambda_585():
        OP_8E(0xFE, 0xFFFFE840, 0xFA0, 0xFFFFCE28, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_585)
    Sleep(50)
    SetChrChipByIndex(0x111, 19)
    SetChrSubChip(0x111, 0)

    def lambda_5AF():
        OP_8E(0xFE, 0xFFFFE840, 0xFA0, 0xFFFFCCFC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_5AF)
    Sleep(50)
    SetChrChipByIndex(0x113, 21)
    SetChrSubChip(0x113, 0)

    def lambda_5D9():
        OP_8E(0xFE, 0xFFFFE840, 0xFA0, 0xFFFFD0E4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_5D9)
    Sleep(450)
    OP_44(0x113, 0xFF)
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x13, 0xFF)
    ClearChrFlags(0x113, 0x1000)
    ClearChrFlags(0x111, 0x1000)
    ClearChrFlags(0x112, 0x1000)
    Battle(0x3A0, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 4)
    Return()

    # Function_3_378 end

    def Function_4_624(): pass

    label("Function_4_624")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-6440, 4000, -11720, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x8F5C, 0xFF78, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x111, -5050, 4000, -11660, 225)
    SetChrPos(0x113, -4540, 4000, -13610, 315)
    SetChrPos(0x112, -6490, 4000, -13030, 45)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0x112,
        "#1755F#5PWhew... That's that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x111,
        (
            "#1749F#11PYeah... That one ended up being tough,\x01",
            "too, but nothin' we couldn't handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x113,
        "#1764F#6P#1SBah... If only there was three of me.\x02",
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_7D0():

        label("loc_7D0")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_7D0")

    QueueWorkItem2(0x112, 2, lambda_7D0)
    Sleep(100)

    def lambda_7E6():

        label("loc_7E6")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_7E6")

    QueueWorkItem2(0x111, 2, lambda_7E6)
    Sleep(300)

    ChrTalk(    #6
        0x112,
        "#1753F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x111,
        "#1743F#11PYou say somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x113,
        (
            "#1762FCouldn't you hear me?\x02\x03",

            "#1763FI meant what I said.\x02\x03",

            "#1761FIf only there was three of me instead of just me\x01",
            "and you two jokes, I'd've been done by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x112,
        "#1753F#5P*sigh* If you say so, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x111,
        (
            "#1745F#11P...\x02\x03",

            "#1749FWell, unfortunately for you, this is the group\x01",
            "we've got, and we're gonna have to stick with\x01",
            "it.\x02\x03",

            "#1742FKeep your shit-talkin' to yourself, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        (
            "#1764F#6PHmph...\x02\x03",

            "#1763FJust don't drag me down.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x113, 90, 500)
    Sleep(100)

    def lambda_9F0():
        OP_8E(0xFE, 0x123E, 0xFA0, 0xFFFFCD38, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_9F0)
    Sleep(1500)

    def lambda_A10():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_A10)

    ChrTalk(    #12
        0x112,
        "#1752F#5PWhat's gotten into him? Seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x111,
        "#1742F#5P...\x02",
    )

    CloseMessageWindow()
    OP_44(0x111, 0x2)
    OP_44(0x112, 0x2)

    def lambda_A6D():
        OP_8E(0xFE, 0x123E, 0xFA0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_A6D)
    Sleep(100)

    def lambda_A8D():
        OP_8E(0xFE, 0x123E, 0xFA0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_A8D)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x113, 0xFF)
    OP_6D(2240, 4000, -12100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0xAAB4, 0xFF78, 0x0)
    OP_9F(0x113, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x111, 2240, 4000, -12100, 90)
    SetChrPos(0x112, 2240, 4000, -12100, 90)
    SetChrPos(0x113, 2240, 4000, -12100, 90)
    SetChrSubChip(0x111, 0)
    SetChrSubChip(0x112, 0)
    SetChrSubChip(0x113, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C4(0x1, 0x20000000)
    OP_A2(0x2F94)
    OP_B2(0x0, 0x0, 0x80)
    EventEnd(0x4)
    Return()

    # Function_4_624 end

    def Function_5_B78(): pass

    label("Function_5_B78")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 23480, 22200, 18920, 150)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 27400, 22000, 15240, 315)
    SetChrChipByIndex(0x12, 18)
    SetChrSubChip(0x12, 3)
    LoadEffect(0x0, "Condition\\\\freeze.eff")
    LoadEffect(0x1, "battle\\\\mgaria0.eff")
    LoadEffect(0x2, "battle\\\\mgaria1.eff")
    LoadEffect(0x3, "magic\\\\mg030_0.eff")
    LoadEffect(0x4, "monster\\ms00300.eff")
    PlayEffect(0x0, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(1000)
    OP_6D(19100, 19040, 5460, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x7FBC, 0xFF78, 0x0)
    SetChrPos(0x111, 19330, 18450, 4490, 45)
    SetChrPos(0x112, 18590, 18490, 5380, 45)
    Sleep(1000)
    OP_20(0x7D0)
    OP_8C(0x112, 45, 0)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x112,
        "#1752F#6PYo, Deen! That looks like him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x111,
        "#1743F#6PYou see him?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x111, 45, 0)
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_21()
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(    #16
        0x111,
        "#1747F#6PWhat's that idiot doing?!\x02",
    )

    CloseMessageWindow()

    def lambda_DA1():
        OP_6D(25960, 22000, 19140, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_DA1)

    def lambda_DB9():
        OP_6C(8000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DB9)

    def lambda_DC9():
        OP_67(0, 5260, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DC9)

    def lambda_DE1():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_DE1)
    WaitChrThread(0x13, 0x0)
    Sleep(1000)

    ChrTalk(    #17
        0x12,
        (
            "#1767F#12P#40WUgh... Damn it!\x02\x03",

            "I can't move... Ngh...\x02\x03",

            "#1764FLooks like this...is the end of the line\x01",
            "for me...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x112, 19330, 18450, 4490, 45)
    SetChrPos(0x111, 18590, 18490, 5380, 45)

    def lambda_E92():
        OP_6D(26100, 22000, 15260, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_E92)

    def lambda_EAA():
        OP_67(0, 4380, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_EAA)

    def lambda_EC2():
        OP_8E(0xFE, 0x5F50, 0x5442, 0x2E54, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_EC2)
    Sleep(100)

    def lambda_EE2():
        OP_8F(0xFE, 0x6478, 0x5460, 0x2940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_EE2)
    WaitChrThread(0x111, 0x1)

    def lambda_F02():

        label("loc_F02")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_F02")

    QueueWorkItem2(0x112, 2, lambda_F02)
    Sleep(300)

    ChrTalk(    #18
        0x111,
        (
            "#1747F#6PRocco!\x02\x03",

            "#1743FThis ain't good! He's frozen!\x02\x03",

            "#1742FCan you handle it, Rais?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x112, 0x1)
    OP_44(0x112, 0x2)

    ChrTalk(    #19
        0x112,
        "#1756F#6PSure thing!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x112, 22)
    SetChrSubChip(0x112, 0)

    def lambda_FA5():
        OP_99(0xFE, 0x0, 0x6, 0x5DC)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_FA5)
    Sleep(400)
    PlayEffect(0x4, 0x2, 0x112, 500, 300, 700, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 700, 0, 0)
    Sleep(1500)

    ChrTalk(    #20
        0x12,
        "#1767F#3S#11PAggghhhhhh!#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_82(0x2, 0x2)
    OP_82(0x1, 0x2)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x12,
        "#1762F#11P...I-I can move.\x02",
    )

    CloseMessageWindow()

    def lambda_1068():
        OP_6D(25520, 22000, 19500, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1068)

    def lambda_1080():
        OP_6B(3640, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1080)

    def lambda_1090():
        OP_8E(0xFE, 0x66F8, 0x55F0, 0x3F34, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1090)
    Sleep(100)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)

    def lambda_10BA():
        OP_8E(0xFE, 0x6324, 0x55F0, 0x38F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_10BA)
    WaitChrThread(0x111, 0x1)
    OP_8C(0x111, 315, 500)
    SetChrChipByIndex(0x111, 13)
    SetChrSubChip(0x111, 0)
    WaitChrThread(0x112, 0x1)
    OP_8C(0x112, 315, 500)
    SetChrChipByIndex(0x112, 14)
    SetChrSubChip(0x112, 0)
    Sleep(300)

    ChrTalk(    #22
        0x111,
        "#1741F#5PHeh. You're a real sorry sight, man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x112,
        "#1756F#6PSorry for keepin' you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        (
            "#1762F#12PTh-The hell are you guys doing here?!\x02\x03",

            "#1767FI thought you bailed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x112,
        "#1751F#6PMore like we came to bail you out! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x111,
        (
            "#1747F#5PBut we can talk later! We've got a fight\x01",
            "on our hands!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1231():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1231)
    Sleep(200)
    Fade(500)
    OP_99(0x12, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #27
        0x12,
        "#1766FRrgh... Fine!\x02",
    )

    CloseMessageWindow()
    OP_59()
    AddParty(0x12, 0xF0, 0xFF)
    SetChrPos(0x113, 27400, 22000, 15240, 315)
    SetChrChipByIndex(0x113, 15)
    SetChrSubChip(0x113, 0)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x112, 25380, 22000, 14580, 315)
    SetChrChipByIndex(0x112, 14)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x111, 13)
    SetChrSubChip(0x111, 0)
    Battle(0x3A3, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 6)
    Return()

    # Function_5_B78 end

    def Function_6_12E2(): pass

    label("Function_6_12E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_6D(25120, 22000, 18540, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x83A4, 0xFF78, 0x0)
    SetChrPos(0x111, 25020, 22000, 16970, 315)
    SetChrPos(0x113, 25940, 22000, 15420, 315)
    SetChrPos(0x112, 24210, 22000, 15900, 315)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #28
        0x111,
        "#1749F#5PWhew... Good thing we made it in time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x112,
        (
            "#1750F#5PSeriously... You really bit off more than you\x01",
            "could chew this time, Rocky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x113,
        (
            "#1767F#12PWhat're you two doing here?! Why'd you come\x01",
            "after me?!\x02\x03",

            "Even without guys, I could've handled that jus--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14B7():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x111, 2, lambda_14B7)
    Sleep(100)
    OP_8C(0x112, 135, 500)
    Sleep(300)

    ChrTalk(    #31
        0x111,
        "#1747F#4S#5PNo, you couldn't, you dumbass!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #32
        0x113,
        "#1762F#12PWhat was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x111,
        (
            "#1747F#5PFor once in your life, stop being so stubborn!\x02\x03",

            "If we hadn't come when we did, you would've\x01",
            "been dead!\x02\x03",

            "And you know it, too! You just don't wanna say it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x113,
        "#1767F#12PWh-What was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x111,
        (
            "#1745F#5P...Nah. I guess I haven't got the right to be\x01",
            "gettin' all angry.\x02\x03",

            "#1749FSorry, man.\x02\x03",

            "I shouldn't've told you to go on alone like I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x113,
        "#1762F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x111,
        (
            "#1744F#5PI might've said earlier that I was only trying to\x01",
            "become a bracer because you pushed us into it...\x02\x03",

            "#1742F...but I swear, that's not the only reason.\x02\x03",

            "There's no way I could've made it through all\x01",
            "that insane training we got put through and\x01",
            "not quit partway if that was the only reason.\x02\x03",

            "I would've thrown in the towel a long time ago\x01",
            "if I wasn't serious about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x112,
        (
            "#1754F#5PWhat he said.\x02\x03",

            "#1750FI'm just as serious about this as you are,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x111,
        (
            "#1749F#5PI know you're in a rush to try and be as tough\x01",
            "as Agate and everythin', and I can't blame you...\x02\x03",

            "#1740F...but whether it's how you'd want things or not, \x01",
            "the three of us are in this together.\x02\x03",

            "It wouldn't hurt to rely on us at least a little,\x01",
            "would it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x113, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x113)
    Sleep(500)

    ChrTalk(    #40
        0x113,
        (
            "#1763F#12PHeh...\x02\x03",

            "#1764F...All right. You got me.\x02\x03",

            "And I ain't no dumbass, Deen. I know my limits.\x02\x03",

            "#1760FYou're probably right. I was just in so much of\x01",
            "a rush to try and narrow the gap between us\x01",
            "that I lost sight of myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x111,
        "#1743F#5PRocco...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x113,
        (
            "#1764F#12PBut that last fight was enough to open my eyes.\x01",
            "I'm not up for the task of getting through this\x01",
            "place alone.\x02\x03",

            "#1763FI know now that I need you guys with me every\x01",
            "step of the way.\x02\x03",

            "#1760F...So, sorry.\x02\x03",

            "Would you two let me stick with you again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x111,
        (
            "#1746F#5PHeh. Come ON. Really?\x02\x03",

            "#1741FAs if you even need to ask!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x113,
        "#1761F#12P...Thanks.\x02",
    )

    CloseMessageWindow()
    OP_62(0x112, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x112,
        (
            "#1751F#5PHahaha! What's gotten into you two? Anyone'd\x01",
            "look as you two now and think smooching and\x01",
            "wedding bells're in your future!\x02\x03",

            "#1756FYou've made up, so make with the kissing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x113,
        (
            "#1763F#12POh, shove it up your ass!\x02\x03",

            "#1767FBesides, YOU still owe me an apology!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x112,
        "#1753F#5PHuh? For what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x113,
        (
            "#1765F#12PWhen someone's frozen, you're s'posed to use an\x01",
            "item on them or something! You know, like a Curia\x01",
            "Balm!\x02\x03",

            "#1763FWere you TRYING to kill me?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x112, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #49
        0x112,
        "#1751F#5PH-Hey! It did the trick, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x113,
        (
            "#1765F#12PUgh... I guess.\x02\x03",

            "#1763FMaybe I do owe you one.\x02\x03",

            "#1761FThanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x112,
        (
            "#1753F#5PWh-What's gotten into you?\x02\x03",

            "#1755FW-Wait... Am I the one you wanna smooch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x113,
        "#1767F#12PIn your dreams.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x112,
        "#1751F#5PKidding, kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x111,
        "#1741F#5PHaha. Well, anyway. Let's get going!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x113,
        "#1761F#4PRight!\x02",
    )


    ChrTalk(    #56
        0x112,
        "#1756F#3PYou got it!\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_C4(0x1, 0x20000000)
    OP_A2(0x2F97)
    OP_B2(0x0, 0x1, 0x80)
    StopSound(0xAAB4, 0xFF78, 0x3E8)
    EventEnd(0x0)
    Return()

    # Function_6_12E2 end

    SaveToFile()

Try(main)
