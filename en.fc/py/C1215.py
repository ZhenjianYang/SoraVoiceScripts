from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1215   ._SN',
        MapName             = 'Bose',
        Location            = 'C1215.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'Professor Alba',                       # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster in a Chest',                   # 12
        'Monster in a Chest',                   # 13
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
        'ED6_DT07/CH02050 ._CH',             # 00
        'ED6_DT09/CH10410 ._CH',             # 01
        'ED6_DT07/CH00101 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00121 ._CH',             # 04
        'ED6_DT09/CH10411 ._CH',             # 05
        'ED6_DT09/CH10440 ._CH',             # 06
        'ED6_DT09/CH10441 ._CH',             # 07
        'ED6_DT09/CH10410 ._CH',             # 08
        'ED6_DT09/CH10411 ._CH',             # 09
        'ED6_DT09/CH10420 ._CH',             # 0A
        'ED6_DT09/CH10421 ._CH',             # 0B
        'ED6_DT09/CH10430 ._CH',             # 0C
        'ED6_DT09/CH10431 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02050P._CP',             # 00
        'ED6_DT09/CH10410P._CP',             # 01
        'ED6_DT07/CH00101P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00121P._CP',             # 04
        'ED6_DT09/CH10411P._CP',             # 05
        'ED6_DT09/CH10440P._CP',             # 06
        'ED6_DT09/CH10441P._CP',             # 07
        'ED6_DT09/CH10410P._CP',             # 08
        'ED6_DT09/CH10411P._CP',             # 09
        'ED6_DT09/CH10420P._CP',             # 0A
        'ED6_DT09/CH10421P._CP',             # 0B
        'ED6_DT09/CH10430P._CP',             # 0C
        'ED6_DT09/CH10431P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 380,
        Y                   = 3530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4280,
        Z                   = 10000,
        Y                   = 4280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4190,
        Z                   = 10000,
        Y                   = 3730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 20670,
        Z                   = 0,
        Y                   = -5460,
        Unknown_0C          = 151,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x94,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19250,
        Z                   = 0,
        Y                   = 8320,
        Unknown_0C          = 329,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x97,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8520,
        Z                   = 0,
        Y                   = 19510,
        Unknown_0C          = 271,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x91,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17540,
        Z                   = 0,
        Y                   = 12440,
        Unknown_0C          = 223,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x96,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3030,
        Y                   = -1000,
        Z                   = 14100,
        Range               = 2970,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3DAE,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 11840,
        TriggerZ            = 0,
        TriggerY            = 40,
        TriggerRange        = 1000,
        ActorX              = 12620,
        ActorZ              = 1500,
        ActorY              = 60,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11810,
        TriggerZ            = 0,
        TriggerY            = -40,
        TriggerRange        = 1000,
        ActorX              = -12660,
        ActorZ              = 1500,
        ActorY              = 90,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_293",          # 01, 1
        "Function_2_2C6",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_DA7",          # 04, 4
        "Function_5_E11",          # 05, 5
        "Function_6_E7B",          # 06, 6
        "Function_7_10C9",         # 07, 7
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Return()

    # Function_0_292 end

    def Function_1_293(): pass

    label("Function_1_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5")
    OP_6F(0x0, 0)
    Jump("loc_2AC")

    label("loc_2A5")

    OP_6F(0x0, 60)

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE")
    OP_6F(0x1, 0)
    Jump("loc_2C5")

    label("loc_2BE")

    OP_6F(0x1, 60)

    label("loc_2C5")

    Return()

    # Function_1_293 end

    def Function_2_2C6(): pass

    label("Function_2_2C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2C6")

    label("loc_2DB")

    Return()

    # Function_2_2C6 end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA6")
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #0
        0x101,
        "#004FAh! It's that guy again...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Fade(1000)
    OP_6C(225000, 0)

    def lambda_35C():
        OP_6D(40, 380, 3090, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_35C)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_91(0x8, 0x3E8, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(200)
    OP_63(0x8)
    OP_91(0x8, 0xFFFFFC18, 0x0, 0x258, 0x3E8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_91(0x8, 0xFFFFFE0C, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
    Sleep(200)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_43(0xA, 0x1, 0x0, 0x5)
    OP_63(0x8)
    OP_91(0x8, 0x1F4, 0x0, 0x12C, 0x3E8, 0x0)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_8C(0x8, 315, 200)
    OP_8C(0x8, 45, 200)
    OP_8C(0x8, 0, 100)
    Sleep(400)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #1
        0x8,
        (
            "#131FY-Yikes!\x02\x03",

            "H-Help!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C3():
        OP_8E(0x9, 0xFFFFFC68, 0x0, 0x1234, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C3)

    def lambda_4DE():
        OP_8E(0xA, 0x4F6, 0x0, 0x1266, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DE)
    OP_91(0x8, 0x0, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x103, 4)
    SetChrPos(0x101, -60, 0, 11030, 182)
    SetChrPos(0x102, 670, 0, 11700, 180)
    SetChrPos(0x103, -810, 0, 12320, 180)

    def lambda_55E():
        OP_90(0x101, 0x0, 0x0, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55E)

    def lambda_579():
        OP_90(0x102, 0x0, 0x0, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_579)

    def lambda_594():
        OP_90(0x103, 0x0, 0x0, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_594)
    WaitChrThread(0x101, 0x1)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x3EF, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5D7"),
        (SWITCH_DEFAULT, "loc_5DC"),
    )


    label("loc_5D7")

    OP_B4(0x0)
    Jump("loc_5DC")

    label("loc_5DC")

    EventBegin(0x0)
    AddParty(0xD, 0x3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrPos(0x101, 0, 0, 5400, 180)
    SetChrPos(0x102, -910, 0, 6810, 180)
    SetChrPos(0x103, 800, 0, 6800, 180)
    SetChrPos(0x10E, 0, 380, 3420, 0)
    OP_6D(0, 0, 4440, 0)

    def lambda_669():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_669)

    def lambda_679():
        OP_6D(-720, 0, 5910, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_679)

    def lambda_691():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_691)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    Sleep(400)

    ChrTalk(    #2
        0x10E,
        (
            "#131FOh...thank you...y-you really\x01",
            "saved my hide!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#006F#6PWell, if it isn't Professor Alba.\x02\x03",

            "I was all tense because I thought\x01",
            "it might be the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10E,
        (
            "#130FAh ha ha, it's been a while now,\x01",
            "hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x103,
        "#023FYou know this guy?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #6
        0x101,
        (
            "#000F#6PYeah, he's a scholar who's been\x01",
            "investigating the towers in Liberl.\x02\x03",

            "When we were escorting those reporters,\x01",
            "we ran into him at the Esmelas Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10E,
        (
            "#130FAh ha ha, and here it looks like\x01",
            "I'm being rescued again.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #8
        0x103,
        (
            "#022FWe heard talking earlier. Is there\x01",
            "someone else in here with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10E,
        (
            "#130FOh, goodness, you heard that?\x02\x03",

            "How embarrassing. It's a bad habit\x01",
            "I have whenever I'm doing my\x01",
            "research...\x02\x03",

            "If I don't say what I'm thinking out\x01",
            "loud, I can't collect my thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#506F#6POh, so you were just talking to\x01",
            "yourself, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#020FEhh, we're all a little crazy sometimes.\x01",
            "At any rate, we'd best save the chit-chat\x01",
            "for another time.\x02\x03",

            "We should get out of this place before\x01",
            "more monsters come looking for a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10E,
        (
            "#131FEh...?\x02\x03",

            "You're leaving already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        "#023FWhy? Is there a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10E,
        "#131FM-My research here isn't finished...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020FOh. Well, in that case, take as\x01",
            "much time as you need.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #16
        0x103,
        (
            "#026FEstelle, Joshua, we're leaving now.\x02\x03",

            "Mr. Researcher here says he can\x01",
            "find his own way back to town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10E,
        "#131FEh?\x02",
    )

    CloseMessageWindow()

    def lambda_BDC():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDC)

    def lambda_BEA():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEA)
    Sleep(400)

    ChrTalk(    #18
        0x101,
        "#509F#6P(Wow! Now that was scary...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#018F#6P(She totally threatened the\x01",
            "poor guy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #20
        0x10E,
        (
            "#131FWait! I-I'm sorry!\x01",
            "I'm ready to leave now!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #21
        0x103,
        (
            "#027FTeehee. Men are definitely best\x01",
            "when they're so agreeable!\x02\x03",

            "Hey, Estelle and Joshua!\x01",
            "Let's go! Pronto!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#007F#6PO-kay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#017F#6PGood grief...\x02",
    )

    CloseMessageWindow()

    def lambda_D4E():
        OP_92(0x101, 0x103, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4E)

    def lambda_D63():
        OP_92(0x102, 0x103, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D63)

    def lambda_D78():
        OP_92(0x10E, 0x103, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_D78)
    OP_69(0x103, 0x578)
    WaitChrThread(0x10E, 0x1)
    OP_28(0xF, 0x4, 0x8)
    OP_28(0xF, 0x1, 0x4)
    OP_28(0xF, 0x1, 0x8)
    EventEnd(0x0)

    label("loc_DA6")

    Return()

    # Function_3_2DC end

    def Function_4_DA7(): pass

    label("Function_4_DA7")

    OP_22(0xBD, 0x0, 0x64)
    OP_8E(0x9, 0xFFFFEF48, 0x0, 0x10B8, 0x4650, 0x0)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0x9, 0xFFFFEEB2, 0x0, 0x12A2, 0x7D0, 0x7D0)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0x9, 0xFFFFF77C, 0x0, 0x196E, 0x578, 0xBB8)
    SetChrChipByIndex(0x9, 1)
    SetChrFlags(0x9, 0x1)
    TurnDirection(0xFE, 0x8, 400)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Return()

    # Function_4_DA7 end

    def Function_5_E11(): pass

    label("Function_5_E11")

    Sleep(600)
    OP_8E(0xA, 0x105E, 0x0, 0xE92, 0x4650, 0x0)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0xA, 0xE1A, 0x0, 0x12AC, 0x9C4, 0x9C4)
    OP_22(0x212, 0x0, 0x64)
    OP_96(0xA, 0x938, 0x0, 0x196E, 0x578, 0xBB8)
    SetChrChipByIndex(0xA, 1)
    SetChrFlags(0xA, 0x1)
    TurnDirection(0xFE, 0x8, 400)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_5_E11 end

    def Function_6_E7B(): pass

    label("Function_6_E7B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 12620, 3000, 60, 320)
    TurnDirection(0xB, 0x0, 0)

    def lambda_ECA():
        OP_8F(0xFE, 0x314C, 0x5DC, 0x3C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_ECA)

    def lambda_EE5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EE5)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(    #24
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xA0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F38"),
        (2, "loc_F4A"),
        (1, "loc_F5A"),
        (SWITCH_DEFAULT, "loc_F5D"),
    )


    label("loc_F38")

    OP_A2(0x382)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_F5D")

    label("loc_F4A")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_F5A")

    OP_B4(0x0)
    Return()

    label("loc_F5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF8, 1)"), scpexpr(EXPR_END)), "loc_FB4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #25
        "\x07\x00Found \x07\x02Chain Mail\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x380)
    Jump("loc_102A")

    label("loc_FB4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #26
        (
            "\x07\x00Found \x07\x02Chain Mail\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Chain Mail\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_102A")

    Jump("loc_10BB")

    label("loc_102D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #27
        (
            "\x07\x05The chest is empty because someone came and took\x01",
            "the stuff out. You wouldn't know who did that now,\x01",
            "would you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0xD)

    label("loc_10BB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_E7B end

    def Function_7_10C9(): pass

    label("Function_7_10C9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AB")
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, -12660, 3000, 90, 320)
    TurnDirection(0xC, 0x0, 0)

    def lambda_1118():
        OP_8F(0xFE, 0xFFFFCE8C, 0x5DC, 0x5A, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1118)

    def lambda_1133():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1133)
    ClearChrFlags(0xC, 0x80)

    AnonymousTalk(    #28
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x9F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1186"),
        (2, "loc_1198"),
        (1, "loc_11A8"),
        (SWITCH_DEFAULT, "loc_11AB"),
    )


    label("loc_1186")

    OP_A2(0x383)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_11AB")

    label("loc_1198")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_11A8")

    OP_B4(0x0)
    Return()

    label("loc_11AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x144, 1)"), scpexpr(EXPR_END)), "loc_1208")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        "\x07\x00Found \x07\x02Emerald Talisman\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x381)
    Jump("loc_128A")

    label("loc_1208")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #30
        (
            "\x07\x00Found \x07\x02Emerald Talisman\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Emerald Talisman\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_128A")

    Jump("loc_12D4")

    label("loc_128D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #31
        "\x07\x05The chest is empty... How depressing...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0xE)

    label("loc_12D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10C9 end

    SaveToFile()

Try(main)
