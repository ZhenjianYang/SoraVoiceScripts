from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1401   ._SN',
        MapName             = 'Bose',
        Location            = 'C1401.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        'Sentry',                               # 9
        'Sentry',                               # 10
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
        Unknown_3A              = 60,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT09/CH10170 ._CH',             # 01
        'ED6_DT09/CH10171 ._CH',             # 02
        'ED6_DT09/CH11170 ._CH',             # 03
        'ED6_DT09/CH11171 ._CH',             # 04
        'ED6_DT09/CH11180 ._CH',             # 05
        'ED6_DT09/CH11181 ._CH',             # 06
        'ED6_DT09/CH11190 ._CH',             # 07
        'ED6_DT09/CH11191 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT09/CH10170P._CP',             # 01
        'ED6_DT09/CH10171P._CP',             # 02
        'ED6_DT09/CH11170P._CP',             # 03
        'ED6_DT09/CH11171P._CP',             # 04
        'ED6_DT09/CH11180P._CP',             # 05
        'ED6_DT09/CH11181P._CP',             # 06
        'ED6_DT09/CH11190P._CP',             # 07
        'ED6_DT09/CH11191P._CP',             # 08
    )

    DeclNpc(
        X                   = 1220,
        Z                   = -2070,
        Y                   = 185310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = -2070,
        Y                   = 185310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -31230,
        Z                   = -30,
        Y                   = 76720,
        Unknown_0C          = 165,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22600,
        Z                   = 0,
        Y                   = 45730,
        Unknown_0C          = 225,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1980,
        Z                   = 40,
        Y                   = 82660,
        Unknown_0C          = 164,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8330,
        Z                   = -1840,
        Y                   = 91320,
        Unknown_0C          = 114,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = -1960,
        Y                   = 58080,
        Unknown_0C          = 156,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = -1990,
        Y                   = 103160,
        Unknown_0C          = 43,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5530,
        Z                   = -1920,
        Y                   = 140390,
        Unknown_0C          = 293,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xBE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10740,
        Z                   = -2009,
        Y                   = 162000,
        Unknown_0C          = 284,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10420,
        Z                   = -1910,
        Y                   = 77510,
        Unknown_0C          = 103,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21780,
        Z                   = -2050,
        Y                   = 78280,
        Unknown_0C          = 162,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -330,
        Y                   = -4000,
        Z                   = 184860,
        Range               = 5340,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x2C808,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -26110,
        Y                   = -4000,
        Z                   = 69000,
        Range               = -38850,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x11558,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -9350,
        TriggerZ            = -1950,
        TriggerY            = 71290,
        TriggerRange        = 1500,
        ActorX              = -9350,
        ActorZ              = -450,
        ActorY              = 71290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19360,
        TriggerZ            = -1990,
        TriggerY            = 166110,
        TriggerRange        = 1000,
        ActorX              = 19810,
        ActorZ              = -490,
        ActorY              = 166800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D2",          # 00, 0
        "Function_1_31E",          # 01, 1
        "Function_2_358",          # 02, 2
        "Function_3_36E",          # 03, 3
        "Function_4_3D6",          # 04, 4
        "Function_5_7FE",          # 05, 5
        "Function_6_8EA",          # 06, 6
        "Function_7_A8C",          # 07, 7
        "Function_8_13A6",         # 08, 8
    )


    def Function_0_2D2(): pass

    label("Function_0_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2E9")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_2F7")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_2F7")

    SetMapFlags(0x10)
    OP_11(0xFF, 0xFF, 0xFF, 0x80E8, 0xD2F0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_31D")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_31D")

    Return()

    # Function_0_2D2 end

    def Function_1_31E(): pass

    label("Function_1_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32E")
    OP_71(0x0, 0x4)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_END)), "loc_33E")
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350")
    OP_6F(0x2, 0)
    Jump("loc_357")

    label("loc_350")

    OP_6F(0x2, 60)

    label("loc_357")

    Return()

    # Function_1_31E end

    def Function_2_358(): pass

    label("Function_2_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_358")

    label("loc_36D")

    Return()

    # Function_2_358 end

    def Function_3_36E(): pass

    label("Function_3_36E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-6987, -2000, 112486, 0)
    OP_6B(4500, 0)
    OP_6C(288000, 0)

    def lambda_39E():
        OP_6D(630, 3040, 186710, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39E)

    def lambda_3B6():
        OP_6B(2500, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B6)
    OP_6C(48000, 10000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_36E end

    def Function_4_3D6(): pass

    label("Function_4_3D6")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(2616, -2000, 188840, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)

    def lambda_406():
        OP_67(0, 3600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_406)

    def lambda_41E():
        OP_6B(3400, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41E)
    OP_6C(24000, 4000)
    Sleep(1000)
    OP_22(0xC1, 0x0, 0x64)
    PlayEffect(0x12, 0xFF, 0xFF, 2616, -2000, 188840, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, 2780, -2020, 190580, 209)
    SetChrPos(0x103, 2140, -2029, 191100, 190)
    SetChrPos(0x102, 2780, -2020, 191990, 178)
    SetChrPos(0x104, 2380, -2029, 192390, 184)
    OP_71(0x0, 0x4)
    OP_6B(3470, 0)
    OP_6B(3400, 80)
    Sleep(1000)

    def lambda_4D6():
        OP_6D(2180, -1900, 181510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4D6)

    def lambda_4EE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EE)

    def lambda_4FE():
        OP_6E(318, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4FE)

    def lambda_50E():
        OP_8E(0xFE, 0x97E, 0xFFFFF858, 0x2CFCE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50E)
    Sleep(200)

    def lambda_52E():
        OP_8E(0xFE, 0x6C2, 0xFFFFF830, 0x2D3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_52E)
    Sleep(200)

    def lambda_54E():
        OP_8E(0xFE, 0xD84, 0xFFFFF858, 0x2D1B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54E)
    Sleep(200)

    def lambda_56E():
        OP_8E(0xFE, 0xB54, 0xFFFFF84E, 0x2D618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_56E)
    Sleep(3000)

    ChrTalk(    #0
        0x101,
        "#004FThis...was a secret door...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x104,
        (
            "#033FThat's quite a neat little trick there.\x01",
            "I wouldn't expect anything less from\x01",
            "a secret fort.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #2
        0x102,
        (
            "#012F#4PThis looks like it's a corner of\x01",
            "the Nebel Valley.\x02\x03",

            "Schera, should we help the hostages\x01",
            "escape first?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_695():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_695)

    def lambda_6A3():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A3)
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #3
        0x103,
        (
            "#022FNo... We need to take out the\x01",
            "sky bandit boss first.\x02\x03",

            "If we're attacked while attempting to\x01",
            "escape, there's no way we'll be able\x01",
            "to protect that many people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#002FOh, that's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x104,
        (
            "#035FWell, then how about we get back in there\x01",
            "and have a face to face chat with the\x01",
            "gentleman running this fine operation?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x357)
    EventEnd(0x0)
    Return()

    # Function_4_3D6 end

    def Function_5_7FE(): pass

    label("Function_5_7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_8E9")
    EventBegin(0x1)
    OP_4A(0x8, 0)
    TurnDirection(0x8, 0x0, 400)

    def lambda_818():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_818)
    TurnDirection(0x1, 0x8, 400)

    ChrTalk(    #6
        0x8,
        (
            "Due to an ongoing investigation,\x01",
            "civilians are not permitted to\x01",
            "pass beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I'm sorry, but I'm going to have\x01",
            "to ask you to turn back.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8E9")

    Return()

    # Function_5_7FE end

    def Function_6_8EA(): pass

    label("Function_6_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CC")
    TurnDirection(0x103, 0x1, 400)

    def lambda_911():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_911)

    def lambda_91F():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_91F)
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #8
        0x103,
        (
            "#022FWe haven't arrested the sky bandits'\x01",
            "boss yet, so going any further could\x01",
            "prove to be dangerous.\x02\x03",

            "We need to return to the sky\x01",
            "bandits' hideout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A70")

    label("loc_9CC")

    TurnDirection(0x103, 0x0, 400)

    def lambda_9D9():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9D9)

    def lambda_9E7():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9E7)
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #9
        0x103,
        (
            "#022FHold on there, guys. We haven't dealt\x01",
            "with the sky bandit boss yet.\x02\x03",

            "Let's hurry and get back to\x01",
            "their hideout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A70")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A8B")

    Return()

    # Function_6_8EA end

    def Function_7_A8C(): pass

    label("Function_7_A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7A")
    SetMapFlags(0x8000000)
    OP_28(0x11, 0x1, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_B1F")
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        "\x07\x00Found \x07\x02Bear Claw\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x363)
    Jump("loc_B6F")

    label("loc_B1F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        (
            "\x07\x00Found \x07\x02Bear Claw\x07\x00\x01",
            "but inventory full so gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B6F")

    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_13A5")

    label("loc_B7A")

    OP_28(0x11, 0x1, 0x4)
    SetMapFlags(0x8000000)
    EventBegin(0x0)
    Fade(1000)
    OP_6C(125000, 0)
    SetChrPos(0x101, -7970, -2000, 71470, 270)
    SetChrPos(0x102, -7850, -2070, 72520, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD6")
    SetChrPos(0x103, -6790, -2009, 71120, 270)

    label("loc_BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF5")
    SetChrPos(0x104, -6370, -2009, 72240, 270)

    label("loc_BF5")

    OP_69(0x101, 0x0)
    OP_6C(135000, 2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_C6C")
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #12
        "\x07\x00Found \x07\x02Bear Claw\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x363)
    Jump("loc_CBC")

    label("loc_C6C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        (
            "\x07\x00Found \x07\x02Bear Claw\x07\x00\x01",
            "but inventory full so gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1202")

    ChrTalk(    #14
        0x101,
        (
            "#000FPhew! After all this walking we\x01",
            "finally found the dang thing.\x02\x03",

            "Now all we've got to do is tell\x01",
            "that old man in the Bose Market\x01",
            "about this place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3F")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #15
        0x103,
        (
            "#020FEstelle...because it's you,\x01",
            "I have to ask...\x02\x03",

            "Do you know the name of this\x01",
            "place?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #16
        0x101,
        (
            "#502FOh, come on, Schera!\x01",
            "What do you think I am? An idiot?\x02\x03",

            "This is the Neber Valley, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_E3F")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        (
            "#014FEstelle, do you know the name\x01",
            "of this place?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #18
        0x101,
        (
            "#502FCome on, Joshua! Quit acting like\x01",
            "I don't know anything.\x02\x03",

            "It's called the Neber Valley, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F94")

    ChrTalk(    #19
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x104,
        (
            "#030FHmm...\x02\x03",

            "Well, doesn't the name of this\x01",
            "place have a beautiful ring to it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #21
        0x102,
        (
            "#017FEstelle...\x02\x03",

            "It's the Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1064")

    label("loc_F94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101F")

    ChrTalk(    #22
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#027FThe name's definitely got a nice\x01",
            "sound to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #24
        0x102,
        (
            "#017FEstelle...\x02\x03",

            "It's the Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1064")

    label("loc_101F")


    ChrTalk(    #25
        0x102,
        (
            "#018F...\x02\x03",

            "#018FEstelle...this place is called\x01",
            "the Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1064")


    ChrTalk(    #26
        0x101,
        "#008FOh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AA")

    ChrTalk(    #27
        0x103,
        "#025FI'm glad I asked...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_10DA")

    label("loc_10AA")


    ChrTalk(    #28
        0x102,
        "#015FIt was a good thing I asked...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    label("loc_10DA")


    ChrTalk(    #29
        0x101,
        (
            "#009FGive me a break! I'm a growing\x01",
            "girl, if you haven't noticed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#018FI'm not sure what kind of excuse\x01",
            "that's supposed to be...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #31
        0x101,
        (
            "#008FAll right, all right, already!\x01",
            "It's back to work for us!\x02\x03",

            "Come on, let's get out of here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #32
        0x102,
        "#017FUnbelievable...\x02",
    )

    CloseMessageWindow()
    Jump("loc_139E")

    label("loc_1202")


    ChrTalk(    #33
        0x101,
        (
            "#000FThis is a Bear Claw, right?\x02\x03",

            "That reminds me. Wasn't somebody\x01",
            "looking for one of these?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12EE")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #34
        0x103,
        (
            "#020FThat's what it said on the bulletin\x01",
            "board, remember?\x02\x03",

            "Check your Bracer Notebook about\x01",
            "it later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_137B")

    label("loc_12EE")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #35
        0x102,
        (
            "#010FI'm sure that's what it said on the\x01",
            "bulletin board.\x02\x03",

            "Why don't you try checking your\x01",
            "Bracer Notebook about it later?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    label("loc_137B")


    ChrTalk(    #36
        0x101,
        "#006FOh, right! I'll do that.\x02",
    )

    CloseMessageWindow()

    label("loc_139E")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)

    label("loc_13A5")

    Return()

    # Function_7_A8C end

    def Function_8_13A6(): pass

    label("Function_8_13A6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1492")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x116, 1)"), scpexpr(EXPR_END)), "loc_141B")
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
    OP_A2(0x377)
    Jump("loc_148F")

    label("loc_141B")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_148F")

    Jump("loc_14E0")

    label("loc_1492")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        (
            "\x07\x05You've taken everything from me...\x01",
            "EVERYTHING!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x16)

    label("loc_14E0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_13A6 end

    SaveToFile()

Try(main)
