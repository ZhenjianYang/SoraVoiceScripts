from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1306   ._SN',
        MapName             = 'Bose',
        Location            = 'C1306.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        'Sky Bandit Aaron',                     # 9
        'Sky Bandit Rosco',                     # 10
        'Sky Bandit Dino',                      # 11
        'Sky Bandit Lonnie',                    # 12
        'Sky Bandit',                           # 13
        'Sky Bandit',                           # 14
        'Sky Bandit',                           # 15
        'Sky Bandit',                           # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00360 ._CH',             # 00
        'ED6_DT07/CH00364 ._CH',             # 01
        'ED6_DT07/CH00361 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00130 ._CH',             # 06
        'ED6_DT09/CH10380 ._CH',             # 07
        'ED6_DT09/CH10381 ._CH',             # 08
        'ED6_DT09/CH10390 ._CH',             # 09
        'ED6_DT09/CH10391 ._CH',             # 0A
        'ED6_DT09/CH10250 ._CH',             # 0B
        'ED6_DT09/CH10251 ._CH',             # 0C
        'ED6_DT06/CH20074 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH00360P._CP',             # 00
        'ED6_DT07/CH00364P._CP',             # 01
        'ED6_DT07/CH00361P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00130P._CP',             # 06
        'ED6_DT09/CH10380P._CP',             # 07
        'ED6_DT09/CH10381P._CP',             # 08
        'ED6_DT09/CH10390P._CP',             # 09
        'ED6_DT09/CH10391P._CP',             # 0A
        'ED6_DT09/CH10250P._CP',             # 0B
        'ED6_DT09/CH10251P._CP',             # 0C
        'ED6_DT06/CH20074P._CP',             # 0D
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
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
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
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
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
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
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
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
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
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
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
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
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
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
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
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


    DeclMonster(
        X                   = -57220,
        Z                   = 0,
        Y                   = -50730,
        Unknown_0C          = 179,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7780,
        Z                   = 0,
        Y                   = 56000,
        Unknown_0C          = 261,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 53910,
        Z                   = 0,
        Y                   = 56840,
        Unknown_0C          = 123,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 104400,
        Z                   = 0,
        Y                   = 10510,
        Unknown_0C          = 331,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -1020,
        TriggerZ            = 0,
        TriggerY            = -145940,
        TriggerRange        = 800,
        ActorX              = -1020,
        ActorZ              = 1000,
        ActorY              = -145940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -57350,
        TriggerZ            = 0,
        TriggerY            = 108350,
        TriggerRange        = 800,
        ActorX              = -57350,
        ActorZ              = 1000,
        ActorY              = 108350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -142790,
        TriggerZ            = 0,
        TriggerY            = 58560,
        TriggerRange        = 1000,
        ActorX              = -142760,
        ActorZ              = 1500,
        ActorY              = 59200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -55470,
        TriggerZ            = 0,
        TriggerY            = -105270,
        TriggerRange        = 1000,
        ActorX              = -54920,
        ActorZ              = 1500,
        ActorY              = -105280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31A",          # 00, 0
        "Function_1_4ED",          # 01, 1
        "Function_2_54F",          # 02, 2
        "Function_3_565",          # 03, 3
        "Function_4_A8E",          # 04, 4
        "Function_5_AC3",          # 05, 5
        "Function_6_B11",          # 06, 6
        "Function_7_B4B",          # 07, 7
        "Function_8_B7E",          # 08, 8
        "Function_9_DE2",          # 09, 9
        "Function_10_EFC",         # 0A, 10
        "Function_11_12EC",        # 0B, 11
        "Function_12_1700",        # 0C, 12
        "Function_13_199E",        # 0D, 13
        "Function_14_1B0A",        # 0E, 14
    )


    def Function_0_31A(): pass

    label("Function_0_31A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_32E"),
        (131, "loc_340"),
        (101, "loc_353"),
        (SWITCH_DEFAULT, "loc_366"),
    )


    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x354)
    Event(0, 3)

    label("loc_33D")

    Jump("loc_366")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Event(0, 10)

    label("loc_350")

    Jump("loc_366")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 11)

    label("loc_363")

    Jump("loc_366")

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_END)), "loc_429")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    SetChrPos(0xA, 56490, 0, -52990, 350)
    SetChrPos(0xB, 56660, 0, -56070, 0)
    SetChrPos(0xD, 55510, 0, -54710, 45)
    SetChrPos(0xE, 55110, 0, -52150, 90)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    SetChrChipByIndex(0xA, 13)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xA, 0xFF)

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_END)), "loc_4EC")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrPos(0x8, 940, 0, -770, 0)
    SetChrPos(0x9, 930, 0, -3680, 90)
    SetChrPos(0xC, 510, 0, -2250, 300)
    SetChrPos(0xF, 500, 0, 580, 45)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0xF, 13)
    SetChrChipByIndex(0x8, 13)
    SetChrChipByIndex(0x9, 13)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xC, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    label("loc_4EC")

    Return()

    # Function_0_31A end

    def Function_1_4ED(): pass

    label("Function_1_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509")
    OP_1B(0x26, 0x0, 0x8)
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_50D")

    label("loc_509")

    OP_64(0x0, 0x1)

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F")
    OP_6F(0x2, 0)
    Jump("loc_526")

    label("loc_51F")

    OP_6F(0x2, 60)

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538")
    OP_6F(0x3, 0)
    Jump("loc_53F")

    label("loc_538")

    OP_6F(0x3, 60)

    label("loc_53F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_54E")
    OP_64(0x1, 0x1)

    label("loc_54E")

    Return()

    # Function_1_4ED end

    def Function_2_54F(): pass

    label("Function_2_54F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_564")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_54F")

    label("loc_564")

    Return()

    # Function_2_54F end

    def Function_3_565(): pass

    label("Function_3_565")

    EventBegin(0x0)
    OP_6D(3220, 1250, 4120, 0)
    SetChrPos(0x101, 5490, 3500, 5190, 270)
    SetChrPos(0x102, 5490, 3500, 5190, 270)
    SetChrPos(0x103, 5490, 3500, 5190, 270)
    SetChrPos(0x104, 5490, 3500, 5190, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)

    def lambda_5D6():
        OP_6D(3150, 0, 510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D6)
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0x103, 0x1, 0x0, 0x6)
    OP_43(0x104, 0x1, 0x0, 0x7)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #0
        0x101,
        (
            "#002FAnyone have a clue what this\x01",
            "place is...?\x02\x03",

            "It's way too big for these bandits\x01",
            "to have built, and it seems pretty\x01",
            "ancient.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    ChrTalk(    #1
        0x103,
        (
            "#020FIt almost feels like a stronghold of\x01",
            "some sort and I agree, this place\x01",
            "is pretty old.\x02\x03",

            "I wonder if people used hidden\x01",
            "forts like this one as hideouts\x01",
            "back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x104,
        (
            "#030FAs far as I've heard, the turmoil following\x01",
            "the Great Collapse continued on for several\x01",
            "hundred years.\x02\x03",

            "So it doesn't seem that strange to\x01",
            "me that something like this is still\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#004FThe Great Collapse?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#012FThe collapse of the ancient Zemurian\x01",
            "civilization which existed more than\x01",
            "1200 years ago.\x02\x03",

            "It's said that a huge natural\x01",
            "catastrophe wiped them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#501FOh, you mean like Professor Alba\x01",
            "said before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x103,
        (
            "#027FI tell you what though, for being a place\x01",
            "this hard to find, someone's got some\x01",
            "seriously bad taste in hideouts.\x02\x03",

            "#027FNot to mention there are all sorts of monsters\x01",
            "lurking around in here, too... I wonder if this\x01",
            "is how all men like to live?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #7
        0x102,
        "#018FUm, Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x104,
        (
            "#034FJust what kind of men are you\x01",
            "hanging out with...?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_565 end

    def Function_4_A8E(): pass

    label("Function_4_A8E")

    ClearChrFlags(0x101, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0x1388, 0x0)
    OP_8E(0xFE, 0xAB4, 0x0, 0xFFFFFB5A, 0x1388, 0x0)
    TurnDirection(0xFE, 0x102, 400)
    Return()

    # Function_4_A8E end

    def Function_5_AC3(): pass

    label("Function_5_AC3")

    Sleep(800)
    ClearChrFlags(0x102, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA82, 0x0, 0x370, 0xBB8, 0x0)
    OP_8E(0xFE, 0x726, 0x0, 0x6E, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_5_AC3 end

    def Function_6_B11(): pass

    label("Function_6_B11")

    Sleep(1600)
    ClearChrFlags(0x103, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD1B, 0x0, 0xC8, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_6_B11 end

    def Function_7_B4B(): pass

    label("Function_7_B4B")

    Sleep(2400)
    ClearChrFlags(0x104, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA82, 0x0, 0x370, 0xBB8, 0x0)
    Return()

    # Function_7_B4B end

    def Function_8_B7E(): pass

    label("Function_8_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE1")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC8")

    def lambda_BA8():
        OP_6D(-4700, 0, -147260, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BA8)
    Sleep(600)
    OP_8C(0x102, 90, 400)

    ChrTalk(    #9
        0x102,
        (
            "#012FHold on a second...\x02\x03",

            "I can hear someone talking on\x01",
            "the other side of the door.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C25():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C25)

    def lambda_C33():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C33)
    OP_8C(0x103, 90, 400)

    ChrTalk(    #10
        0x103,
        (
            "#022FIt sounds like some of the grunts. Let's\x01",
            "take care of them before we move on, so\x01",
            "there are no surprises behind us later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC6")

    label("loc_CC8")


    def lambda_CCE():
        OP_6D(-4700, 0, -147260, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_CCE)
    Sleep(600)
    OP_8C(0x104, 90, 400)

    ChrTalk(    #11
        0x104,
        (
            "#033FDo my ears deceive me...?\x02\x03",

            "I swear I can hear someone talking\x01",
            "on the other side of this door.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D5A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D5A)

    def lambda_D68():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D68)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #12
        0x101,
        (
            "#002FSky bandits, perhaps? If that's the case,\x01",
            "let's take them out first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC6")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_DE1")

    Return()

    # Function_8_B7E end

    def Function_9_DE2(): pass

    label("Function_9_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05The voices of some men can be heard.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #14
        0x102,
        (
            "#012FI can hear somebody talking again...\x01",
            "Shall we rush the room?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Rush in]\x01",      # 0
            "[Not yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_EE7"),
        (0, "loc_EEC"),
        (SWITCH_DEFAULT, "loc_EFB"),
    )


    label("loc_EE7")

    EventEnd(0x1)
    Jump("loc_EFB")

    label("loc_EEC")

    OP_A2(0x3FB)
    NewScene("ED6_DT01/C1304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_EFB")

    label("loc_EFB")

    Return()

    # Function_9_DE2 end

    def Function_10_EFC(): pass

    label("Function_10_EFC")

    EventBegin(0x0)
    OP_6D(59090, 0, -54570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 57770, 0, -52340, 180)
    SetChrPos(0xB, 59050, 0, -52450, 180)
    SetChrPos(0xD, 60650, 0, -51550, 180)
    SetChrPos(0xE, 56680, 0, -51410, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x101, 58000, 0, -56220, 0)
    SetChrPos(0x102, 57090, 0, -57040, 0)
    SetChrPos(0x103, 59130, 0, -56480, 0)
    SetChrPos(0x104, 59940, 0, -57280, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x103, 5)
    SetChrChipByIndex(0x104, 6)
    OP_0D()

    ChrTalk(    #15
        0xB,
        "Hold it right there, you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        "You're not getting past us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#004FY-You guys are back for more after\x01",
            "taking a righteous beating like\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#012FNow that's what I call tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#024FHmph. If you don't want to move,\x01",
            "then we're just going to force our\x01",
            "way through!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrChipByIndex(0xB, 2)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xD, 2)
    SetChrChipByIndex(0xE, 2)

    def lambda_112C():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_112C)

    def lambda_1147():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1147)

    def lambda_1162():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1162)

    def lambda_117D():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_117D)
    Sleep(400)
    Battle(0x38D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_11B0"),
        (SWITCH_DEFAULT, "loc_11B3"),
    )


    label("loc_11B0")

    OP_B4(0x0)
    Return()

    label("loc_11B3")

    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    SetChrPos(0xA, 56490, 0, -52990, 350)
    SetChrPos(0xB, 56660, 0, -56070, 0)
    SetChrPos(0xD, 55510, 0, -54710, 45)
    SetChrPos(0xE, 55110, 0, -52150, 90)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    SetChrChipByIndex(0xA, 13)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrPos(0x101, 58700, 0, -53950, 270)
    SetChrPos(0x102, 58700, 0, -53950, 270)
    SetChrPos(0x103, 58700, 0, -53950, 270)
    SetChrPos(0x104, 58700, 0, -53950, 270)
    OP_6D(58700, 0, -53950, 0)
    OP_6B(2600, 0)
    FadeToBright(1000, 0)
    OP_A2(0x359)
    EventEnd(0x0)
    Return()

    # Function_10_EFC end

    def Function_11_12EC(): pass

    label("Function_11_12EC")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(2880, 0, -3610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 2970, 0, -700, 180)
    SetChrPos(0x9, 1580, 0, -1100, 180)
    SetChrPos(0xC, 3050, 0, 910, 180)
    SetChrPos(0xF, 1640, 0, 500, 180)
    SetChrPos(0x101, 1560, 0, -5690, 0)
    SetChrPos(0x102, 510, 0, -6570, 0)
    SetChrPos(0x103, 2530, 0, -5860, 0)
    SetChrPos(0x104, 3240, 0, -6510, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x103, 5)
    SetChrChipByIndex(0x104, 6)
    OP_0D()

    ChrTalk(    #20
        0x8,
        "Don't think you're going up any further!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "Take the hostages and go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#007FSo you're back for more, huh...?\x01",
            "When will you learn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#012FWhat are you trying to do...\x01",
            "buy time for your leaders to\x01",
            "escape?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "Heh! They've done a lot for us\x01",
            "over the years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "Now it's time to return the favor!\x02",
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0xC, 2)
    SetChrChipByIndex(0xF, 2)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 2)

    def lambda_1540():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1540)

    def lambda_155B():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_155B)

    def lambda_1576():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1576)

    def lambda_1591():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1591)
    Sleep(500)
    Battle(0x38E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_15C4"),
        (SWITCH_DEFAULT, "loc_15C7"),
    )


    label("loc_15C4")

    OP_B4(0x0)
    Return()

    label("loc_15C7")

    SetChrPos(0x8, 940, 0, -770, 0)
    SetChrPos(0x9, 930, 0, -3680, 90)
    SetChrPos(0xC, 510, 0, -2250, 300)
    SetChrPos(0xF, 500, 0, 580, 45)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0xF, 13)
    SetChrChipByIndex(0x8, 13)
    SetChrChipByIndex(0x9, 13)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xC, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrPos(0x101, 3010, 0, -1740, 270)
    SetChrPos(0x102, 3010, 0, -1740, 270)
    SetChrPos(0x103, 3010, 0, -1740, 270)
    SetChrPos(0x104, 3010, 0, -1740, 270)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    OP_6D(3010, 0, -1740, 0)
    OP_6B(2600, 0)
    FadeToBright(1000, 0)
    OP_A2(0x35A)
    EventEnd(0x0)
    Return()

    # Function_11_12EC end

    def Function_12_1700(): pass

    label("Function_12_1700")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199D")
    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Fade(1000)
    SetChrPos(0x101, -56980, 0, 107430, 0)
    SetChrPos(0x102, -57900, 0, 106910, 0)
    SetChrPos(0x103, -57000, 0, 105940, 0)
    SetChrPos(0x104, -57970, 0, 105640, 0)
    OP_0D()
    Sleep(100)

    ChrTalk(    #26
        0x101,
        "#501FWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#010FI'm guessing it's an orbal vacuum.\x02\x03",

            "It looks like the newest model,\x01",
            "so it's probably stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#501FInteresting...\x02\x03",

            "#004F...Huh?\x02\x03",

            "What's this? There's something\x01",
            "stuffed inside...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #29
        "\x07\x00Found \x07\x02Black Notebook\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x14, 0x1, 0x8000)
    OP_3E(0x338, 1)
    OP_64(0x1, 0x1)
    Sleep(100)

    ChrTalk(    #30
        0x102,
        "#014FA notebook...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#505FYep, that's what it looks like to me.\x02\x03",

            "But what's something like this doing\x01",
            "inside a vacuum?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x103,
        (
            "#020FIt's probably something important.\x02\x03",

            "Let's hold onto it just in case.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #33
        0x101,
        "#006FYeah, good idea.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    ClearMapFlags(0x8000000)

    label("loc_199D")

    Return()

    # Function_12_1700 end

    def Function_13_199E(): pass

    label("Function_13_199E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A96")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x60, 1)"), scpexpr(EXPR_END)), "loc_1A17")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x00Found \x07\x02Bear Assault\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x370)
    Jump("loc_1A93")

    label("loc_1A17")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x00Found \x07\x02Bear Assault\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Bear Assault\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1A93")

    Jump("loc_1AFC")

    label("loc_1A96")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #36
        (
            "\x07\x05The chest is empty...because you emptied it.\x01",
            "Funny how that works, no?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x13)

    label("loc_1AFC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_199E end

    def Function_14_1B0A(): pass

    label("Function_14_1B0A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x116, 1)"), scpexpr(EXPR_END)), "loc_1B7F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00Found \x07\x02Strega-R\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x371)
    Jump("loc_1BF3")

    label("loc_1B7F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x00Found \x07\x02Strega-R\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Strega-R\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1BF3")

    Jump("loc_1C3E")

    label("loc_1BF6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        "\x07\x05The chest has nothing left to offer you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x14)

    label("loc_1C3E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1B0A end

    SaveToFile()

Try(main)
