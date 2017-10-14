from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R3105   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3105.x',
        MapIndex            = 144,
        MapDefaultBGM       = "ed60029",
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
        'Captain Hoffman',                      # 9
        'Private Reno',                         # 10
        'Zeiss',                                # 11
        'Wolf Fort',                            # 12
        'Carnelia Tower',                       # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
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
        'ED6_DT09/CH10610 ._CH',             # 00
        'ED6_DT09/CH10611 ._CH',             # 01
        'ED6_DT09/CH10080 ._CH',             # 02
        'ED6_DT09/CH10081 ._CH',             # 03
        'ED6_DT09/CH10120 ._CH',             # 04
        'ED6_DT09/CH10121 ._CH',             # 05
        'ED6_DT09/CH10140 ._CH',             # 06
        'ED6_DT09/CH10141 ._CH',             # 07
        'ED6_DT09/CH10620 ._CH',             # 08
        'ED6_DT09/CH10621 ._CH',             # 09
        'ED6_DT09/CH10600 ._CH',             # 0A
        'ED6_DT09/CH10601 ._CH',             # 0B
        'ED6_DT09/CH10400 ._CH',             # 0C
        'ED6_DT09/CH10401 ._CH',             # 0D
        'ED6_DT09/CH11210 ._CH',             # 0E
        'ED6_DT09/CH11211 ._CH',             # 0F
        'ED6_DT09/CH11250 ._CH',             # 10
        'ED6_DT09/CH11251 ._CH',             # 11
        'ED6_DT07/CH01310 ._CH',             # 12
        'ED6_DT07/CH01640 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT09/CH10610P._CP',             # 00
        'ED6_DT09/CH10611P._CP',             # 01
        'ED6_DT09/CH10080P._CP',             # 02
        'ED6_DT09/CH10081P._CP',             # 03
        'ED6_DT09/CH10120P._CP',             # 04
        'ED6_DT09/CH10121P._CP',             # 05
        'ED6_DT09/CH10140P._CP',             # 06
        'ED6_DT09/CH10141P._CP',             # 07
        'ED6_DT09/CH10620P._CP',             # 08
        'ED6_DT09/CH10621P._CP',             # 09
        'ED6_DT09/CH10600P._CP',             # 0A
        'ED6_DT09/CH10601P._CP',             # 0B
        'ED6_DT09/CH10400P._CP',             # 0C
        'ED6_DT09/CH10401P._CP',             # 0D
        'ED6_DT09/CH11210P._CP',             # 0E
        'ED6_DT09/CH11211P._CP',             # 0F
        'ED6_DT09/CH11250P._CP',             # 10
        'ED6_DT09/CH11251P._CP',             # 11
        'ED6_DT07/CH01310P._CP',             # 12
        'ED6_DT07/CH01640P._CP',             # 13
    )

    DeclNpc(
        X                   = 1400,
        Z                   = -40,
        Y                   = 9260,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2490,
        Z                   = -30,
        Y                   = 7960,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -74130,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 64319,
        Z                   = 10,
        Y                   = -52920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 10040,
        Z                   = -130,
        Y                   = 67800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -36940,
        Z                   = -10,
        Y                   = 10890,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28070,
        Z                   = 80,
        Y                   = 10280,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17490,
        Z                   = 0,
        Y                   = -1540,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4150,
        Z                   = -60,
        Y                   = 15540,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32970,
        Z                   = -30,
        Y                   = 25660,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26690,
        Z                   = 50,
        Y                   = 5570,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13500,
        Z                   = -20,
        Y                   = -4890,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34620,
        Z                   = -50,
        Y                   = -10530,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37440,
        Z                   = -50,
        Y                   = -24530,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15930,
        Z                   = 0,
        Y                   = -38970,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35920,
        Z                   = -20,
        Y                   = -35400,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29740,
        Z                   = -110,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19490,
        Z                   = 0,
        Y                   = -17710,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12390,
        Z                   = 50,
        Y                   = -16010,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5230,
        Z                   = 0,
        Y                   = -27150,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -3130,
        TriggerZ            = 30,
        TriggerY            = -11320,
        TriggerRange        = 1000,
        ActorX              = -3130,
        ActorZ              = 30,
        ActorY              = -10750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13630,
        TriggerZ            = 0,
        TriggerY            = 35620,
        TriggerRange        = 1500,
        ActorX              = 13630,
        ActorZ              = 1200,
        ActorY              = 35620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36850,
        TriggerZ            = 80,
        TriggerY            = 17250,
        TriggerRange        = 1000,
        ActorX              = 33720,
        ActorZ              = -1000,
        ActorY              = 13980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3FA",          # 00, 0
        "Function_1_42C",          # 01, 1
        "Function_2_52B",          # 02, 2
        "Function_3_541",          # 03, 3
        "Function_4_9DD",          # 04, 4
        "Function_5_D3A",          # 05, 5
        "Function_6_EA6",          # 06, 6
        "Function_7_1E64",         # 07, 7
        "Function_8_1E80",         # 08, 8
        "Function_9_1EA1",         # 09, 9
        "Function_10_1EC2",        # 0A, 10
        "Function_11_1EE3",        # 0B, 11
        "Function_12_1F69",        # 0C, 12
        "Function_13_1FC2",        # 0D, 13
        "Function_14_2020",        # 0E, 14
    )


    def Function_0_3FA(): pass

    label("Function_0_3FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_428")
    SetChrPos(0x9, 5620, 20, -7270, 45)

    label("loc_428")

    OP_A2(0x0)
    Return()

    # Function_0_3FA end

    def Function_1_42C(): pass

    label("Function_1_42C")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x23002F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E9")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1C), scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    OP_CE(0x0, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_498")
    OP_28(0x6E, 0x1, 0x40)
    Jump("loc_4E9")

    label("loc_498")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD")
    OP_28(0x6E, 0x1, 0x20)
    Jump("loc_4E9")

    label("loc_4AD")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C2")
    OP_28(0x6E, 0x1, 0x10)
    Jump("loc_4E9")

    label("loc_4C2")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D7")
    OP_28(0x6E, 0x1, 0x8)
    Jump("loc_4E9")

    label("loc_4D7")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    OP_28(0x6E, 0x1, 0x4)

    label("loc_4E9")

    OP_A3(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE")
    OP_6F(0x1, 0)
    Jump("loc_505")

    label("loc_4FE")

    OP_6F(0x1, 60)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_52A")

    Return()

    # Function_1_42C end

    def Function_2_52B(): pass

    label("Function_2_52B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_540")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_52B")

    label("loc_540")

    Return()

    # Function_2_52B end

    def Function_3_541(): pass

    label("Function_3_541")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B")
    Call(0, 6)
    Jump("loc_9D9")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_7C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741")

    ChrTalk(    #0
        0xFE,
        "Hi there, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "How'd the repairs to the hot\x01",
            "springs go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000FThey went great, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1040FWe completed them safely.\x02\x03",

            "Thank you for your assistance,\x01",
            "Captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Glad to hear it went well!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Hopefully, even a little thing like this\x01",
            "will help calm the citizenry a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "The Royal Army strives to keep order\x01",
            "and stability in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I hope we can continue to cooperate\x01",
            "to overcome these hardships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1000FI hope so, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20CE)
    Jump("loc_7C0")

    label("loc_741")


    ChrTalk(    #9
        0xFE,
        (
            "I'm glad to hear the hot springs repairs\x01",
            "went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I hope we can continue to cooperate to\x01",
            "overcome these hardships.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C0")

    Jump("loc_9D9")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_864")

    ChrTalk(    #11
        0xFE,
        (
            "At times like this, it's only right that we\x01",
            "should be going the extra arge to keep\x01",
            "the people at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Good luck restoring the Elmo springs.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D9")

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95D")

    ChrTalk(    #13
        0xFE,
        (
            "Our controls stopped responding\x01",
            "en route to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "We barely managed to land without\x01",
            "incident here on the plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "From what we can tell, all orbal devices\x01",
            "have stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Hmm... I wonder what happened.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_9D9")

    label("loc_95D")


    ChrTalk(    #17
        0xFE,
        (
            "Our controls stopped responding\x01",
            "en route to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "We barely managed to land without\x01",
            "incident here on the plains.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D9")

    TalkEnd(0x8)
    Return()

    # Function_3_541 end

    def Function_4_9DD(): pass

    label("Function_4_9DD")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F7")
    Call(0, 6)
    Jump("loc_D36")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(    #19
        0xFE,
        "I'm looking over the ship, just in case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Actually...I'm really just killing time.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 45, 400)
    SetChrFlags(0x9, 0x10)
    OP_A2(0x2)
    Jump("loc_AA3")

    label("loc_A74")


    ChrTalk(    #21
        0xFE,
        "All right! Nothing wrong with the struts.\x02",
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_D36")

    label("loc_AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B56")

    ChrTalk(    #22
        0xFE,
        (
            "The Elmo hot springs? Man, I haven't\x01",
            "been there in forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I'd love to go take a soak sometime soon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Anyway, good luck with those repairs!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_BC6")

    label("loc_B56")


    ChrTalk(    #25
        0xFE,
        (
            "The Elmo hot springs? Man, I haven't\x01",
            "been there in forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "I'd love to go take a soak sometime soon!\x02",
    )

    CloseMessageWindow()

    label("loc_BC6")

    Jump("loc_D36")

    label("loc_BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9E")

    ChrTalk(    #27
        0xFE,
        "Phew! We managed to land safely...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Of all the places in Liberl to land, of course\x01",
            "we end up in the middle of the Tratt Plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Doubt the rescue team will find US any\x01",
            "time soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_D36")

    label("loc_C9E")


    ChrTalk(    #30
        0xFE,
        (
            "Of all the places in Liberl to land, of course\x01",
            "we end up in the middle of the Tratt Plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Doubt the rescue team will find US any\x01",
            "time soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D36")

    TalkEnd(0x9)
    Return()

    # Function_4_9DD end

    def Function_5_D3A(): pass

    label("Function_5_D3A")

    OP_EA(0x2, 0xEF, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x0, 0xA)
    AddSepith(0x1, 0xA)
    AddSepith(0x2, 0xA)
    AddSepith(0x3, 0xA)
    AddSepith(0x4, 0xA)
    AddSepith(0x5, 0xA)
    AddSepith(0x6, 0xA)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #32
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1506)
    Jump("loc_E94")

    label("loc_E30")


    AnonymousTalk(    #33
        (
            "\x07\x05Now that my contents are gone, I guess I'll just\x01",
            "have to turn to crime. I hope you're happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_E94")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_D3A end

    def Function_6_EA6(): pass

    label("Function_6_EA6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECB")
    Call(0, 11)
    Call(0, 12)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_ECB")

    Fade(1000)
    OP_6D(2520, -50, 8109, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(179000, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, 2690, -70, 10480, 225)
    SetChrPos(0x102, 3500, -20, 9710, 225)
    SetChrPos(0xF8, 3300, 50, 11900, 225)
    SetChrPos(0xF9, 4280, 60, 11100, 225)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_8C(0x8, 45, 0)
    OP_8C(0x9, 45, 0)
    OP_0D()

    ChrTalk(    #34
        0x8,
        "#2PSay, who are you lot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1025F#5PWe're from the Bracer Guild, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x05Estelle's team explained the situation and asked about\x01",
            "the combustion engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #37
        0x8,
        (
            "#2PI see! I'd totally forgotten about it in\x01",
            "the chaos.\x02\x03",

            "Yes, we have the engine in our cargo hold.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #38
        0x8,
        "#4PReno! Give me a hand.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #39
        0x9,
        "#1PYes, sir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)

    def lambda_10F9():

        label("loc_10F9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_10F9")

    QueueWorkItem2(0x101, 2, lambda_10F9)

    def lambda_110A():

        label("loc_110A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_110A")

    QueueWorkItem2(0x102, 2, lambda_110A)

    def lambda_111B():

        label("loc_111B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_111B")

    QueueWorkItem2(0xF8, 2, lambda_111B)

    def lambda_112C():

        label("loc_112C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_112C")

    QueueWorkItem2(0xF9, 2, lambda_112C)
    OP_6D(2520, -50, 8109, 0)
    OP_67(0, 2970, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(179000, 0)
    OP_6E(359, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1184():
        OP_67(0, 4960, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1184)
    SetChrPos(0x8, 5830, 1000, 1450, 135)
    SetChrPos(0x9, 5830, 1000, 1450, 315)
    ClearChrFlags(0x8, 0x80)

    def lambda_11C3():
        OP_8F(0xFE, 0x546, 0xFFFFFFC4, 0x21F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11C3)
    Sleep(600)
    ClearChrFlags(0x9, 0x80)

    def lambda_11E8():
        OP_8F(0xFE, 0x88E, 0xFFFFFFC4, 0x1E6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11E8)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    Sleep(200)
    OP_8F(0x8, 0x546, 0xFFFFFFC4, 0x21F2, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 45, 400)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 45, 400)

    ChrTalk(    #40
        0x8,
        "#2PSorry to keep you waiting.\x02",
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xA96, 0xFFFFFFCE, 0x24EA, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #41
        "\x07\x00Received #1037i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x40D, 1)
    OP_8F(0x9, 0x88E, 0xFFFFFFC4, 0x1E6E, 0x7D0, 0x0)

    ChrTalk(    #42
        0x101,
        "#1006F#5PWe've got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        "#1040F#6PSorry to trouble you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#4PNot at all. I'm sorry we bothered picking it\x01",
            "up if things were going to end up like this.\x02\x03",

            "Still, all this to help get a hot spring\x01",
            "working in a situation like this...\x02\x03",

            "Bracers seem to have different priorities\x01",
            "than we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1013F#5PUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#1043F#6PForgive us. We know things are\x01",
            "difficult right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#4PNo, please don't misunderstand me.\x01",
            "I wasn't being sarcastic.\x02\x03",

            "For a soldier, being unable to use your\x01",
            "orbal weaponry is nerve-racking.\x02\x03",

            "We're all struggling to figure out some\x01",
            "other way to fight off our enemies.\x02\x03",

            "Meanwhile, you guys are moving around\x01",
            "with all the confidence in the world. We\x01",
            "could learn a thing or two from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1025F#5PAhaha...\x02\x03",

            "#1016FWe, umm... We're just doing what\x01",
            "we think is right, is all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B3")

    ChrTalk(    #49
        0x108,
        (
            "#070F#1PTo be honest, we're not too sure what\x01",
            "we should be doing at this point, either.\x02\x03",

            "All any of us can do is grope around\x01",
            "and try to find an answer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_16B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1751")

    ChrTalk(    #50
        0x103,
        (
            "#027F#1PWe're hardly paragons of enlightenment\x01",
            "and wisdom ourselves, sir.\x02\x03",

            "We're all simply groping in the dark,\x01",
            "looking for an answer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_1751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1802")

    ChrTalk(    #51
        0x106,
        (
            "#051F#1PHeh, we're sort of wanderin' around\x01",
            "holdin' our butts right now, too, to be\x01",
            "honest.\x02\x03",

            "Think all any of us can do is just try\x01",
            "and trip over the answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1802")


    ChrTalk(    #52
        0x8,
        (
            "#4PHaha, true enough.\x02\x03",

            "At times like this, it's only right that we\x01",
            "should be going the extra arge to keep\x01",
            "the people at ease.\x02\x03",

            "Good luck restoring the hot springs,\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18DA")

    ChrTalk(    #53
        0x107,
        "#061F#5PThank you!\x02",
    )

    CloseMessageWindow()

    label("loc_18DA")


    ChrTalk(    #54
        0x101,
        "#1006F#5PYou bet. Leave it to us!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_6D(15760, -50, -20140, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 15020, 10, -21640, 180)
    SetChrPos(0x102, 15950, -30, -21640, 180)
    SetChrPos(0xF8, 14650, 20, -20780, 180)
    SetChrPos(0xF9, 16400, -30, -20780, 180)
    OP_43(0x101, 0x1, 0x0, 0x7)
    OP_43(0x102, 0x1, 0x0, 0x8)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    Sleep(400)

    def lambda_19B9():
        OP_6D(15150, 70, -30990, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19B9)

    def lambda_19D1():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19D1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0xF8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as have gasoline\x01",                                         # 0
            "Set as don't have gasoline but have introduction letter\x01",      # 1
            "Set as have neither gasoline nor introduction letter\x01",         # 2
            "No change\x01",                                                    # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1ACE"),
        (1, "loc_1AD4"),
        (2, "loc_1ADD"),
        (SWITCH_DEFAULT, "loc_1AE6"),
    )


    label("loc_1ACE")

    OP_A2(0x2011)
    Jump("loc_1AE6")

    label("loc_1AD4")

    OP_A3(0x2011)
    OP_A2(0x2010)
    Jump("loc_1AE6")

    label("loc_1ADD")

    OP_A3(0x2011)
    OP_A3(0x2010)
    Jump("loc_1AE6")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_END)), "loc_1C80")
    OP_28(0xC2, 0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA3")
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #55
        0x101,
        (
            "#1006F#5PAll right. Now we've got everything.\x02\x03",

            "Should we get back to Elmo and work\x01",
            "on the pump?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #56
        0x107,
        "#061F#6PYeah, I'm ready to work on it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C7D")

    label("loc_1BA3")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #57
        0x101,
        (
            "#1006F#5PAll right, we've got all the parts, but...\x02\x03",

            "#1015FWe're kind of missing a Tita to actually\x01",
            "work on the pump, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#1040F#4PWe are.\x02\x03",

            "Let's return to the guildhouse and meet\x01",
            "up with Tita.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7D")

    Jump("loc_1E2E")

    label("loc_1C80")


    ChrTalk(    #59
        0x101,
        (
            "#1006F#5POkay, we've got the engine.\x02\x03",

            "#1015FNow we just need that gasoline...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_END)), "loc_1DB3")

    ChrTalk(    #60
        0x102,
        (
            "#1040F#4PAccording to Chief Murdock, there should\x01",
            "be some at the Ruan harbor delivered from\x01",
            "the Republic.\x02\x03",

            "We should probably check there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1006F#5PYeah, we've gotten this far.\x01",
            "Let's see this to the end!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2E")

    label("loc_1DB3")


    ChrTalk(    #62
        0x102,
        (
            "#1035F#4PThe central factory may have a supply,\x01",
            "like before.\x02\x03",

            "#1040FLet's check there first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1006F#5PGood idea.\x02",
    )

    CloseMessageWindow()

    label("loc_1E2E")

    OP_A2(0x200F)
    OP_28(0xC2, 0x1, 0x80)
    SetChrPos(0x8, 1400, -40, 9260, 135)
    SetChrPos(0x9, 2590, -40, 7810, 315)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_6_EA6 end

    def Function_7_1E64(): pass

    label("Function_7_1E64")

    OP_8E(0xFE, 0x3692, 0x3C, 0xFFFF815C, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_1E64 end

    def Function_8_1E80(): pass

    label("Function_8_1E80")

    Sleep(150)
    OP_8E(0xFE, 0x3CC8, 0x50, 0xFFFF82B0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_1E80 end

    def Function_9_1EA1(): pass

    label("Function_9_1EA1")

    Sleep(350)
    OP_8E(0xFE, 0x3700, 0x32, 0xFFFF8878, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_9_1EA1 end

    def Function_10_1EC2(): pass

    label("Function_10_1EC2")

    Sleep(350)
    OP_8E(0xFE, 0x3D5E, 0x32, 0xFFFF88BE, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_10_1EC2 end

    def Function_11_1EE3(): pass

    label("Function_11_1EE3")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F5C"),
        (1, "loc_1F62"),
        (SWITCH_DEFAULT, "loc_1F68"),
    )


    label("loc_1F5C")

    OP_A2(0x1200)
    Jump("loc_1F68")

    label("loc_1F62")

    OP_A2(0x1201)
    Jump("loc_1F68")

    label("loc_1F68")

    Return()

    # Function_11_1EE3 end

    def Function_12_1F69(): pass

    label("Function_12_1F69")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_12_1F69 end

    def Function_13_1FC2(): pass

    label("Function_13_1FC2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #64
        (
            "\x07\x05North: Carnelia Tower\x01",
            "※Beware of Monsters!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1FC2 end

    def Function_14_2020(): pass

    label("Function_14_2020")

    EventBegin(0x1)

    ChrTalk(    #65
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_204C():
        OP_6D(34900, 70, 15500, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_204C)

    def lambda_2064():
        OP_6B(3250, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2064)

    def lambda_2074():
        OP_6C(270000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2074)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211A")
    OP_C0(0xE, 0x23, 0x8FF2, 0x50, 0x4362, 0xE1, 0x83B8, 0xFFFFFC18, 0x369C)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_2129")

    label("loc_211A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2129")
    EventEnd(0x1)

    label("loc_2129")

    Return()

    # Function_14_2020 end

    SaveToFile()

Try(main)
